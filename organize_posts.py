#!/usr/bin/env python3
"""
Script to organize blog posts into category subdirectories.
This will move posts from _posts/ into _posts/category_name/ folders.
"""

import os
import re
import shutil
from pathlib import Path
from collections import defaultdict

# Define category keywords for auto-categorization
CATEGORY_KEYWORDS = {
    'machine_learning': [
        'logistic', 'regression', 'neural', 'nlp', 'language-processing',
        'recommendation', 'smart-reply', 'deeplearning', 'elmo', 'naive-bayes',
        'crf', 'hlai', 'mlprague', 'ernie', 'gamification', 'coursera', 'fewshot',
        'masters', 'meetup'
    ],
    'travel': [
        'barcelona', 'taiwan', 'kuala', 'lumpur', 'bali', 'okinawa', 'melaka',
        'hong-kong', 'macao', 'tokio', 'italy', 'malta', 'england', 'krakov',
        'seattle', 'tabor', 'riga', 'maroko', 'croatia', 'preparation'
    ],
    'books': [
        'books', 'homo-deus', 'solve-for-happy', 'factfulness', 'entrepreneur',
        'vedec-a-media', 'blinklist', 'solve', 'algoritmy'
    ],
    'software_engineering': [
        'python', 'defaultdict', 'webexpo', 'computex', 'aog',
        'ideas-to-think', 'algorithmy'
    ]
}

def get_category_from_file(filepath):
    """Extract category from file's front matter."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check for category field
        category_match = re.search(r'^category:\s*(.+)$', content, re.MULTILINE)
        if category_match:
            return category_match.group(1).strip()
        
        # Check for old tag field
        tag_match = re.search(r'^tag:\s*(.+)$', content, re.MULTILINE)
        if tag_match:
            tag = tag_match.group(1).strip()
            if tag == 'machine learning':
                return 'machine_learning'
            elif tag in ['books', 'notes']:
                return 'books'
            elif tag == 'travel':
                return 'travel'
        
        # Guess from filename
        filename_lower = filepath.stem.lower()
        for category, keywords in CATEGORY_KEYWORDS.items():
            for keyword in keywords:
                if keyword in filename_lower:
                    return category
        
        # Default to uncategorized
        return 'uncategorized'
    
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
        return 'uncategorized'

def organize_posts(posts_dir, dry_run=True):
    """Organize posts into category subdirectories."""
    posts_dir = Path(posts_dir)
    
    if not posts_dir.exists():
        print(f"Error: {posts_dir} does not exist!")
        return
    
    # Get all markdown files in _posts root (not in subdirectories)
    post_files = [f for f in posts_dir.glob('*.md') if f.is_file()]
    
    if not post_files:
        print("No posts found to organize.")
        return
    
    # Categorize posts
    categorized = defaultdict(list)
    for post_file in post_files:
        category = get_category_from_file(post_file)
        categorized[category].append(post_file)
    
    # Print summary
    print(f"\n{'='*70}")
    print(f"Found {len(post_files)} posts to organize")
    print(f"{'='*70}\n")
    
    for category, files in sorted(categorized.items()):
        print(f"{category}: {len(files)} posts")
    
    print(f"\n{'='*70}")
    
    if dry_run:
        print("\n🔍 DRY RUN - No files will be moved\n")
    else:
        print("\n📦 MOVING FILES\n")
    
    # Move files
    for category, files in sorted(categorized.items()):
        category_dir = posts_dir / category
        
        if not dry_run:
            category_dir.mkdir(exist_ok=True)
        
        print(f"\n📁 {category}/ ({len(files)} files)")
        print("-" * 70)
        
        for post_file in sorted(files):
            dest_path = category_dir / post_file.name
            
            if dry_run:
                print(f"  Would move: {post_file.name} → {category}/{post_file.name}")
            else:
                try:
                    shutil.move(str(post_file), str(dest_path))
                    print(f"  ✓ Moved: {post_file.name} → {category}/{post_file.name}")
                except Exception as e:
                    print(f"  ✗ Error moving {post_file.name}: {e}")
    
    print(f"\n{'='*70}")
    
    if dry_run:
        print("\nTo actually move the files, run: python3 organize_posts.py --execute")
    else:
        print("\n✅ All posts have been organized into category folders!")
        print("\nNext steps:")
        print("1. Review the organization")
        print("2. Run categorize_posts.py to add category fields to posts")
        print("3. Test locally with: bundle exec jekyll serve")
        print("4. Commit and push changes")

def main():
    import sys
    
    posts_dir = Path('_posts')
    dry_run = '--execute' not in sys.argv
    
    print("\n" + "="*70)
    print("Blog Posts Organization Tool")
    print("="*70)
    
    organize_posts(posts_dir, dry_run)

if __name__ == '__main__':
    main()
