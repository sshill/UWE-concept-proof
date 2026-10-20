// Instant Client-Side Filter & Search for UWE Cases
document.addEventListener('DOMContentLoaded', () => {
  const searchInput = document.getElementById('case-search');
  const cards = document.querySelectorAll('.case-item');
  const pills = document.querySelectorAll('.filter-pill');
  let activeDomain = 'ALL';

  function applyFilter() {
    const q = (searchInput ? searchInput.value : '').toLowerCase().trim();
    cards.forEach(card => {
      const text = card.textContent.toLowerCase();
      const domain = card.getAttribute('data-domain') || '';
      const domainMatch = (activeDomain === 'ALL' || domain === activeDomain);
      const textMatch = !q || text.includes(q);
      card.style.display = (domainMatch && textMatch) ? 'block' : 'none';
    });
  }

  if (searchInput) {
    searchInput.addEventListener('input', applyFilter);
  }

  pills.forEach(pill => {
    pill.addEventListener('click', () => {
      pills.forEach(p => p.classList.remove('active'));
      pill.classList.add('active');
      activeDomain = pill.getAttribute('data-filter') || 'ALL';
      applyFilter();
    });
  });
});
