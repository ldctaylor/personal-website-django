## Introduction
To put my Django skills into practice I decided to build a personal website with a portfolio page and a blog.

## Features
* [x] WYSIWIG editor for creating blog posts using TinyMCE
* [ ] Add blog post view (i.e. not from admin)
* [x] Page for 'featured' blog posts 
* [x] Users can create an account and log in 
* [x] Logged in users can like/unlike posts 
* [x] Slugs for post URLs, project URLs
* [x] Blog categories
* [x] Slugs for blog categories
* [ ] Media management
* [x] Ability to comment on blog posts
* [ ] Security features - highlight cs skills
* [ ] Add mini projects e.g. password generator
* [ ] Post not found / 404 and other errors - graceful handling
* [x] Excerpts for the home/index page instead of beginning of post text.
* [x] XML Sitemap
* [ ] spam protection for comments
* [ ] Multi-level comments using MPTT
   
## Project Status
Started August 2023. In progress.

### Slugs
Followed a [Learn Django tutorial](https://learndjango.com/tutorials/django-slug-tutorial) for the basic functionality. 
* [ ] Extend functionality to automatically generate slugs based on post title?
* [ ] Incorporate 'ID/slug' into URL

### MPTT
Explain what it is.
Very Academy tutorial.

## Bugs / Changes / Tasks
* [ ] change layout to grid style
* [ ] Optimise templates - create template for pagination
* [x] Pagination on category page not working
* [ ] Autopopulate the author of a blog post when saved
* [ ] Add front end for adding blog posts (not from admin view)
* [ ] How to display tinymce formatting while keeping content and comment fields safe from injection (excerpt/content is currently set to safe)
* [ ] Display email address in comment table (admin view)
* [x] Clicking on "read more" from Featured page leads to error.
* [x] Categories have a space at the end of the word that is part of the hyperlink, remove this
* [ ] Do I want the ability for users to create account / log in or shall I remove? Security implications.
* [ ] Create sitemap for static pages if I end up with many

## Deployment
https://docs.djangoproject.com/en/dev/howto/deployment/checklist/
https://learndjango.com/tutorials/django-best-practices-security
* [ ] Set domain name for XML sitemap, in admin/sites

## Dependencies
django-crispy-forms
crispy-bootstrap5
django-tinymce
pillow