from django.db import models

# Create your models here.
from utils.model_utils import AbstractRowInformation, AbstractNameAndDescription


class Tag(AbstractRowInformation, AbstractNameAndDescription):
    """
    Model to Store Tag
    """
    _MODEL_CODE = 'TG'

    class Meta:
        db_table = 'tags'

    def save(self, *args, **kwargs):
        super(Tag, self).save(*args, **kwargs)

