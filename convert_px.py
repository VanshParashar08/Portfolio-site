import re

with open('/Users/vanshparashar/Documents/Portfolio Website/index.html', 'r') as f:
    content = f.read()

def px_to_rem(match):
    val = float(match.group(1))
    # Don't convert 1px, 2px, 3px (usually borders/small shadows)
    if val <= 3:
        return match.group(0)
    rem_val = val / 16.0
    # format to 2 decimal places max
    rem_str = f"{rem_val:.3f}".rstrip('0').rstrip('.')
    return f"{rem_str}rem"

# Only replace inside <style> tags
style_start = content.find('<style>')
style_end = content.find('</style>')

if style_start != -1 and style_end != -1:
    style_content = content[style_start:style_end]
    # Replace anything that looks like 140px, but avoid things inside calc() if possible, or just replace all \d+px
    new_style = re.sub(r'(\d+(?:\.\d+)?)px', px_to_rem, style_content)
    
    # Add html font-size scaling
    new_style = new_style.replace('html { scroll-behavior: smooth; }', 'html { scroll-behavior: smooth; font-size: clamp(14px, 1vw, 36px); }')
    
    new_content = content[:style_start] + new_style + content[style_end:]
    
    with open('/Users/vanshparashar/Documents/Portfolio Website/index.html', 'w') as f:
        f.write(new_content)
    print("Successfully converted px to rem and added root scaling.")
else:
    print("Could not find style tags.")
