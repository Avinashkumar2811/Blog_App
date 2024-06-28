# 📝 Blog Post Management System

Welcome to the Blog Post Management System! This project allows users to create, update, view, and delete blog posts.

## 🚀 Features

- 🖋️ Create new blog posts
- 📝 Update existing posts
- 👀 View all posts
- ❌ Delete posts
- 🛡️ CSRF protection for forms

## 🏗️ Project Structure

```plaintext
project_root/
│
├── blog/                       # Main application directory
│   ├── migrations/             # Database migrations
│   ├── templates/              # HTML templates
│   │   ├── blog/
│   │   │   ├── create_post.html    # Create post form
│   │   │   ├── update_post.html    # Update post form
│   │   │   ├── delete_post.html    # Delete post confirmation
│   │   │   ├── post_list.html      # List of all posts
│   │   │   └── post_detail.html    # Detail view of a post
│   ├── __init__.py             # Package initializer
│   ├── admin.py                # Admin interface setup
│   ├── apps.py                 # App configuration
│   ├── models.py               # Database models
│   ├── tests.py                # Unit tests
│   ├── urls.py                 # URL routes
│   └── views.py                # View functions
│
├── project_name/               # Project directory
│   ├── __init__.py             # Package initializer
│   ├── settings.py             # Project settings
│   ├── urls.py                 # URL routes
│   ├── wsgi.py                 # WSGI configuration
│
├── manage.py                   # Django management script
└── README.md                   # Project readme file
```
