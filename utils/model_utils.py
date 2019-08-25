# third party imports

# django imports
from django.template.defaultfilters import slugify
from django.utils.crypto import get_random_string
from django.db import models

# project level imports


# app level imports

def custom_slugify(data, suffix=True, offset=15):
    """
    Using django util methods create a slug.
    Append a random string at the end of the slug if necessary for making it unique
    """

    # slugify the source_field passed to the function
    new_slug = slugify(data)[:offset]

    if suffix:
        # get a random string of length 10
        random_str = get_random_string(length=10)

        # the new_slug and random_str is concatenated
        new_slug = "{0}-{1}".format(new_slug, random_str)

    return new_slug


class AbstractRowInformation(models.Model):
    """
    This class is used to maintain meta information such as is_active, created_at, modified_at
    This can  be inherited in other classes to avoid making repeated attributes
    """
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class AbstractNameAndDescription(models.Model):
    """
    Abstract model to store name, description, slug and code generation logic
    """
    name = models.CharField(max_length=100, blank=False, null=False, unique=True)
    description = models.TextField(blank=True)
    slug = models.CharField(max_length=100, null=True, blank=True, unique=True)  # marked as blank to avoid django forms

    _MODEL_CODE = ''

    class Meta:
        abstract = True

    @property
    def code(self):
        return "{0}/{1}".format(self._MODEL_CODE, self.pk)

    def __str__(self):
        return "{0} - {1}".format(self.code, self.name)
