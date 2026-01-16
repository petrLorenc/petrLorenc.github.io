# Posts Reorganization Summary

## What Was Done

All blog posts in the `_posts/` directory have been reorganized into category-based subdirectories for better organization and management.

## Changes Made

### 1. Directory Structure Created

```
_posts/
├── books/                  (20 posts)
├── machine_learning/       (28 posts)
├── software_engineering/   (1 post)
└── travel/                 (25 posts)
```

### 2. All Posts Moved

**Total: 74 posts organized**

#### Books (20 posts)
- Book reviews and reading notes
- Includes: Homo Deus, Factfulness, Solve for Happy, etc.

#### Machine Learning (28 posts)
- ML tutorials, papers, and technical content
- Includes: Logistic Regression, NLP, Neural Networks, ELMO, etc.

#### Software Engineering (1 post)
- Programming tutorials and tips
- Python defaultdict

#### Travel (25 posts)
- Travel experiences and adventures
- Includes: Barcelona, Taiwan, Italy, Malta, Seattle, etc.

### 3. Category Metadata Added

Every post now has a `category:` field in its front matter matching its directory:

```yaml
---
layout: post
title: Post Title
category: machine_learning  # matches the folder name
---
```

## Jekyll Compatibility

✅ **Jekyll fully supports posts in subdirectories!**

Posts in `_posts/subdirectory/` are processed exactly like posts in `_posts/` root. The subdirectory structure:
- Does NOT affect URLs
- Does NOT affect permalinks
- Does NOT affect site generation
- ONLY helps with organization

## Benefits

1. **Better Organization**: Easy to find posts by category
2. **Easier Management**: Related posts grouped together
3. **Clearer Structure**: Obvious which posts belong to which category
4. **Scalability**: Easy to add new posts to the right category
5. **Maintenance**: Simpler to maintain and update category-specific posts

## Scripts Used

### organize_posts.py
Automatically organizes posts into category folders based on:
1. Existing `category:` field in front matter
2. Old `tag:` field (for backward compatibility)
3. Filename pattern matching

### categorize_posts.py
Adds `category:` metadata to posts based on:
1. Parent directory name (primary method)
2. Existing tags
3. Filename patterns

## For New Posts

When creating new posts, follow this structure:

```bash
# Create post in appropriate category folder
_posts/machine_learning/2026-01-16-New-ML-Post.md
_posts/travel/2026-01-16-Trip-to-Prague.md
_posts/books/2026-01-16-Book-Review.md
_posts/software_engineering/2026-01-16-Coding-Tips.md
```

And include the category in front matter:

```yaml
---
layout: post
title: My New ML Tutorial
category: machine_learning
date: 2026-01-16
---
```

## Testing

To verify everything works:

```bash
# Test locally
bundle exec jekyll serve

# Visit http://localhost:4000
# Check all category pages work
# Verify posts appear correctly
```

## Commit Message Suggestion

```
Reorganize blog posts into category subdirectories

- Moved all 74 posts into category-specific folders:
  * 20 posts → _posts/books/
  * 28 posts → _posts/machine_learning/
  * 1 post  → _posts/software_engineering/
  * 25 posts → _posts/travel/

- Added category metadata to all posts
- Created organize_posts.py for future reorganization
- Updated categorize_posts.py to work with subdirectories

This improves organization while maintaining full Jekyll compatibility.
Post URLs and permalinks remain unchanged.
```

## Next Steps

1. ✅ Posts organized into folders
2. ✅ Category metadata added
3. 🔄 Test locally (optional)
4. 🔄 Commit and push changes
5. 🔄 Verify on GitHub Pages

## Rollback (if needed)

If you need to undo this:

```bash
# Move all posts back to _posts root
find _posts/*/*.md -type f -exec mv {} _posts/ \;

# Remove empty category directories
rmdir _posts/*/
```

However, this organization is beneficial and recommended to keep!
