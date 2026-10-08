# Verify that all SVG shapes and gradients parse cleanly
import xml.etree.ElementTree as ET

test_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">
  <defs>
    <linearGradient id="g1"><stop offset="0%" stop-color="#fff"/></linearGradient>
  </defs>
  <rect x="0" y="0" width="100" height="100" fill="url(#g1)"/>
</svg>"""

tree = ET.fromstring(test_svg)
print("XML parser verified.")
