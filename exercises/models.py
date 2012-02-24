from django.db import models

from mptt.models import MPTTModel, TreeForeignKey

class KhanExerciseTreeNode(MPTTModel):
    parent = TreeForeignKey('self',
        null=True, blank=True, related_name='children')

    khan_id = models.CharField(max_length=255)
    display_name = models.CharField(max_length=255)
    live = models.BooleanField()
    url = models.URLField()

    def __unicode__(self):
        return self.khan_id
