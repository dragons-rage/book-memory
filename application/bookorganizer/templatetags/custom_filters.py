from django import template
import re

register = template.Library()

# Example filter: join a queryset of authors by comma
@register.filter
def join_authors(authors):
    return ", ".join([str(author) for author in authors])

# Add more custom filters below
@register.filter
def is_asin(s):
    """
    Checks if a string is a valid ASIN.

    Args:
        s: The string to check.

    Returns:
        True if the string is a valid ASIN, False otherwise.
    """
    # ASINs are typically 10 alphanumeric characters.
    # The pattern matches 10 characters that are either letters (uppercase or lowercase) or digits.
    asin_pattern = re.compile(r'^[A-Za-z0-9]{10}$')
    return bool(asin_pattern.fullmatch(s))

@register.filter
def is_url(s):
    url_pattern = re.compile(
        r'^(https?://)?'  # http:// or https:// (optional)
        r'([a-zA-Z0-9-]+\\.)+[a-zA-Z]{2,}'  # domain
        r'(:\\d+)?'  # optional port
        r'(/\\S*)?$'  # optional path
    )
    return bool(url_pattern.match(s))