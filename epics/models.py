from django.db import models


class Epic(models.Model):
    title = models.CharField(max_length=512, default=None, null=True, blank=True)
    cover_img = models.FileField(upload_to='uploads/', default=None, null=True, blank=True)
    global_url = models.TextField(default=None, null=True, blank=True)

    class Meta:
        db_table = "epics"
