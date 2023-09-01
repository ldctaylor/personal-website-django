## Introduction
To put my Django skills into practice I decided to build a personal website with a portfolio page and a blog.

## Features
* [x] WYSIWIG editor for creating blog posts using TinyMCE
* [x] Page for 'featured' blog posts 
* [x] Users can create an account and log in 
* [x] Logged in users can like/unlike posts 
* [x] Slugs for post URLs
* [ ] Blog categories
* [ ] Slugs for blog categories
* [ ] Ability to comment on blog posts
* [ ] Security features - highlight cs skills
* [ ] Add mini projects e.g. password generator
* [ ] Post not found / 404 and other errors - graceful handling
* [ ] Excerpts for the home/index page instead of beginning of post text. Very Academy "Simple Blog App" 1h29
* [ ] XML Sitemap

## Project Status
Started August 2023. In progress.

### Slugs
Followed a [Learn Django tutorial](https://learndjango.com/tutorials/django-slug-tutorial) for the basic functionality. 
* [ ] Extend functionality to automatically generate slugs based on post title?
* [ ] Incorporate 'ID/slug' into URL

## Bugs / Changes / Tasks
* [x] Clicking on "read more" from Featured page leads to error.
* [x] Categories have a space at the end of the word that is part of the hyperlink, remove this
* [ ] Do I want the ability for users to create account / log in or shall I remove? Security implications.
* [ ] Create sitemap for static pages if I end up with many

## Deployment
* [ ] Set domain name for XML sitemap, in admin/sites