# Static Files for Book Organizer App

This directory contains static files (CSS, JavaScript, images) for the bookorganizer Django app.

## Directory Structure

```
bookorganizer/static/bookorganizer/
├── css/
│   └── style.css          # CSS styles for the app
├── js/
│   └── bookorganizer.js   # JavaScript functionality
└── images/
    └── .gitkeep           # Keeps directory in version control
```

## Usage in Templates

To use these static files in your Django templates:

1. Load the static template tag at the top of your template:
   ```django
   {% load static %}
   ```

2. Reference static files using the static tag:
   ```django
   <!-- CSS -->
   <link rel="stylesheet" type="text/css" href="{% static 'bookorganizer/css/style.css' %}">
   
   <!-- JavaScript -->
   <script src="{% static 'bookorganizer/js/bookorganizer.js' %}"></script>
   
   <!-- Images -->
   <img src="{% static 'bookorganizer/images/logo.png' %}" alt="Logo">
   ```

## Development vs Production

- **Development**: Django's staticfiles app serves static files automatically when `DEBUG=True`
- **Production**: Run `python manage.py collectstatic` to gather all static files into the `STATIC_ROOT` directory

## CSS Classes Available

The `style.css` file includes these example classes:
- `.book-container` - Container for book items
- `.book-title` - Styling for book titles
- `.book-author` - Styling for book authors

## JavaScript Functions

The `bookorganizer.js` file includes:
- `initializeBookOrganizer()` - Main initialization function
- Click event handlers for book elements

See `example_with_static.html` template for usage examples.
