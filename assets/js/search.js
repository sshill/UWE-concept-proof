// Instant Client-Side Filter & Dual Search for UWE Cases
document.addEventListener('DOMContentLoaded', () => {
  const searchInput = document.getElementById('case-search');
  const cards = document.querySelectorAll('.case-item');
  const domainPills = document.querySelectorAll('.domain-pill');
  const vendorPills = document.querySelectorAll('.vendor-pill');
  const specSegs = document.querySelectorAll('.spec-seg');
  
  let activeDomain = 'ALL';
  let activeVendor = 'ALL';

  function applyFilter() {
    const q = (searchInput ? searchInput.value : '').toLowerCase().trim();
    let visibleCount = 0;

    cards.forEach(card => {
      const text = card.textContent.toLowerCase();
      const domain = card.getAttribute('data-domain') || '';
      const vendor = card.getAttribute('data-vendor') || '';

      const domainMatch = (activeDomain === 'ALL' || domain === activeDomain);
      const vendorMatch = (activeVendor === 'ALL' || vendor === activeVendor);
      const textMatch = !q || text.includes(q);

      if (domainMatch && vendorMatch && textMatch) {
        card.style.display = 'block';
        visibleCount++;
      } else {
        card.style.display = 'none';
      }
    });

    const countDisplay = document.getElementById('visible-count');
    if (countDisplay) {
      countDisplay.textContent = visibleCount;
    }
  }

  if (searchInput) {
    searchInput.addEventListener('input', applyFilter);
  }

  domainPills.forEach(pill => {
    pill.addEventListener('click', () => {
      domainPills.forEach(p => p.classList.remove('active'));
      pill.classList.add('active');
      activeDomain = pill.getAttribute('data-domain-filter') || 'ALL';
      applyFilter();
    });
  });

  vendorPills.forEach(pill => {
    pill.addEventListener('click', () => {
      vendorPills.forEach(p => p.classList.remove('active'));
      pill.classList.add('active');
      activeVendor = pill.getAttribute('data-vendor-filter') || 'ALL';
      applyFilter();
    });
  });

  specSegs.forEach(seg => {
    seg.addEventListener('click', () => {
      const targetDomain = seg.getAttribute('data-domain-filter') || 'ALL';
      domainPills.forEach(p => {
        if (p.getAttribute('data-domain-filter') === targetDomain) {
          p.classList.add('active');
        } else {
          p.classList.remove('active');
        }
      });
      activeDomain = targetDomain;
      applyFilter();
    });
  });
});
