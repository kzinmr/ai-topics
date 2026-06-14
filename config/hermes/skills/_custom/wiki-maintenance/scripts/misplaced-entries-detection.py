#!/usr/bin/env python3
"""Detect misplaced wiki entries — e.g. concept entries sitting between Events and Comparisons, 
or entity entries in the Concepts section. Run this before any section rebuild.

Usage: python3 references/misplaced-entries-detection.py
Run from ~/ai-topics/
"""

import re
import os

WIKI = "wiki"

def detect_misplaced():
    with open(os.path.join(WIKI, "index.md")) as f:
        content = f.read()

    # Find all section headers and their positions
    section_headers = []
    for m in re.finditer(r'^## (\w[^)]*?) \(', content, re.MULTILINE):
        section_headers.append((m.start(), m.group(1)))
    
    section_headers.sort()

    # For each chunk between section headers, check if the wikilink type matches the section
    misplaced = []
    for i, (pos, section_name) in enumerate(section_headers):
        next_pos = section_headers[i+1][0] if i+1 < len(section_headers) else len(content)
        body = content[pos:next_pos]
        
        for m in re.finditer(r'^- \[\[(\w+)/', body, re.MULTILINE):
            entry_type = m.group(1)
            # Normalize section name to a type
            section_type = section_name.lower().split()[0].rstrip('s')
            if entry_type != section_type and section_type in ('entitie', 'concept', 'event', 'comparison', 'querie', 'transcript'):
                misplaced.append({
                    'entry': m.group(0),
                    'found_in': section_name.strip(),
                    'actual_type': entry_type,
                    'line_pos': content[:m.start()].count('\n') + 1
                })
    
    return misplaced

def compute_section_boundaries(content):
    """Return dict of section_name -> (start_line, end_line_after_header, end_line_content)"""
    sections = {}
    lines = content.split('\n')
    current_section = None
    current_start = None
    header_start = None
    
    for i, line in enumerate(lines):
        m = re.match(r'^## (\w[^)]*?) ', line)
        if m:
            if current_section:
                sections[current_section] = {
                    'header_line': header_start,
                    'first_data_line': current_start,
                    'last_data_line': i - 1
                }
            current_section = m.group(1).strip()
            header_start = i
            current_start = i + 1
    
    if current_section:
        sections[current_section] = {
            'header_line': header_start,
            'first_data_line': current_start,
            'last_data_line': len(lines) - 1
        }
    
    return sections

if __name__ == '__main__':
    misplaced = detect_misplaced()
    print(f"Misplaced entries found: {len(misplaced)}")
    for m in misplaced[:30]:
        print(f"  Line {m['line_pos']}: '{m['entry'][:80]}' is '{m['actual_type']}' but found in '{m['found_in']}' section")
    if not misplaced:
        print("  ✅ No misplaced entries detected.")
