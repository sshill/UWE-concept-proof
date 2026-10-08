with open('/home/hills/Documents/UWS/generate_uov_infographic.py', 'r') as f:
    text = f.read()

# Replace any comment dashes that have multiple hyphens
import re
text = re.sub(r'<!--\s*-+.*?-->', lambda m: m.group(0).replace('-', '=').replace('<==', '<!--').replace('==>', '-->'), text)

with open('/home/hills/Documents/UWS/generate_uov_infographic.py', 'w') as f:
    f.write(text)

print("Updated script.")
