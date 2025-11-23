#!/usr/bin/env python3
# Auto-generated script to fix terminology inconsistencies

import os
import re

def fix_terminology(file_path, replacements):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content
    for old_term, new_term in replacements:
        # Case-insensitive replacement preserving original case
        pattern = r'\b' + re.escape(old_term) + r'\b'
        content = re.sub(pattern, new_term, content, flags=re.IGNORECASE)

    if content != original:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

# Terminology fixes
replacements = {
    'authentication': [
        ('auth', 'authentication'),
    ],
    'configuration': [
        ('config', 'configuration'),
    ],
    'application': [
        ('app', 'application'),
    ],
    'documentation': [
        ('docs', 'documentation'),
    ],

}

# Apply fixes
files_to_fix = [
    '/Users/chocho/projects/thevibecoders-revamped/PLAN.md',
    '/Users/chocho/projects/thevibecoders-revamped/PRD.md',
    '/Users/chocho/projects/thevibecoders-revamped/README.md',
    '/Users/chocho/projects/thevibecoders-revamped/design-system/README.md',
    '/Users/chocho/projects/thevibecoders-revamped/design-system/components.md',
    '/Users/chocho/projects/thevibecoders-revamped/design-system/implementation-guide.md',
    '/Users/chocho/projects/thevibecoders-revamped/design-system/patterns.md',
    '/Users/chocho/projects/thevibecoders-revamped/docs/madrs/001-tech-stack.md',

]

fixed_count = 0
for file_path in files_to_fix:
    all_replacements = []
    for term_group in replacements.values():
        all_replacements.extend(term_group)

    if fix_terminology(file_path, all_replacements):
        print(f"✓ Fixed: {file_path}")
        fixed_count += 1

print(f"\n✅ Fixed {fixed_count} files")
