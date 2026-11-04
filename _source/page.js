(() => {
  const $ = (s, r = document) => r.querySelector(s);
  const $$ = (s, r = document) => [...r.querySelectorAll(s)];
  const reduceMotion = matchMedia('(prefers-reduced-motion: reduce)');

  /* ── Page data (written by build.py) ───── */
  const EX = JSON.parse($('#pageData').textContent);

  // Notes summary is the notes' own first sentence, so nothing has to be hand-written
  const notes = $('#notesBody').textContent.trim();
  $('#notesSummary').textContent = notes.split(/(?<=[.;])\s/)[0].replace(/[;.]$/, '');

  /* ── State ─────────────────────────────── */
  const state = { avail: EX.avail, credits: '2', creditValue: '100', ship: 'both', times: 'single', slot: null, badge: EX.badge };

  // Multiple start times on the day (filler from build.py until the API provides them)
  const TIMES = EX.times;
  const multi = () => state.times === 'multi';
  const slot = () => TIMES.find(t => t.id === state.slot) || null;
  const needsTime = () => multi() && !slot();
  const effAvail = () => multi() ? (slot() ? slot().status : 'available') : state.avail;
  const startTime = () => multi() ? (slot() ? slot().time : null) : EX.start;
  const timeList = () => TIMES.map(t => t.time).join(', ').replace(/, ([^,]*)$/, ' or $1');
  const STATUS_TEXT = { available: 'Available', limited: 'Limited Capacity', soldout: 'Sold Out' };

  // Availability is a fixed label from the excursion system — no live seat counts
  const AVAIL = {
    available: { pill: null, cta: 'Reserve' },
    limited:   { pill: '<b>Limited Capacity</b>', cta: 'Reserve' },
    // Live seat count when the excursion system provides one (e.g. "1 Spot Left")
    spots:     { pill: `<b>${EX.spots} ${EX.spots === 1 ? 'Spot' : 'Spots'} Left</b>`, cta: 'Reserve' },
    soldout:   { pill: '<b>Sold Out</b>', muted: true, cta: 'Join waitlist' },
  };
  // Credit value comes from the credits system: $100, $200 or $300 (confirm with product)
  const creditHTML = c => { const v = '$' + state.creditValue; return c === '1' ? `You have <b>a ${v} excursion credit</b>`
                        : c === '0' ? '' : `You have <b>2 excursion credits of ${v}</b>`; };
  // With more than one credit, say plainly that each guest uses one
  const multiCredit = () => state.credits === '2' || state.credits === 'banner';
  const creditText = c => creditHTML(c).replace(/<\/?b>/g, '');

  function apply() {
    const a = AVAIL[effAvail()];
    $$('[data-badge]').forEach(b => b.hidden = b.dataset.badge !== state.badge);
    $('#xpBadges').hidden = state.badge === 'none';
    const pill = $('#statusPill');
    pill.classList.toggle('show', !!a.pill);
    pill.classList.toggle('muted', !!a.muted);
    $('#statusText').innerHTML = a.pill || '';
    $('#cta').textContent = needsTime() ? 'Select a time' : a.cta;

    // Hero start time: one time, or a picker until a time is chosen
    const st = startTime();
    $('#startLabel').textContent = multi() && !st ? 'Start times' : 'Start time';
    $('#startValue').innerHTML = multi()
      ? `<button class="key-value" data-open="times" aria-haspopup="dialog">${st || TIMES.length + ' times'}<svg class="i"><use href="#i-right"/></svg></button>`
      : `<div class="key-value">${st}</div>`;
    $('#barLine2').innerHTML = EX.dateShort + ' · ' + (st || `<span class="pick">${TIMES.length} times</span>`);
    $('#times').hidden = !multi();
    $('#timeChips').innerHTML = TIMES.map(t => `<button class="chip${t.status === 'soldout' ? ' soldout' : ''}" role="radio" aria-checked="${t.id === state.slot}" data-time="${t.id}">
      <span class="t">${t.time}</span><span class="s${t.status === 'limited' ? ' warn' : ''}">${STATUS_TEXT[t.status]}</span></button>`).join('');

    const ct = creditText(state.credits);
    $('#creditTitle').innerHTML = creditHTML(state.credits);
    $('#bannerTitle').textContent = `2 excursion credits of $${state.creditValue} available`;
    $$('[data-credit-sub]').forEach(el => el.hidden = !multiCredit());
    $('#creditCard').hidden = !ct;
    $('#creditBanner').classList.toggle('hidden', state.credits !== 'banner' || bannerDismissed || window.scrollY > 160);
  }

  /* ── Toast / hand-offs ─────────────────── */
  const toast = $('#toast');
  let toastTimer;
  function showToast(msg) {
    toast.textContent = msg;
    toast.classList.add('show');
    clearTimeout(toastTimer);
    toastTimer = setTimeout(() => toast.classList.remove('show'), 2200);
  }
  document.addEventListener('click', e => {
    const h = e.target.closest('[data-handoff]');
    if (!h || h.disabled) return;
    e.preventDefault();
    showToast(`Hand-off: ${h.dataset.handoff}`);
  });

  // Primary CTA: pick a time first when the day has several start times
  function primaryAction(from) {
    if (needsTime()) return openDrawer('times', from);
    showToast(`${AVAIL[effAvail()].cta}${multi() ? ' · ' + startTime() : ''} → booking flow`);
  }
  $('#cta').addEventListener('click', e => primaryAction(e.currentTarget));
  function pickTime(id) { state.slot = id; apply(); }
  document.addEventListener('click', e => {
    const c = e.target.closest('#timeChips [data-time]');
    if (c) return pickTime(c.dataset.time);
    const o = e.target.closest('[data-open]');
    if (o) openDrawer(o.dataset.open, o);
  });

  /* ── Scroll: parallax, glass sheen, compact header ── */
  const hero = $('#hero'), heroBg = $('.hero-bg'), photo = $('#photo'), wash = $('#wash');
  const heroCard = $('#heroCard'), compact = $('#compact');
  const glassEls = [heroCard, ...$$('.fact')];
  let ticking = false, compactOn = false, bannerDismissed = false;

  function onScroll() {
    ticking = false;
    const y = Math.max(0, window.scrollY);
    const heroH = hero.offsetHeight;
    const p = Math.min(1, y / heroH);

    if (!reduceMotion.matches && y < heroH + 200) {
      // Photo holds nearly still (70% of scroll speed on phones, 55% wider up) so the
      // glass cards keep sliding over it instead of off its bottom edge.
      const drift = innerWidth < 768 ? 0.7 : 0.55;
      heroBg.style.setProperty('--photo-y', (y * drift).toFixed(1) + 'px');
      // Zoom runs over the photo's own height (not the whole hero) so it reads early: up to +12%.
      const zoomP = Math.min(1, y / photo.offsetHeight);
      photo.style.setProperty('--photo-s', (1 + zoomP * 0.12).toFixed(4));
      photo.style.setProperty('--dim', (p * 0.25).toFixed(3));
      wash.style.setProperty('--wash-y', (y * drift * 0.6).toFixed(1) + 'px');
      const blur = (14 + p * 10).toFixed(1) + 'px';
      glassEls.forEach((el, i) => {
        el.style.setProperty('--glass-blur', blur);
        el.style.setProperty('--sheen-y', (-10 + p * 140 + i * 6).toFixed(1) + '%');
        el.style.setProperty('--sheen-x', (25 + p * 50).toFixed(1) + '%');
      });
    }

    const show = heroCard.getBoundingClientRect().bottom < 60;
    if (show !== compactOn) {
      compactOn = show;
      compact.classList.toggle('show', show);
      compact.setAttribute('aria-hidden', String(!show));
      $$('button', compact).forEach(b => b.tabIndex = show ? 0 : -1);
      if (!show) setCompactExpanded(false);
    }

    if (state.credits === 'banner' && !bannerDismissed) {
      $('#creditBanner').classList.toggle('hidden', y > 160);
    }
  }
  window.addEventListener('scroll', () => { if (!ticking) { ticking = true; requestAnimationFrame(onScroll); } }, { passive: true });
  window.addEventListener('resize', onScroll);

  function setCompactExpanded(on) {
    compact.classList.toggle('expanded', on);
    $('#compactTitle').setAttribute('aria-expanded', String(on));
  }
  $('#compactTitle').addEventListener('click', () => setCompactExpanded(!compact.classList.contains('expanded')));

  $('#bannerClose').addEventListener('click', () => { bannerDismissed = true; $('#creditBanner').classList.add('hidden'); });

  /* ── Disclosures ───────────────────────── */
  function toggleCollapse(btn, panel, labels) {
    const open = btn.getAttribute('aria-expanded') !== 'true';
    btn.setAttribute('aria-expanded', String(open));
    panel.classList.toggle('open', open);
    panel.inert = !open;
    if (labels) btn.querySelector('span').textContent = open ? labels[1] : labels[0];
  }
  const inertClosed = root => $$('.collapse', root).forEach(p => p.inert = !p.classList.contains('open'));
  inertClosed(document);
  $('#readMore').addEventListener('click', e => toggleCollapse(e.currentTarget, $('#desc'), ['Read the full description', 'Show less']));
  // Accordions on the page and inside drawers (FAQ): several can be open at once
  document.addEventListener('click', e => {
    const b = e.target.closest('button.acc-head, button.credit-head');
    if (b) toggleCollapse(b, b.nextElementSibling);
  });

  /* ── Drawers / modals ─────────────────── */
  const layer = $('#layer'), sheet = $('#sheet'), body = $('#sheetBody'), label = $('#sheetLabel');
  let opener = null, current = null;

  function fillPricing() {
    const ct = creditText(state.credits);
    $('[data-slot="credits"]', body).hidden = !ct;
    $('[data-slot="credit-title"]', body).innerHTML = creditHTML(state.credits);
    $$('[data-credit-sub]', body).forEach(el => el.hidden = !multiCredit());
    const cta = $('[data-slot="cta"]', body);
    cta.textContent = needsTime() ? 'Select a time' : AVAIL[effAvail()].cta;
    cta.addEventListener('click', () => needsTime() ? openDrawer('times', $('#cta')) : (closeDrawer(), primaryAction()));
  }
  // Start-time rows in the Duration and Price details drawers
  function fillStart() {
    const st = startTime();
    $$('[data-slot="start"]', body).forEach(el => el.textContent = st || timeList());
    $$('[data-slot="start-label"]', body).forEach(el => el.textContent = st ? 'Start time' : 'Start times');
  }
  function fillTimes() {
    const box = $('[data-slot="options"]', body);
    box.innerHTML = TIMES.map(t => {
      const cur = t.id === state.slot;
      return `<button class="level time-opt${cur ? ' current' : ''}" role="radio" aria-checked="${cur}" data-pick="${t.id}">
        <span class="txt"><b>${t.time}</b> <small class="${t.status === 'limited' ? 'warn' : ''}">· ${STATUS_TEXT[t.status]}</small></span>
        <span class="radio" aria-hidden="true"></span></button>`;
    }).join('');
    box.addEventListener('click', e => {
      const o = e.target.closest('[data-pick]');
      if (!o) return;
      pickTime(o.dataset.pick);
      closeDrawer();
      showToast(`${slot().time} selected`);
    });
  }

  function openDrawer(name, from) {
    const t = document.getElementById('t-' + name);
    if (!t) return;
    opener = from || document.activeElement;
    current = name;
    label.textContent = t.dataset.label;
    body.replaceChildren(t.content.cloneNode(true));
    inertClosed(body);
    body.scrollTop = 0;
    // Long, scrolling content (FAQ) opens full height so expanding an answer never resizes the sheet
    sheet.classList.toggle('full', 'full' in t.dataset);
    if (name === 'pricing') { fillPricing(); $('#barPrice').setAttribute('aria-expanded', 'true'); }
    if (name === 'duration') $('[data-slot="aboard-row"]', body).hidden = state.ship !== 'both';
    if (name === 'duration' || name === 'pricing') fillStart();
    if (name === 'times') fillTimes();
    sheet.style.setProperty('--drag', '0px');
    layer.setAttribute('aria-hidden', 'false');
    layer.classList.add('open');
    document.body.classList.add('locked');
    requestAnimationFrame(() => sheet.focus({ preventScroll: true }));
  }
  function closeDrawer() {
    if (!layer.classList.contains('open')) return;
    layer.classList.remove('open');
    layer.setAttribute('aria-hidden', 'true');
    document.body.classList.remove('locked');
    $('#barPrice').setAttribute('aria-expanded', 'false');
    current = null;
    // Back to where the reader left the page (e.g. the FAQ row)
    if (opener && opener.focus) opener.focus({ preventScroll: true });
  }
  $$('[data-drawer]').forEach(b => b.addEventListener('click', () => {
    if (b.dataset.drawer === 'pricing' && current === 'pricing') return closeDrawer();
    openDrawer(b.dataset.drawer, b);
  }));
  layer.addEventListener('click', e => { if (e.target.closest('[data-close]')) closeDrawer(); });
  document.addEventListener('keydown', e => {
    if (!layer.classList.contains('open')) return;
    if (e.key === 'Escape') return closeDrawer();
    if (e.key === 'Tab') { // focus trap
      const f = $$('button:not([disabled]), a[href]', sheet);
      if (!f.length) return;
      const first = f[0], last = f[f.length - 1];
      if (e.shiftKey && (document.activeElement === first || document.activeElement === sheet)) { e.preventDefault(); last.focus(); }
      else if (!e.shiftKey && document.activeElement === last) { e.preventDefault(); first.focus(); }
    }
  });

  // Swipe-down to dismiss (bottom-sheet mode only). Inside scrolling content it only
  // starts when the content is already at the top, so scrolling never closes the sheet.
  const isSheet = () => innerWidth < 768;
  let startY = null, dy = 0;
  function dragStart(e) {
    if (!isSheet()) return;
    if (e.currentTarget === body && body.scrollTop > 0) return;
    if (e.target.closest('button') && e.currentTarget !== body) return;
    startY = e.clientY; dy = 0;
  }
  function dragMove(e) {
    if (startY === null) return;
    dy = Math.max(0, e.clientY - startY);
    if (dy > 4) { sheet.classList.add('dragging'); sheet.style.setProperty('--drag', dy + 'px'); }
  }
  function dragEnd() {
    if (startY === null) return;
    sheet.classList.remove('dragging');
    if (dy > 110) closeDrawer(); else sheet.style.setProperty('--drag', '0px');
    startY = null;
  }
  [$('#sheetHead'), body].forEach(el => el.addEventListener('pointerdown', dragStart));
  window.addEventListener('pointermove', dragMove);
  window.addEventListener('pointerup', dragEnd);
  window.addEventListener('pointercancel', dragEnd);

  /* ── Prototype state switcher ─────────── */
  // Rule: picking a state scrolls to the element it changed and flashes it, so the reviewer sees the result
  const CHANGED = {
    badge:   () => $('#heroCard'),
    avail:   () => $('#cardWrap'),
    times:   () => multi() ? $('#times') : $('#heroCard'),
    credits: () => $('#creditCard').hidden ? $('#price') : $('#creditCard'),
    creditValue: () => $('#creditCard').hidden ? $('#price') : $('#creditCard'),
    ship:    () => $('[data-drawer="duration"]'),
  };
  function revealChange(name, value) {
    if (name === 'credits' && value === 'banner') return; // the banner has its own jump to the top
    const el = CHANGED[name] && CHANGED[name]();
    if (!el) return;
    el.scrollIntoView({ behavior: reduceMotion.matches ? 'auto' : 'smooth', block: 'center' });
    el.classList.remove('proto-flash');
    void el.offsetWidth; // restart the animation
    el.classList.add('proto-flash');
    setTimeout(() => el.classList.remove('proto-flash'), 1800);
    // Ship times live in the Duration drawer, so open it once the tile is in view
    if (name === 'ship') setTimeout(() => openDrawer('duration', el), 500);
  }
  const DEFAULTS = { ...state };
  const banner = $('#creditBanner');
  function toTop() { window.scrollTo({ top: 0, behavior: 'instant' }); }

  $('#protoPanel').addEventListener('change', e => {
    const { name, value } = e.target;
    if (name === 'times') {
      state.times = value === 'single' ? 'single' : 'multi';
      state.slot = value === 'multi-picked' ? TIMES[0].id : null;
    } else state[name] = value;
    if (name === 'credits') bannerDismissed = false;
    apply();
    revealChange(name, value);
    if (name === 'credits' && value === 'banner') {
      // Jump to the top, then let the banner slide in so its entrance plays
      banner.classList.add('hidden');
      toTop();
      setTimeout(() => { if (state.credits === 'banner' && !bannerDismissed) banner.classList.remove('hidden'); }, 450);
    }
  });
  $('#protoReset').addEventListener('click', () => {
    Object.assign(state, DEFAULTS);
    bannerDismissed = false;
    $('#protoPanel').reset();
    if (layer.classList.contains('open')) closeDrawer();
    apply();
    toTop();
    showToast('States reset');
  });

  apply();
  onScroll();
})();
