import os, re

BASE = "https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/"

def fix_links(filepath, base_url):
    with open(filepath, 'r') as f:
        content = f.read()
    
    # Vervang relatieve markdown links: [tekst](relatief/pad.md)
    def replace(match):
        text, href = match.group(1), match.group(2)
        if href.startswith('http') or href.startswith('#'):
            return match.group(0)  # al absoluut of anchor, skip
        abs_url = base_url + href
        return f'[{text}]({abs_url})'
    
    fixed = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', replace, content)
    
    with open(filepath, 'w') as f:
        f.write(fixed)

for root, dirs, files in os.walk('markdown'):
    for file in files:
        if file.endswith('.md'):
            path = os.path.join(root, file)
            # base_url voor dit bestand
            rel_dir = os.path.dirname(path).replace('\\', '/') + '/'
            fix_links(path, BASE + rel_dir)

# Fix ook root README
fix_links('README.md', BASE)