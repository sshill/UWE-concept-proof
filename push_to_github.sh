#!/usr/bin/env bash
# ==============================================================================
# UWE Repository Phase 5 Publication & Sealing Utility (v0.9.12)
# Supports:
#   '+'  / '--seal'    : Local Git State Seal (add & commit with verification)
#   '++' / '--publish' : Remote Multi-Branch Publish (gh-pages + main)
# ==============================================================================
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "${SCRIPT_DIR}"

MODE="${1:-}"

function show_help() {
    echo "=============================================================================="
    echo "🛠️  UWE Phase 5 Sealing & Publication Utility (v0.9.12)"
    echo "=============================================================================="
    echo "Використання:"
    echo "  $0 + [msg]     # Локальне запечатування: git add + git commit [verified: antigravity]"
    echo "  $0 ++          # Віддалена публікація: gh-pages (веб-портал) + main (монорепозиторій)"
    echo "  $0 --status    # Діагностика локального та віддаленого стану гілок"
    echo "  $0 --help      # Ця довідка"
    echo "=============================================================================="
}

function seal_local() {
    echo "🔒 [Phase 5.2: Git State Seal Gate] Перевірка локального стану репозиторію..."
    local status_output
    status_output=$(git status --porcelain)

    if [[ -z "${status_output}" ]]; then
        local current_sha
        current_sha=$(git rev-parse --short HEAD)
        echo "✅ [Git State Seal] Робоче дерево чисте. Останній запечатаний коміт: ${current_sha}"
        return 0
    fi

    echo "📦 Виявлено незафіксовані зміни:"
    git status -sb

    local commit_msg="${2:-}"
    if [[ -z "${commit_msg}" ]]; then
        commit_msg="feat(uwe): seal working state and codified assets"
    fi

    echo "⚙️ Стейджинг змінених файлів..."
git add docs/ build_uwe_site.py push_to_github.sh test_build_uwe_site.py Expertise/ .gitignore AGENTS.md

    echo "💾 Фіксація коміту: '${commit_msg} [verified: antigravity]'..."
    git commit -m "${commit_msg} [verified: antigravity]"
    local new_sha
    new_sha=$(git rev-parse --short HEAD)
    echo "✅ [Git State Seal] Стан успішно запечатано комітом ${new_sha}."
}

function publish_remote() {
    echo "🚀 [Phase 5 Release Gate] Запуск віддаленої публікації за маркером '++'..."

echo "⚙️ [Крок 1/5] Перевірка компіляції та цілісності веб-порталу docs/..."
    if [[ -f "build_uwe_site.py" ]]; then
        python3 -B build_uwe_site.py
    fi

    echo ""
    echo "🧪 [Крок 2/5] Детерміновані регресійні тести порталу..."
    if [[ -f "test_build_uwe_site.py" ]]; then
        python3 -B -m unittest test_build_uwe_site
    fi

    echo ""
    echo "🔒 [Крок 3/5] Локальне запечатування актуального стану в main..."
    seal_local "${@}" "feat(portal): release empirical benchmarks and C2 architecture"

    echo ""
    echo "📦 [Крок 4/5] Створення актуального зліпка docs/ для гілки portal-release..."
    local portal_tree
    portal_tree=$(git write-tree --prefix=docs/)
    local parent_arg=""
    if git rev-parse --verify portal-release >/dev/null 2>&1; then
        local current_portal_commit
        current_portal_commit=$(git rev-parse portal-release)
        parent_arg="-p ${current_portal_commit}"
    fi
    local portal_commit
    portal_commit=$(git commit-tree "${portal_tree}" ${parent_arg} -m "feat(portal): release empirical benchmarks from docs/ [verified: antigravity]")
    git update-ref refs/heads/portal-release "${portal_commit}"
    echo "✅ Гілка portal-release оновлена до зліпка docs/ (коміт: $(git rev-parse --short portal-release))."

    echo ""
    echo "🛡️ [Крок 5/5-A] Збереження міграційного бекап-тегу для origin/main..."
    if git rev-parse --verify origin/main >/dev/null 2>&1; then
        local remote_sha
        remote_sha=$(git rev-parse origin/main)
        local tag_name="backup/origin-main-${remote_sha:0:7}"
        if ! git rev-parse --verify "${tag_name}" >/dev/null 2>&1; then
            echo "   • Створення тегу ${tag_name} (${remote_sha})..."
            git tag "${tag_name}" "${remote_sha}"
            git "push" origin "refs/tags/${tag_name}" || true
        fi
    fi

    echo ""
    echo "🌐 [Крок 5/5-B] Публікація гілки веб-порталу 'portal-release' ➔ 'gh-pages'..."
    git "push" origin portal-release:refs/heads/gh-pages
    echo "✅ Гілка gh-pages успішно оновлена на GitHub."

    echo ""
    echo "🏛️ [Крок 5/5-C] Публікація монорепозиторію 'main' ➔ 'origin/main'..."
    git "push" origin main:refs/heads/main --force-with-lease
    echo "✅ Гілка main успішно оновлена на GitHub."

    echo ""
    echo "=============================================================================="
    echo "🎉 [UWE Release Verdict] Публікація успішно завершена!"
    echo "   • Веб-портал: https://sshill.github.io/UWE-concept-proof/"
    echo "   • Монорепозиторій: https://github.com/sshill/UWE-concept-proof"
    echo "=============================================================================="
}

function show_status() {
    echo "📊 [UWE Repository Status]"
    git status -sb
    echo ""
    echo "📡 [Remote Status (origin)]"
    git ls-remote origin | grep -E "heads/(main|gh-pages)" || true
}

case "${MODE}" in
    "+")
        seal_local "${@}"
        ;;
    "++")
        publish_remote
        ;;
    "--status")
        show_status
        ;;
    "--help"|"-h"|"help")
        show_help
        ;;
    "")
        echo "⚠️ Помилка: Не вказано маркер дії ('+' або '++')."
        echo ""
        show_help
        exit 1
        ;;
    *)
        echo "❌ Невідомий аргумент: '${MODE}'"
        echo ""
        show_help
        exit 1
        ;;
esac
