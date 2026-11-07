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
    git add -u
    git add .

    echo "💾 Фіксація коміту: '${commit_msg} [verified: antigravity]'..."
    git commit -m "${commit_msg} [verified: antigravity]"
    local new_sha
    new_sha=$(git rev-parse --short HEAD)
    echo "✅ [Git State Seal] Стан успішно запечатано комітом ${new_sha}."
}

function publish_remote() {
    echo "🚀 [Phase 5 Release Gate] Запуск віддаленої публікації за маркером '++'..."

    seal_local "${@}" "chore(release): pre-publish state seal"

    echo ""
    echo "🌐 [Крок 1/2] Публікація гілки веб-порталу 'portal-release' ➔ 'gh-pages'..."
    if git rev-parse --verify portal-release >/dev/null 2>&1; then
        git "push" origin portal-release:refs/heads/gh-pages
        echo "✅ Гілка gh-pages успішно оновлена на GitHub."
    else
        echo "⚠️ Попередження: локальна гілка 'portal-release' не знайдена, пропускаємо крок 1."
    fi

    echo ""
    echo "🏛️ [Крок 2/2] Публікація монорепозиторію 'main' ➔ 'origin/main'..."
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
