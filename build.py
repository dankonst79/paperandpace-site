"""Generate the static GitHub Pages site from products.json."""
from __future__ import annotations

import html
import json
from pathlib import Path

ROOT = Path(__file__).parent
PRODUCTS = json.loads((ROOT / "products.json").read_text(encoding="utf-8"))
UPDATED = "22 November 2026"
NAV = [("index.html", "Home"), ("about.html", "About"), ("contact.html", "Contact")]
FOOTER = [("terms.html", "Terms"), ("refund.html", "Refund policy"), ("privacy.html", "Privacy")]


def page(filename: str, title: str, description: str, body: str) -> None:
    nav = "".join(f'<a href="{path}"{(" aria-current=page" if path == filename else "")}>{label}</a>' for path, label in NAV)
    links = "".join(f'<a href="{path}">{label}</a>' for path, label in [*NAV, *FOOTER])
    document = f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="{html.escape(description, quote=True)}">
  <meta name="theme-color" content="#24343A">
  <title>{html.escape(title)} | Paper &amp; Pace</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <header class="site-header"><div class="shell header-inner"><a class="brand" href="index.html">Paper &amp; Pace</a><nav class="main-nav" aria-label="Main navigation">{nav}</nav></div></header>
  <main id="main">{body}</main>
  <footer class="site-footer"><div class="shell footer-inner"><div><a class="brand" href="index.html">Paper &amp; Pace</a><p>Printable tools for planning at your own pace.<br>Operated by ARIADNA PLUS d.o.o., Ljubljana, Slovenia.</p><p>© 2026 Paper &amp; Pace</p></div><nav class="footer-links" aria-label="Footer navigation">{links}</nav></div></footer>
</body>
</html>
'''
    (ROOT / filename).write_text(document, encoding="utf-8")


def product_card(product: dict) -> str:
    title = html.escape(product["title"])
    summary = html.escape(product["summary"])
    detail = html.escape(product["detail"])
    cover = html.escape(product["cover"], quote=True)
    url = product["checkout_url"]
    action = (f'<a class="button" href="{html.escape(url, quote=True)}" rel="noopener noreferrer">View product</a>'
              if url else '<span class="coming-soon">Coming soon</span>')
    return f'''<article class="product-card"><img src="{cover}" alt="Cover of {title}" loading="lazy"><div class="product-body"><h3>{title}</h3><p>{summary}</p><p class="product-meta">{detail}</p><div class="product-action">{action}</div></div></article>'''


hero = '''<section class="shell hero"><div><p class="eyebrow">Print it. Make it yours.</p><h1>A little more clarity, one page at a time.</h1><p class="lede">Paper &amp; Pace makes printable planners and trackers for the everyday work of setting goals, building habits and looking after your money.</p><a class="button" href="#products">Explore the collection</a></div><div class="hero-art"><img src="assets/covers/budget-planner-2027.png" alt="Preview of the 2027 Budget Planner printable cover"><span>Made for real life</span></div></section>'''
cards = "".join(product_card(product) for product in PRODUCTS)
home = f'''{hero}<section class="shell section" id="products"><div class="section-head"><div><p class="eyebrow">The collection</p><h2>Tools you'll actually use</h2></div><p>Download, print and start where you are. Each design gives you space to think and write, without an app to keep up with.</p></div><div class="product-grid">{cards}</div></section><section class="feature-band"><div class="shell feature-grid"><div><h3>Ready to print</h3><p>Our printable products come in US Letter and A4 sizes for home printing.</p></div><div><h3>Room to make it yours</h3><p>Write by hand, choose your own pace and reprint reusable pages when you need a fresh start.</p></div><div><h3>Simple downloads</h3><p>Checkout and file delivery are handled by Polar. Your files are available after purchase.</p></div></div></section>'''
page("index.html", "Printable planners and trackers", "Thoughtful printable planners and trackers for money, goals and habits.", home)

page("about.html", "About", "Meet Paper & Pace, printable tools operated by ARIADNA PLUS d.o.o. in Ljubljana, Slovenia.", f'''<div class="shell prose"><p class="eyebrow">About us</p><h1>Paper plans for real life.</h1><p class="lede">Paper &amp; Pace creates printable planners and trackers designed to make everyday decisions feel more manageable.</p><h2>What we make</h2><p>Our collection focuses on practical pages for budgeting, goals and habits. You can print the pages you need and work through them at a pace that suits you.</p><h2>Who operates Paper &amp; Pace</h2><p>Paper &amp; Pace is operated by <strong>ARIADNA PLUS d.o.o.</strong> in Ljubljana, Slovenia.</p><div class="card-note"><strong>Questions?</strong><br>Write to <a href="mailto:paperandpacesupport@gmail.com">paperandpacesupport@gmail.com</a>. We can help with products, downloads and support requests.</div></div>''')

page("contact.html", "Contact", "Contact Paper & Pace for product and download support.", '''<div class="shell prose"><p class="eyebrow">Get in touch</p><h1>We're here to help.</h1><p class="lede">Have a question about a planner, your download or a purchase? Send us an email and include your order reference if you have one.</p><div class="card-note"><p><strong>Email</strong><br><a href="mailto:paperandpacesupport@gmail.com">paperandpacesupport@gmail.com</a></p><p><strong>Business</strong><br>ARIADNA PLUS d.o.o.<br>Ljubljana, Slovenia</p></div><p>For payment, tax or receipt questions, your Polar order email also links to purchase support.</p></div>''')

page("terms.html", "Terms", "Terms for Paper & Pace digital printable products.", f'''<div class="shell prose"><p class="eyebrow">Policies · Updated {UPDATED}</p><h1>Terms</h1><p>These terms describe the printable digital products offered by Paper &amp; Pace, operated by ARIADNA PLUS d.o.o., Ljubljana, Slovenia. Please read the product description and format details before ordering.</p><h2>Digital products</h2><p>Products are delivered as downloadable files. No physical item is shipped. PDF pages are intended for printing at actual size. Some products may also include a spreadsheet; the product page describes what is included.</p><h2>Personal-use license</h2><p>Unless a product says otherwise, your purchase is for your own personal use. You may print copies for yourself. Please do not redistribute, resell, upload or share the digital files. The included <code>license.txt</code> confirms the license for each product.</p><h2>Checkout and delivery</h2><p>Checkout, payment and file delivery are handled by Polar as merchant of record. Your purchase is also subject to <a href="https://polar.sh/legal/checkout-buyer-terms" rel="noopener noreferrer">Polar's buyer terms</a>. The price, currency and any applicable taxes are shown at checkout before you pay.</p><h2>Support and rights</h2><p>If a file is missing or does not work as described, email <a href="mailto:paperandpacesupport@gmail.com">paperandpacesupport@gmail.com</a> with your order reference. Nothing in these terms limits rights that cannot be excluded under applicable consumer law. See our <a href="refund.html">refund policy</a> for requests about a purchase.</p></div>''')

page("refund.html", "Refund policy", "Refund and support policy for Paper & Pace digital downloads.", f'''<div class="shell prose"><p class="eyebrow">Policies · Updated {UPDATED}</p><h1>Refund policy</h1><p>We want the files you buy to match the description and work as intended. If a download is missing, damaged or materially different from its description, email <a href="mailto:paperandpacesupport@gmail.com">paperandpacesupport@gmail.com</a> with your order reference and a short explanation. We will help resolve the issue or review a refund request.</p><h2>Digital downloads</h2><p>Digital files can be delivered immediately after checkout. Refund and withdrawal rights depend on the circumstances and applicable law. In the EU, starting a digital download can affect the statutory withdrawal right only when the legal conditions for consent, acknowledgement and confirmation are met. We do not treat every download as automatically non-refundable.</p><h2>How refunds are handled</h2><p>Polar acts as merchant of record for the purchase and processes payments and refunds under its <a href="https://polar.sh/legal/checkout-buyer-terms" rel="noopener noreferrer">buyer terms</a>. You can contact us first at <a href="mailto:paperandpacesupport@gmail.com">paperandpacesupport@gmail.com</a>, or use the support route in your Polar receipt. This policy does not limit non-waivable consumer rights.</p></div>''')

page("privacy.html", "Privacy", "How Paper & Pace handles contact and purchase information.", f'''<div class="shell prose"><p class="eyebrow">Policies · Updated {UPDATED}</p><h1>Privacy</h1><p>Paper &amp; Pace is operated by ARIADNA PLUS d.o.o., Ljubljana, Slovenia. For privacy questions or requests, email <a href="mailto:paperandpacesupport@gmail.com">paperandpacesupport@gmail.com</a>.</p><h2>Information we use</h2><p>This site has no account, contact form or first-party analytics. If you email us, we receive your email address and the information you send. If you buy a product, Polar handles checkout and may provide us with order and customer details needed to deliver the product and support your purchase. We do not collect payment card details on this site.</p><h2>Why we use it</h2><p>We use support correspondence and relevant order details to answer questions, deliver and support products, and meet applicable business obligations. We keep information only as long as needed for those purposes or required by law.</p><h2>Other services</h2><p>Polar operates checkout and delivery under its own <a href="https://polar.sh/legal/privacy-policy" rel="noopener noreferrer">privacy notice</a>. This site is hosted on GitHub Pages; GitHub may process technical data needed to serve the website under its <a href="https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement" rel="noopener noreferrer">privacy statement</a>.</p><h2>Your choices</h2><p>You may ask us about information we hold, request access or correction, or ask for deletion where applicable. You may also object to certain processing or raise a concern with your data protection authority. Email us at <a href="mailto:paperandpacesupport@gmail.com">paperandpacesupport@gmail.com</a> and we will respond under applicable law.</p></div>''')

(ROOT / ".nojekyll").write_text("", encoding="utf-8")
print("Built 6 pages")

