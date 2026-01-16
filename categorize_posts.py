#!/usr/bin/env python3
"""
Script to help categorize blog posts based on their filenames and existing tags.
Run this script to automatically add category field to posts.
"""

import os
import re
from pathlib import Path

# Define category keywords to help auto-categorize
CATEGORY_KEYWORDS = {
    'machine_learning': [
        'logistic', 'regression', 'neural', 'nlp', 'language-processing',
        'recommendation', 'smart-reply', 'deeplearning', 'elmo', 'naive-bayes',
        'crf', 'hlai', 'mlprague', 'ernie', 'gamification', 'coursera'
    ],
    'travel': [
        'barcelona', 'taiwan', 'kuala', 'lumpur', 'bali', 'okinawa', 'melaka',
        'hong-kong', 'macao', 'tokio', 'italy', 'malta', 'england', 'krakov',
        'seattle', 'tabor'
    ],
    'books': [
        'homo-deus', 'solve-for-happy', 'factfulness', 'books', 'entrepreneur',
        'vedec-a-media', 'blinklist'
    ],
    'software_engineering': [
        'python', 'defaultdict', 'webexpo', 'computex', 'meetup', 'aog',
        'ideas-to-think'
    ]
}

def guess_category_from_filename(filename):
    """Guess category based on filename."""
    filename_lower = filename.lower()
    
    for category, keywords in CATEGORY_KEYWORDS.items():
        for keyword in keywords:
            if keyword in filename_lower:
                return category
    
    return None

def has_tag_machine_learning(content):
    """Check if post has 'tag: machine learning'."""
    return 'tag: machine learning' in content

def get_existing_category(content):
    """Extract existing category if present."""
    match = re.search(r'^category:\s*(.+)$', content, re.MULTILINE)
    return match.group(1).strip() if match else None

def update_post_category(filepath):
    """Update a single post with category field."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if already has category
    existing_category = get_existing_category(content)
    if existing_category:
        print(f"✓ {filepath.name} already has category: {existing_category}")
        return False
    
    # Determine category
    category = None
    
    # First, try to get category from parent directory
    parent_dir = filepath.parent.name
    if parent_dir in ['machine_learning', 'software_engineering', 'travel', 'books']:
        category = parent_dir
    # Then check for old tag
    elif has_tag_machine_learning(content):
        category = 'machine_learning'
    else:
        # Guess from filename
        category = guess_category_from_filename(filepath.stem)
    
    if not category:
        print(f"? {filepath.name} - Could not determine category")
        return False
    
    # Replace 'tag: machine learning' with 'category: machine_learning'
    # or add category after layout/title
    if 'tag: machine learning' in content:
        new_content = content.replace('tag: machine learning', f'category: {category}')
    else:
        # Add category after the first '---' block
        parts = content.split('---', 2)
        if len(parts) >= 3:
            front_matter = parts[1]
            # Add category before the closing ---
            new_front_matter = front_matter.rstrip() + f'\ncategory: {category}\n'
            new_content = '---' + new_front_matter + '---' + parts[2]
        else:
            print(f"✗ {filepath.name} - Invalid front matter")
            return False
    
    # Write back
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"✓ {filepath.name} → {category}")
    return True

def main():
    """Main function to process all posts."""
    posts_dir = Path('_posts')
    
    if not posts_dir.exists():
        print("Error: _posts directory not found. Run this script from the repository root.")
        return
    
    updated = 0
    skipped = 0
    
    print("Processing blog posts...\n")
    
    # Process posts in subdirectories
    for category_dir in sorted(posts_dir.iterdir()):
        if category_dir.is_dir():
            print(f"\n{'='*60}")
            print(f"Processing {category_dir.name}/ category")
            print(f"{'='*60}")
            
            for post_file in sorted(category_dir.glob('*.md')):
                if update_post_category(post_file):
                    updated += 1
                else:
                    skipped += 1
    
    # Also process any remaining posts in root _posts directory
    for post_file in sorted(posts_dir.glob('*.md')):
        if update_post_category(post_file):
            updated += 1
        else:
            skipped += 1
    
    print(f"\n{'='*60}")
    print(f"Summary:")
    print(f"  Updated: {updated}")
    print(f"  Skipped: {skipped}")
    print(f"{'='*60}")
    print("\nNote: Please review the changes and manually categorize any")
    print("posts marked with '?' that couldn't be auto-categorized.")

if __name__ == '__main__':
    main()
