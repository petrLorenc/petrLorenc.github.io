# Blog Categorization Guide

## Overview
The blog now supports dynamic categorization with 4 main categories:
- **machine_learning**: ML tutorials, papers, and technical AI content
- **software_engineering**: Programming tutorials, tips, and development insights
- **travel**: Travel experiences and adventures
- **books**: Book reviews and reading notes

## How to Categorize Posts

### Adding Category to Posts
In the front matter of each post, add a `category` field:

```yaml
---
layout: post
title: Your Post Title
category: machine_learning
---
```

### Category Values
Use one of these exact values:
- `machine_learning`
- `software_engineering`
- `travel`
- `books`

### Migration from Old Tags
The old system used a `tag` field. Replace it with `category`:

**Old format:**
```yaml
---
layout: post
title: Logistic Regression
tag: machine learning
---
```

**New format:**
```yaml
---
layout: post
title: Logistic Regression
category: machine_learning
---
```

## Navigation Structure

### Main Navigation
- Home
- Categories (dropdown)
  - Machine Learning
  - Software Engineering
  - Travel
  - Books
- About Me
- New Personal Pages

### Category Pages
Each category has its own page:
- `/machine_learning/` - All machine learning posts
- `/software_engineering/` - All software engineering posts
- `/travel/` - All travel posts
- `/books/` - All book reviews

### Legacy Pages
- `/blog/` - All posts except machine learning (for backward compatibility)
- `/blog_ml/` - All machine learning posts (for backward compatibility)

## Example Post Updates

### Machine Learning Post
```yaml
---
layout: post
title: My intuitive explanation of Logistic Regression!
category: machine_learning
---
```

### Travel Post
```yaml
---
layout: post
title: Barcelona Adventure
category: travel
description: My experience in sunny Barcelona
author: Petr Lorenc
comments: true
---
```

### Book Review Post
```yaml
---
layout: post
title: Homo Deus - A Brief History of Tomorrow
category: books
comments: true
---
```

### Software Engineering Post
```yaml
---
layout: post
title: Python defaultdict
category: software_engineering
---
```

## Benefits
1. **Better Organization**: Posts are clearly categorized
2. **Easy Navigation**: Dropdown menu provides quick access
3. **Category Pages**: Dedicated pages for each topic
4. **Backward Compatible**: Old `/blog/` and `/blog_ml/` still work
5. **Scalable**: Easy to add new categories in the future
