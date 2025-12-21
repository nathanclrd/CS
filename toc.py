import os
import re

root_dir = "/Users/nthclrd/Documents/Obsidian/Vault/CS"

def generate_toc(content):
    headers = []
    lines = content.split('\n')
    for line in lines:
        # Match headers
        match = re.match(r'^(#{2,3})\s+(.+)', line)
        if match:
            level = len(match.group(1))
            title = match.group(2).strip()
            headers.append((level, title))
    
    if not headers:
        return None

    toc_lines = ["| Topic |", "| :--- |"]
    for level, title in headers:
        indent = "&nbsp;&nbsp;&nbsp;&nbsp;" * (level - 2) if level > 2 else ""
        # Use [[#Header]] format. This avoids using the pipe character | which breaks the table.
        # Obsidian renders [[#Header]] as "Header" (without the #) in the preview/link.
        # We must escape | in the title if it exists, but usually headers don't have pipes.
        # If they do, we might have issues, but let's assume they don't for now.
        safe_title = title.replace("|", "") # Remove pipes from title to be safe for the link text if any
        
        toc_lines.append(f"| {indent}[[{'#' + safe_title}]] |")
    
    return "\n".join(toc_lines)

def process_file(file_path):
    with open(file_path, 'r') as f:
        content = f.read()

    lines = content.split('\n')
    new_lines = []
    
    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()
        
        # Check if this is the start of a TOC table
        # It must start with | and contain "Topic" in the first row
        if stripped.startswith("|") and "Topic" in stripped:
            # This is a TOC table start. Skip this line and subsequent table lines.
            i += 1
            while i < len(lines) and lines[i].strip().startswith("|"):
                i += 1
            continue
        
        new_lines.append(line)
        i += 1
    
    cleaned_content = "\n".join(new_lines).strip()
    
    # Generate new TOC
    toc = generate_toc(cleaned_content)
    
    if toc:
        final_content = toc + "\n\n" + cleaned_content
        
        with open(file_path, 'w') as f:
            f.write(final_content)
        print(f"Updated {file_path}")

for root, dirs, files in os.walk(root_dir):
    if ".obsidian" in dirs:
        dirs.remove(".obsidian")
    
    for file in files:
        if file.endswith(".md"):
            process_file(os.path.join(root, file))
