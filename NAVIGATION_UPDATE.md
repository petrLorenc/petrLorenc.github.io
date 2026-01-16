# GitHub Pages Update - Dynamic Categories & Navigation

## What Changed

Your GitHub Pages site has been updated with a modern, dynamic categorization system and improved navigation structure.

## New Features

### 1. **Dynamic Navigation Menu**
- Clean dropdown menu for easy category access
- Mobile-responsive design
- Active page highlighting

### 2. **Four Content Categories**
- **Machine Learning**: Technical ML content, tutorials, and research
- **Software Engineering**: Programming tips, tools, and development insights
- **Travel**: Adventures and travel experiences
- **Books**: Book reviews and reading notes

### 3. **Category Pages**
Each category has a dedicated page with:
- Clean, consistent layout
- Category description
- Sub-navigation between categories
- All posts in that category

### 4. **Backward Compatibility**
- `/blog/` still works (shows all non-ML posts)
- `/blog_ml/` still works (shows all ML posts)
- Old URLs continue to function

## File Structure

### Directory Organization
```
_posts/
  books/                 # All book review posts
  machine_learning/      # All ML and AI posts
  software_engineering/  # All programming posts
  travel/                # All travel posts

_layouts/
  category.html          # Template for category pages

_includes/
  navigation.html        # Main navigation menu
  category_submenu.html  # Sub-navigation for categories

css/
  navigation.css         # Styling for new navigation

# Category pages
machine_learning.md
software_engineering.md
travel.md
books.md

# Helper files
organize_posts.py        # Script to organize posts into folders
categorize_posts.py      # Script to add category metadata
CATEGORIZATION_GUIDE.md  # Guide for manual categorization
```

### Modified Files
```
_config.yml              # Added category names
_layouts/default.html    # Updated navigation
blog.md                  # Added category submenu
blog_ml.md              # Added category submenu
```

## How to Use

### Adding Category to New Posts

When creating a new post, **place it in the appropriate subfolder** and add the `category` field in the front matter:

1. Create your post in the correct category folder:
   - `_posts/machine_learning/YYYY-MM-DD-title.md`
   - `_posts/travel/YYYY-MM-DD-title.md`
   - `_posts/books/YYYY-MM-DD-title.md`
   - `_posts/software_engineering/YYYY-MM-DD-title.md`

2. Add category in front matter:
```yaml
---
layout: post
title: Your Post Title
category: machine_learning  # must match the folder name
---
```

### Organizing Posts into Folders

All posts have been organized into category subdirectories within `_posts/`. This makes it much easier to manage and find posts by topic.

The folder structure matches the category system:
- `_posts/books/` - Book reviews
- `_posts/machine_learning/` - ML content
- `_posts/software_engineering/` - Programming content
- `_posts/travel/` - Travel posts

### Categorizing Existing Posts

#### Posts Are Already Organized! ✅

All 74 posts have been:
1. **Organized into category folders** - Moved to `_posts/category_name/`
2. **Tagged with category metadata** - Added `category:` field to front matter

The organization is complete:
- 📚 **20 book reviews** in `_posts/books/`
- 🤖 **28 ML posts** in `_posts/machine_learning/`
- 💻 **1 software post** in `_posts/software_engineering/`
- ✈️ **25 travel posts** in `_posts/travel/`

#### If You Need to Reorganize Later

Use the `organize_posts.py` script:

```bash
# Dry run to preview changes
python3 organize_posts.py

# Execute the reorganization
python3 organize_posts.py --execute
```

## Navigation Structure

```
Home
├── Categories (dropdown)
│   ├── Machine Learning
│   ├── Software Engineering
│   ├── Travel
│   └── Books
├── About Me
└── New Personal Pages
```

## Category Page URLs

- Machine Learning: `/machine_learning/`
- Software Engineering: `/software_engineering/`
- Travel: `/travel/`
- Books: `/books/`

## Styling

The new navigation includes:
- Dropdown menus (hover to reveal)
- Active page highlighting
- Responsive design for mobile
- Category submenu on category pages
- Clean, modern appearance

## Testing Locally

To test the changes locally:

```bash
bundle exec jekyll serve
```

Then visit `http://localhost:4000` to see your updated site.

## Next Steps

1. **Categorize Your Posts**: Run `python3 categorize_posts.py` to auto-categorize
2. **Review Changes**: Check auto-categorized posts and adjust as needed
3. **Manual Categorization**: Add categories to any posts that couldn't be auto-categorized
4. **Test**: View each category page to ensure posts are correctly categorized
5. **Deploy**: Commit and push to GitHub to publish changes

## Tips

- Use consistent category names (lowercase with underscores)
- Each post should have exactly one category
- The submenu appears on all category pages for easy navigation
- Mobile users can tap the dropdown to see categories

## Customization

### Adding More Categories

1. Edit `_config.yml` to add new category name
2. Create new category page (e.g., `new_category.md`)
3. Add link to `_includes/navigation.html` and `_includes/category_submenu.html`

### Changing Styles

Edit `/css/navigation.css` to customize:
- Colors
- Dropdown behavior
- Spacing
- Responsive breakpoints

## Support

See [CATEGORIZATION_GUIDE.md](CATEGORIZATION_GUIDE.md) for detailed categorization instructions.
