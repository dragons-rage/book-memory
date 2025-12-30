"""
Django models for the Book Memory application.

This module defines the database models used to track books, authors, series,
locations, and reading status. The application helps users avoid accidentally
purchasing or starting books they've already read or didn't enjoy.
"""

from django.db import models


class Author(models.Model):
    """
    Represents a book author with first and last name.
    
    Authors can be associated with multiple books through a many-to-many
    relationship defined in the Book model.
    """

    # Full name of the author (up to 100 characters)
    full_name = models.CharField(max_length=100, default="")
    official_alias = models.CharField(max_length=100, blank=True, default="")
    alias = models.CharField(max_length=100, blank=True, default="")
    # Used for sorting and display purposes
    first_name = models.CharField(max_length=100, blank=True, default="")
    last_name = models.CharField(max_length=100, blank=True, default="")

    notes = models.TextField(blank=True, default="")

    def __str__(self):
        """Return the author's full name as a string representation."""
        if self.official_alias:
            return self.official_alias
        if self.first_name and self.last_name:
            return f"{self.last_name}, {self.first_name}"
        if self.full_name:
            return self.full_name
        return ""

class Tags(models.Model):
    name = models.CharField(
        max_length=255,
        unique = True,
        help_text="Name of the tag."
    )

    description = models.TextField(
        blank = True,
        default = ""
    )

    def __str__(self):
        return str(self.name)

    class Meta:
        indexes = [
            models.Index(fields=["name"], name="teg_name_index")
        ]
        verbose_name = "Tag"
        verbose_name_plural = "Tags"

class Series(models.Model):
    """
    Represents a book series that can contain multiple books.
    
    Tracks series information and allows marking how many books
    are missing from the user's collection.
    """
    
    # Title of the book series (up to 100 characters)
    title = models.CharField(max_length=100)
    
    # Number of books missing from this series in the user's collection
    # Optional field that can be null if not tracking missing books
    missing = models.SmallIntegerField(
        blank=True, 
        null=True, 
        default=None,
        help_text="Number of books missing from this series"
    )

    tags = models.ManyToManyField(
        Tags, 
        blank=True, 
        default=None, 
        help_text="Tags in the Series"
    )

    def __str__(self):
        """Return the series title as a string representation."""
        return str(self.title)

    class Meta:
        verbose_name = "Series"
        # Prevent Django from pluralizing as "Seriess"
        verbose_name_plural = "Series"




class Location(models.Model):
    """
    Represents a physical or digital location where books are stored.
    
    Examples: "Home Library", "Kindle", "Audible", "Office", etc.
    """
    
    # Name of the location (up to 25 characters)
    name = models.CharField(
        max_length=25,
        help_text="Name of where the book is stored (e.g., 'Home Library', 'Kindle')"
    )

    def __str__(self):
        """Return the location name as a string representation."""
        return str(self.name)


class Ratings(models.Model):
    """
    Represents the reading status or rating of a book.
    
    Note: Despite the name 'Ratings', this model is used to track status
    (e.g., 'Read', 'Currently Reading', 'Want to Read', 'Did Not Like').
    The Meta class correctly labels this as 'Status' in the admin interface.
    """
    
    # Name of the status/rating (up to 25 characters)
    name = models.CharField(
        max_length=25,
        help_text="Status of the book (e.g., 'Read', 'Currently Reading', 'Did Not Like')"
    )

    priority = models.SmallIntegerField(
        default=0,
        help_text="Priority of the status (higher numbers indicate higher priority)"
    )

    def __str__(self):
        """Return the status name as a string representation."""
        return str(self.name)
    
    class Meta:
        # Correct labeling in admin interface
        verbose_name = "Status"
        verbose_name_plural = "Statuses"

class MediaType(models.Model):
    """
    Represents the type or genre of a book.
    """
    name = models.CharField(
        max_length=25,
        help_text="Type of the media (e.g., 'Novel', 'Manga', 'Audiobook')"
    )

    def __str__(self):
        """Return the type name as a string representation."""
        return str(self.name)

    class Meta:
        verbose_name = "Type"
        verbose_name_plural = "Types"


class Book(models.Model):
    """
    Main model representing a book with all its associated information.
    
    This model ties together authors, series, location, and status to provide
    a comprehensive view of the user's book collection and reading progress.
    """

    # Title of the book (up to 100 characters)
    title = models.CharField(
        max_length=255,
        help_text="Full title of the book"
    )
    
    # Many-to-many relationship with authors (books can have multiple authors)
    authors = models.ManyToManyField(
        Author, 
        blank=True, 
        default=None, 
        related_name="books",
        help_text="Authors who wrote this book"
    )

    media_type = models.ForeignKey(
        MediaType,
        on_delete=models.SET_NULL,
        null=True,
        default=None,
        related_name="books",
        help_text="Type of media (e.g., 'Novel', 'Manga', 'Audiobook')"
    )
    # Current reading status/rating of the book
    # Uses SET_NULL to preserve book data if status is deleted
    status = models.ForeignKey(
        Ratings, 
        on_delete=models.SET_NULL, 
        null=True, 
        default=None,
        help_text="Current reading status of the book"
    )
    
    # Reading progress as a percentage or page number
    progress = models.SmallIntegerField(
        blank=True, 
        null=True,
        help_text="Reading progress (percentage or page number)"
    )
    
    # Link or ASIN for the book
    # TODO: Implement more codes and link formats
    link = models.CharField(
        max_length=255, 
        blank=True, 
        null=True, 
        default="",
        help_text="Link or ASIN for this book"
    )
    # TODO: Add a spot for Extra Links

    # Personal notes about the book
    notes = models.TextField(
        blank=True,
        help_text="Personal notes, thoughts, or reviews about the book"
    )
    
    # Series this book belongs to (if any)
    # CASCADE deletion removes books when series is deleted
    series = models.ForeignKey(
        Series, 
        on_delete=models.CASCADE, 
        null=True, 
        default=None, 
        blank=True, 
        related_name="books",
        help_text="Series this book belongs to"
    )
    
    # Physical or digital location where the book is stored
    location = models.ForeignKey(
        Location, 
        on_delete=models.CASCADE, 
        null=True, 
        default=None,
        related_name="books",
        help_text="Where this book is stored"
    )

    # img = models.ImageField(
    #     upload_to='book_covers/',
    #     blank=True,
    #     null=True,
    #     help_text="Cover image for this book"
    # )

    # epub = models.FileField(
    #     upload_to='book_epubs/',
    #     blank=True,
    #     null=True,
    #     help_text="EPUB file for this book"
    # )

    def __str__(self):
        """Return the book title as a string representation."""
        return str(self.title)

    def authorlist(self):
        """
        Return a comma-separated string of all authors for this book.
        
        Returns:
            str: Comma-separated list of author names, or empty string if no authors.
            
        Example:
            "Jane Doe, John Smith"
        """
        return ", ".join(str(author) for author in self.authors.all())
