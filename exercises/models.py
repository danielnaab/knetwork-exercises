import re

from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

class KhanExerciseTreeNode(MPTTModel):
    parent = TreeForeignKey('self',
        null=True, blank=True, related_name='children')

    khan_id = models.CharField(max_length=255)
    display_name = models.CharField(max_length=255)
    live = models.BooleanField()
    url = models.URLField(null=True)
    is_topic = models.BooleanField(default=False)

    @property
    def is_exercise(self):
        # This is a hack.  There should be a separate field for this...
        return not self.is_topic

    @property
    def filename(self):
        return 'wwwkhanacademyorgexercise%s-full-trimmed.png' % (
            re.sub('\W', '', self.khan_id)
        )

    def __unicode__(self):
        return self.khan_id
