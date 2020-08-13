'''
Всякий раз при возникновении подозрений относительно моделей выполняйте команду
python manage.py check
Она обнаруживает все типичные ошибки в моделях.

Следующая команда выведет в консоль SQL нашей первой миграции:
python manage.py sqlmigrate catalog 0001
'''
import os

from django.db import models
from django.conf import settings
from django.urls import reverse # To generate URLS by reversing URL patterns
from django.contrib.auth.models import User  # Required to assign User as a borrower

# === - Take full_path of book - ===
def get_review_manuscript_full_path(instance, filename):
    ext = filename.split('.')[-1]
    root = settings.MEDIA_ROOT
    cpk = instance.slug if instance else 'unknown_cats'
    path = f'{root}/{cpk}'
    name = f'{instance.title}'
    return f'{path}/{name}.{ext}'

# dla vozvrasheniya direktorii i nazvanie field gde budet save pictura
def generate_filename(instance, filename):
    filename = instance.slug + '.jpg'
    return "{0}/{1}".format(instance.slug, filename)


class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    country = models.CharField(max_length=50)

    def __str__(self):
        return '{0}'.format(self.name)


class Genre(models.Model):
    """Model representing a book genre (e.g. Science Fiction, Non Fiction)."""
    name = models.CharField(max_length=200, help_text="Enter a book genre (e.g. Science Fiction, French Poetry etc.)")

    def get_absolute_url(self):
        """Returns the url to access a particular category instance."""

        return reverse('category-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return '{0}'.format(self.name)


class Language(models.Model):
    """Model representing a Language (e.g. English, French, Japanese, etc.)"""
    name = models.CharField(max_length=200, help_text="Enter the book's natural language")

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return '{0}'.format(self.name)


class Author(models.Model):
    """Model representing an author."""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('died', null=True, blank=True)
    email = models.EmailField(unique=True, null=True, blank=True)

    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""

        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return '{0}, {1}'.format(self.last_name, self.first_name)


class Book(models.Model):
    """Model representing a book (but not a specific copy of a book)."""
    review_manuscript = models.FileField(upload_to=get_review_manuscript_full_path)
    # Genre class has already been defined so we can specify the object above.
    fk_genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    # Foreign Key used because book can only have one author, but authors can have multiple books
    # Author as a string rather than object because it hasn't been declared yet in the file.
    fk_author = models.ForeignKey(Author, on_delete=models.CASCADE)
    fk_language = models.ForeignKey(Language, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.SlugField()
    image = models.ImageField(upload_to=generate_filename)
    summary = models.TextField(max_length=1000, help_text="Enter a brief description of the book")
    publication_date = models.DateField()
    fk_publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)

    def get_absolute_url(self):
        """Returns the url to access a particular book instance."""

        return reverse('book-detail', args=[str(self.id)])

    def get_book_path(self):
        """Returns the url to access a particular category instance."""

        # Remove media root path from file path
        # '/home/kakajan/Projects/Kitap/media/kngaDjango/Django.pdf' - '/home/kakajan/Projects/Kitap/media/' = 'kngaDjango/Django.pdf'
        review = os.path.relpath(self.review_manuscript.path, settings.MEDIA_ROOT)

        # Add media url to file path
        # '/media/' + 'kngaDjango/Django.pdf' = '/media/kngaDjango/Django.pdf'
        review = settings.MEDIA_URL + review

        return review


    def __str__(self):
        """String for representing the Model object."""

        return self.title