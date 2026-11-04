"""Builds one HTML page per live HAL excursion into the parent folder.

    python3 build.py

Every page shares page.css byte for byte; only the trailing "This page's photo" block differs.
All copy comes from excursions.py (verbatim from the live pages)."""
import html, os, re
from excursions import (EXCURSIONS, SHIP_TIMES_FILLER, BADGES, STATUS, ACTIVITY_LEVELS,
                        CANCELLATION_HTML, FAQ)

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.dirname(HERE)
CSS = open(os.path.join(HERE, "page.css"), encoding="utf-8").read().rstrip()


def curly(s):
    return s.replace("'", "’")


def T(s):  # plain text
    return curly(html.escape(s, quote=False))


def H(s):  # trusted HTML from excursions.py
    return curly(s)


def paras(items):
    return "\n".join(f"<p>{H(p)}</p>" for p in items)


ICONS = """<svg width="0" height="0" style="position:absolute" aria-hidden="true">
  <symbol id="i-back" viewBox="0 0 22 22"><path d="M13.75 4.58 7.33 11l6.42 6.42"/></symbol>
  <symbol id="i-close" viewBox="0 0 22 22"><path d="M5.5 5.5l11 11M16.5 5.5l-11 11"/></symbol>
  <symbol id="i-right" viewBox="0 0 18 18"><path d="M6.75 4.5 11.25 9l-4.5 4.5"/></symbol>
  <symbol id="i-down" viewBox="0 0 20 20"><path d="M5 7.5 10 12.5 15 7.5"/></symbol>
  <symbol id="i-up" viewBox="0 0 14 14"><path d="M3.5 8.75 7 5.25l3.5 3.5"/></symbol>
  <symbol id="i-clock" viewBox="0 0 20 20"><circle cx="10" cy="10" r="7.5"/><path d="M10 5.83V10l2.5 1.67"/></symbol>
  <symbol id="i-pulse" viewBox="0 0 20 20"><path d="M2.5 10h3.33l2.5-5.83 3.34 11.66L14.17 10h3.33"/></symbol>
  <symbol id="i-access" viewBox="0 0 20 20"><circle cx="9.17" cy="3.33" r="1.5"/><path d="M9.17 6.25v2.08m0 0v2.5h4.16l2.09 4.59M9.17 8.33h3.75"/><path d="M6.67 8.75a4.58 4.58 0 1 0 6.33 5.83"/></symbol>
  <symbol id="i-meals" viewBox="0 0 20 20"><path d="M5.5 2.5v4.17a1.67 1.67 0 0 0 3.33 0V2.5M7.17 2.5v15M14.17 17.5V2.5c-1.84 0-2.92 2.08-2.92 5.42 0 1.66.83 2.5 2.92 2.5"/></symbol>
  <symbol id="i-anchor" viewBox="0 0 20 20"><circle cx="10" cy="4.17" r="1.67"/><path d="M10 5.83V17.5M7.08 8.75h5.84M3.75 11.67c.42 3.33 3 5.83 6.25 5.83s5.83-2.5 6.25-5.83M3.75 11.67 2.5 12.92M3.75 11.67 5 12.92M16.25 11.67 15 12.92M16.25 11.67l1.25 1.25"/></symbol>
  <symbol id="i-ship" viewBox="0 0 20 20"><path d="M2.92 11.67h14.16l-1.87 4.16H4.79zM5.83 11.67V8.75h8.34v2.92M8.75 8.75V5.83h2.5v2.92M2.5 18.33c1.25 0 1.25-.83 2.5-.83s1.25.83 2.5.83 1.25-.83 2.5-.83 1.25.83 2.5.83 1.25-.83 2.5-.83 1.25.83 2.5.83"/></symbol>
  <symbol id="i-star" viewBox="0 0 22 22"><path d="M11 2.29l2.66 5.5 6.05.83-4.4 4.21 1.1 5.96L11 15.95l-5.41 2.84 1.1-5.96-4.4-4.21 6.05-.83L11 2.29z"/></symbol>
  <symbol id="i-spark" viewBox="0 0 20 20"><path d="M8.33 2.5l1.43 4.24 4.24 1.43-4.24 1.43-1.43 4.23-1.43-4.23-4.23-1.43 4.23-1.43zM15 12.5l.71 2.12 2.12.71-2.12.71L15 18.17l-.71-2.13-2.12-.71 2.12-.71z"/></symbol>
  <symbol id="i-award" viewBox="0 0 20 20"><circle cx="10" cy="7.5" r="5"/><path d="M7.08 11.58 5.83 17.5 10 15.42l4.17 2.08-1.25-5.92"/></symbol>
  <symbol id="i-landmark" viewBox="0 0 20 20"><path d="M2.5 7.5 10 3.33l7.5 4.17M3.75 7.5h12.5M5 7.5v6.67M8.33 7.5v6.67M11.67 7.5v6.67M15 7.5v6.67M3.33 14.17h13.34M2.5 16.67h15"/></symbol>
  <symbol id="i-help" viewBox="0 0 20 20"><circle cx="10" cy="10" r="7.5"/><path d="M7.92 7.92a2.08 2.08 0 1 1 2.92 1.9c-.5.23-.84.72-.84 1.27v.66M10 13.75v.01"/></symbol>
</svg>"""


def multi_times(start):
    """Filler for the multiple-times variant: the excursion's real start plus two later departures,
    one of each availability state. Replace with API data."""
    h, m, ap = re.match(r"(\d+):(\d+) (AM|PM)", start).groups()
    base = (int(h) % 12 + (12 if ap == "PM" else 0)) * 60 + int(m)
    def fmt(t):
        hh, mm = divmod(t, 60)
        return f"{hh % 12 or 12}:{mm:02d} {'AM' if hh < 12 else 'PM'}"
    return [{"id": "t0", "time": start, "status": "available"},
            {"id": "t1", "time": fmt(base + 120), "status": "limited"},
            {"id": "t2", "time": fmt(base + 240), "status": "soldout"}]


def build(x):
    arrive, aboard = SHIP_TIMES_FILLER["arrive"], SHIP_TIMES_FILLER["aboard"]
    title = T(x["title"])
    # Experience-type badges (HISTORY Channel Exclusive, Accessible Travel Solutions Exclusive, Heritage Tour)
    badge_default = x["badges"][0] if x["badges"] else "none"
    if True:
        def mark(b):
            if b.get("img"):
                return f'<img class="xp-mark" src="assets/{b["img"]}" alt="" width="20" height="18">'
            return f'<svg class="i" aria-hidden="true"><use href="#{b["icon"]}"/></svg>'
        chips = "".join(f'<span class="xp-badge xp-{k}" data-badge="{k}"{"" if k in x["badges"] else " hidden"}>{mark(b)}<span>{T(b["label"])}</span></span>'
                        for k, b in BADGES.items())
        badge = f'<p class="xp-badges" id="xpBadges"{"" if x["badges"] else " hidden"}>{chips}</p>\n          '

    # Fact tiles: only tiles with template content open a drawer
    def tile(label, icon, value, drawer=None):
        if drawer:
            return f'''      <button class="fact glass" role="listitem" data-drawer="{drawer}" aria-haspopup="dialog">
        <span class="fact-label"><svg class="i"><use href="#{icon}"/></svg><span>{label}</span></span>
        <span class="fact-value"><b>{value}</b><svg class="i"><use href="#i-right"/></svg></span>
      </button>'''
        return f'''      <div class="fact glass" role="listitem">
        <span class="fact-label"><svg class="i"><use href="#{icon}"/></svg><span>{label}</span></span>
        <span class="fact-value"><b>{value}</b></span>
      </div>'''
    tiles = "\n".join([
        tile("Duration", "i-clock", T(x["duration"]), "duration"),
        tile("Activity", "i-pulse", T(x["activity"]), "activity"),
        tile("Wheelchair", "i-access", "Accessible", "access") if x["wheelchair"] else tile("Wheelchair", "i-access", "Not accessible"),
        tile("Meals", "i-meals", T(x["meals"] or "Not provided")),
    ])

    notice = ""
    if x["notice"]:
        first, rest = x["notice"].split(". ", 1)
        notice = f'''  <div class="notice" role="note">
    <svg class="i"><use href="#i-access"/></svg>
    <p><b>{T(first)}.</b> {T(rest)}</p>
  </div>
'''
    top3 = "\n".join(f'        <li class="highlight"><span class="num" aria-hidden="true">{i}</span><h3>{T(t)}</h3></li>'
                     for i, t in enumerate(x["top3"], 1))
    about = "\n        ".join(f"<p>{H(p)}</p>" for p in x["about_html"])
    notes = "\n          ".join(f"<p>{H(p)}</p>" for p in x["notes_html"])
    cancel = "\n          ".join(f"<p>{H(p)}</p>" for p in CANCELLATION_HTML)

    rates = ""
    if x["child"]:
        rates = f'''
    <div class="rates">
      <div class="rate"><span>Adult</span><b>{x["adult"]}</b></div>
      <div class="rate"><span>Child (12 and under)</span><b>{x["child"]}</b></div>
    </div>'''
    child_row = (f'\n    <div class="d-row"><div class="top"><b>Child (12 and under)</b><span><strong style="color:var(--n90)">{x["child"]}</strong> per child</span></div></div>'
                 if x["child"] else "")

    levels = "\n".join(
        (f'    <div class="level current"><b>{n} activity</b> <small>· This excursion</small><p>{T(d)}</p></div>'
         if n == x["activity"] else f'    <div class="level"><b>{n} activity</b><p>{T(d)}</p></div>')
        for n, d in ACTIVITY_LEVELS)

    access_tpl = ""
    if x["wheelchair"]:
        access_tpl = f'''
<template id="t-access" data-label="Accessibility">
  <h2>Wheelchair accessible</h2>
  <p>{T(x["wheelchair"])}</p>
</template>
'''

    def faq_body(a):
        if isinstance(a, dict):
            return '<ul class="bullets">' + "".join(f"<li>{H(i)}</li>" for i in a["list"]) + "</ul>"
        return "".join(f"<p>{H(p)}</p>" for p in a)
    faq = "\n".join(f'''    <div class="acc">
      <button class="acc-head" aria-expanded="false"><span class="titles"><strong>{T(q)}</strong></span><svg class="i chev"><use href="#i-down"/></svg></button>
      <div class="collapse"><div><div class="acc-body">{faq_body(a)}</div></div></div>
    </div>''' for q, a in FAQ)

    def radio(name, value, label, default):
        c = " checked" if value == default else ""
        return f'<label><input type="radio" name="{name}" value="{value}"{c}> {label}</label>'
    avail_default = x["status"] or "available"

    photo_css = (f'/* ───────────── This page’s photo (the only page-specific styling) ───────────── */\n'
                 f'/* {x["photo"]}: 2000×711 banner */\n.photo img{{ object-position:{x["focal"]} }}')

    credit_value_fs = (
        '\n      <fieldset><legend>Credit value</legend>\n        ' +
        "\n        ".join(radio("creditValue", v, "$" + v, "100") for v in ("100", "200", "300")) +
        '\n        <p>One credit is used per guest — shown whenever there is more than one.</p>')
    page_data = {
        "avail": avail_default, "spots": x.get("spots") or 1, "start": x["start"], "dateShort": x["date_short"],
        "portShort": x["port_short"], "arrive": arrive, "aboard": aboard,
        "times": multi_times(x["start"]), "badge": badge_default, "creditsV2": True,
    }
    import json

    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="theme-color" content="#022658">
<title>{title} · Shore Excursion</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Gelasio:wght@400;500&family=Poppins:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>
{CSS}

{photo_css}
</style>
</head>
<body>

<!-- Icon sprite -->
{ICONS}

<!-- Compact header (slides in once the hero card scrolls away) -->
<div class="compact" id="compact" aria-hidden="true">
  <div class="wrap">
    <button class="compact-back" data-handoff="back" aria-label="Back" tabindex="-1"><svg class="i"><use href="#i-back"/></svg></button>
    <button class="compact-text" id="compactTitle" aria-expanded="false" tabindex="-1">
      <span class="compact-eyebrow">{T(x["port_short"])} · <b>Starts {x["start"]}</b></span>
      <span class="compact-title">{title}</span>
    </button>
  </div>
</div>

<header class="hero" id="hero">
  <div class="hero-bg" aria-hidden="true">
    <div class="wash" id="wash"><img src="assets/{x["photo"]}" alt=""></div>
    <div class="photo" id="photo"><img src="assets/{x["photo"]}" alt=""><div class="photo-dim"></div></div>
    <div class="top-shade"></div>
    <div class="ramp"></div>
  </div>

  <div class="topbar"><div class="wrap">
    <button class="round-btn" data-handoff="back" aria-label="Back"><svg class="i"><use href="#i-back"/></svg></button>
    </div></div>

  <div class="hero-stack wrap">
    <div class="card-wrap" id="cardWrap">
      <div class="status-pill" id="statusPill" role="status"><span class="dot"></span><span id="statusText"></span></div>
      <article class="glass hero-card" id="heroCard">
        <div class="on-photo">
          {badge}<h1 class="hero-title">{title}</h1>
          <p class="hero-meta"><span class="meta-port" title="{T(x["port"])}">{T(x["port"])}</span><span>Day {x["day"]} · {x["date"]}</span></p>
        </div>

        <div class="key-row on-photo">
          <div class="key">
            <p class="key-label"><svg class="i"><use href="#i-clock"/></svg><span id="startLabel">Start time</span></p>
            <div id="startValue"><div class="key-value">{x["start"]}</div></div>
          </div>
          <div class="key">
            <p class="key-label">Per adult</p>
            <div class="key-price"><div class="key-value">{x["adult"]}</div><a class="card-link" href="#price">View all pricing</a></div>
          </div>
        </div>
      </article>
    </div>

    <div class="facts" role="list">
{tiles}
    </div>
  </div>
</header>

<main class="wrap">
{notice}  <section class="block" id="overview" aria-labelledby="overviewTitle">
    <p class="eyebrow">Overview</p>
    <h2 class="section-title" id="overviewTitle">Top 3 reasons to book</h2>
    <div class="section-body">
      <ol class="highlights">
{top3}
      </ol>
      <button class="btn-outline" id="readMore" aria-expanded="false" aria-controls="desc"><span>Read the full description</span><svg class="i"><use href="#i-down"/></svg></button>
      <div class="collapse" id="desc"><div><div class="description">
        {about}
      </div></div></div>
    </div>
  </section>

  <section class="block" id="times" aria-labelledby="timesTitle" hidden>
    <p class="eyebrow">Start times</p>
    <h2 class="section-title" id="timesTitle">Choose a time on {x["date_short"]}</h2>
    <div class="time-chips" role="radiogroup" aria-labelledby="timesTitle" id="timeChips"></div>
  </section>

  <section class="block" id="price" aria-labelledby="priceEyebrow">
    <p class="eyebrow" id="priceEyebrow">Price</p>
    <div class="price-heading"><span class="amt">{x["adult"]}</span><span class="unit">per adult</span></div>{rates}
    <!-- Excursion credits: CONFIRM WITH PRODUCT what credit data and copy can be shown -->
    <div class="credit-card" id="creditCard">
      <button class="credit-head" aria-expanded="false" aria-controls="creditRules"><svg class="i star" aria-hidden="true"><use href="#i-star"/></svg><span class="credit-text"><span id="creditTitle">You have <b>2 excursion credits of $100</b></span><span class="credit-sub" data-credit-sub hidden>One credit is used per guest</span></span><svg class="i chev" aria-hidden="true"><use href="#i-down"/></svg></button>
      <div class="collapse" id="creditRules"><div><div class="credit-rules">
        <!-- FPO: credit rules copy taken from Figma "Dining credit" (14953:27539). Not on the live pages — needs product confirmation. -->
        <p class="credit-rules-title">Using your excursion credit</p>
        <ul><li>Your credit covers up to the dollar amount listed.</li><li>Credits expire at the end of the voyage.</li></ul>
      </div></div></div>
    </div>
  </section>

  <section class="block" id="know" aria-labelledby="knowEyebrow">
    <p class="eyebrow" id="knowEyebrow">Know before you go</p>
    <div class="accordion" id="accordion">
      <div class="acc">
        <button class="acc-head" aria-expanded="false">
          <span class="titles"><strong>Cancellation</strong></span>
          <svg class="i chev"><use href="#i-down"/></svg>
        </button>
        <div class="collapse"><div><div class="acc-body">
          {cancel}
        </div></div></div>
      </div>
      <div class="acc">
        <div class="acc-head static">
          <span class="titles"><strong>Language</strong></span>
          <span class="acc-value">{T(x["language"])}</span>
        </div>
      </div>
      <div class="acc">
        <button class="acc-head" aria-expanded="false">
          <span class="titles"><strong>Notes</strong><small id="notesSummary"></small></span>
          <svg class="i chev"><use href="#i-down"/></svg>
        </button>
        <div class="collapse"><div><div class="acc-body" id="notesBody">
          {notes}
        </div></div></div>
      </div>
    </div>
    <button class="faq-row" data-drawer="faq" aria-haspopup="dialog">
      <svg class="i"><use href="#i-help"/></svg>
      <span class="txt">Shore Excursions FAQs</span>
      <svg class="i go"><use href="#i-right"/></svg>
    </button>
  </section>
</main>

<footer class="wrap proto-foot">
  <details class="proto" id="proto">
    <summary>Prototype states <small>Review tool only</small><svg class="i"><use href="#i-down"/></svg></summary>
    <form class="proto-panel" id="protoPanel">
      <fieldset><legend>Start times</legend>
        {radio("times", "single", "One start time", "single")}
        {radio("times", "multi", "Multiple times · none picked", "single")}
        {radio("times", "multi-picked", "Multiple times · first picked", "single")}
        <p>Extra times are filler until the API provides them. With multiple times, each time has its own availability.</p>
      </fieldset>
      <fieldset><legend>Experience badge</legend>
        {radio("badge", "none", "None", badge_default)}
        {"".join(radio("badge", k, T(b["label"]), badge_default) for k, b in BADGES.items())}
      </fieldset>
      <fieldset><legend>Availability</legend>
        {radio("avail", "available", "Available", avail_default)}
        {radio("avail", "limited", "Limited Capacity", avail_default)}
        {radio("avail", "spots", f"{x.get('spots') or 1} {'Spot' if (x.get('spots') or 1) == 1 else 'Spots'} Left", avail_default)}
        {radio("avail", "soldout", "Sold Out", avail_default)}
      </fieldset>
      <fieldset><legend>Credits</legend>
        {radio("credits", "2", "2 credits of $100", "2")}
        {radio("credits", "1", "1 credit of $100", "2")}
        {radio("credits", "0", "No credits", "2")}
        {radio("credits", "banner", "Credit introduction banner", "2")}
        <p>Confirm with product what credit data can be shown.</p>
      </fieldset>{credit_value_fs}
      </fieldset>
      <fieldset><legend>Ship times</legend>
        {radio("ship", "both", "Arrive + all aboard", "both")}
        {radio("ship", "arrive", "Arrive only", "both")}
        <p>Filler times ({arrive} / {aboard}) until the API provides them.</p>
      </fieldset>
      <button type="button" class="proto-reset" id="protoReset">Reset all states</button>
    </form>
  </details>
</footer>

<!-- Floating booking bar -->
<div class="bar-zone" id="barZone">
  <div class="credit-banner hidden" id="creditBanner" role="status">
    <strong id="bannerTitle">2 excursion credits of $100 available</strong>
    <span class="banner-sub" data-credit-sub hidden>One credit is used per guest</span>
    <button aria-label="Dismiss" id="bannerClose"><svg class="i"><use href="#i-close"/></svg></button>
  </div>
  <div class="bar">
    <button class="bar-price" id="barPrice" data-drawer="pricing" aria-haspopup="dialog" aria-expanded="false" aria-label="Show price details">
      <span class="bar-line1"><b>{x["adult"]}</b><span class="u">/ adult</span><svg class="i"><use href="#i-up"/></svg></span>
      <span class="bar-line2" id="barLine2">{x["date_short"]} · {x["start"]}</span>
    </button>
    <button class="btn-primary" id="cta">Reserve</button>
  </div>
</div>

<!-- Drawer / modal shell -->
<div class="layer" id="layer" aria-hidden="true">
  <div class="scrim" data-close></div>
  <div class="sheet" role="dialog" aria-modal="true" aria-labelledby="sheetLabel" id="sheet" tabindex="-1">
    <span class="grabber" aria-hidden="true"></span>
    <div class="sheet-head" id="sheetHead">
      <button class="close" data-close aria-label="Close"><svg class="i"><use href="#i-close"/></svg></button>
      <span class="sheet-label" id="sheetLabel"></span>
    </div>
    <div class="sheet-body" id="sheetBody"></div>
  </div>
</div>

<!-- Drawer content -->
<template id="t-duration" data-label="Duration">
  <h2>{T(x["duration"])}</h2>
  <div class="d-rows">
    <div class="d-row"><div class="top"><b class="ico"><svg class="i"><use href="#i-clock"/></svg><span data-slot="start-label">Start time</span></b><span data-slot="start">{x["start"]}</span></div></div>
    <div class="d-row"><div class="top"><b class="ico"><svg class="i"><use href="#i-anchor"/></svg>Ship arrives</b><span>{arrive}</span></div></div>
    <div class="d-row" data-slot="aboard-row"><div class="top"><b class="ico"><svg class="i"><use href="#i-ship"/></svg>All aboard</b><span>{aboard}</span></div></div>
  </div>
</template>

<template id="t-activity" data-label="Activity level">
  <h2>{T(x["activity"])}</h2>
  <div class="levels">
{levels}
  </div>
</template>
{access_tpl}
<template id="t-pricing" data-label="Price details">
  <h2>{x["adult"]} per adult</h2>
  <div class="d-rows">
    <div class="d-row"><div class="top"><b>Adult</b><span><strong style="color:var(--n90)">{x["adult"]}</strong> per adult</span></div></div>{child_row}
  </div>
  <div data-slot="credits">
    <p class="d-sub">Excursion credits</p>
    <div class="credit-card">
      <button class="credit-head" aria-expanded="false" aria-controls="sheetCreditRules"><svg class="i star" aria-hidden="true"><use href="#i-star"/></svg><span class="credit-text"><span data-slot="credit-title">You have <b>2 excursion credits of $100</b></span><span class="credit-sub" data-credit-sub hidden>One credit is used per guest</span></span><svg class="i chev" aria-hidden="true"><use href="#i-down"/></svg></button>
      <div class="collapse" id="sheetCreditRules"><div><div class="credit-rules">
        <!-- FPO: credit rules copy taken from Figma "Dining credit" (14953:27539). Not on the live pages — needs product confirmation. -->
        <p class="credit-rules-title">Using your excursion credit</p>
        <ul><li>Your credit covers up to the dollar amount listed.</li><li>Credits expire at the end of the voyage.</li></ul>
      </div></div></div>
    </div>
  </div>
  <p class="d-sub">Details</p>
  <div class="d-rows">
    <div class="d-row"><div class="top"><b>Date</b><span>{x["date"]}</span></div></div>
    <div class="d-row"><div class="top"><b data-slot="start-label">Start time</b><span data-slot="start">{x["start"]}</span></div></div>
    <div class="d-row"><div class="top"><b>Duration</b><span>{T(x["duration"])}</span></div></div>
    <div class="d-row"><div class="top"><b>Port</b><span>{T(x["port"])}</span></div></div>
  </div>
  <button class="btn-primary sheet-cta" data-slot="cta">Reserve</button>
</template>

<template id="t-times" data-label="Start times">
  <h2>Choose a time on {x["date_short"]}</h2>
  <div class="levels" role="radiogroup" aria-label="Start time" data-slot="options"></div>
</template>

<template id="t-faq" data-label="Shore Excursions FAQs" data-full>
  <div class="accordion">
{faq}
  </div>
</template>

<div class="toast" id="toast" role="status" aria-live="polite"></div>

<script id="pageData" type="application/json">{json.dumps(page_data)}</script>
<script>
{JS}
</script>
</body>
</html>
'''


JS = open(os.path.join(HERE, "page.js"), encoding="utf-8").read().rstrip()

if __name__ == "__main__":
    for x in EXCURSIONS:
        path = os.path.join(OUT, x["file"])
        with open(path, "w", encoding="utf-8") as f:
            f.write(build(x))
        print("wrote", x["file"])
