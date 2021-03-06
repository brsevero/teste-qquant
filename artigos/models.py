from django.db import models
from django.contrib.postgres.fields import ArrayField


class Article(models.Model):
    type_of_reference = models.CharField(max_length=50, null=True, blank=True)
    primary_title = models.CharField(max_length=1000, null=True, blank=True)
    first_authors = ArrayField(
        models.CharField(max_length=1000, null=True, blank=True), null=True, blank=True
    )
    secondary_authors = ArrayField(
        models.CharField(max_length=50, null=True, blank=True), null=True, blank=True
    )
    publication_year = models.CharField(max_length=500, null=True, blank=True)
    notes_abstract = models.CharField(max_length=1000, null=True, blank=True)
    keywords = ArrayField(
        models.CharField(max_length=1000, null=True, blank=True), null=True, blank=True
    )
    alternate_title3 = models.CharField(max_length=500, null=True, blank=True)
    alternate_title2 = models.CharField(max_length=500, null=True, blank=True)
    volume = models.CharField(max_length=50, null=True, blank=True)
    number = models.CharField(max_length=50, null=True, blank=True)
    start_page = models.CharField(max_length=50, null=True, blank=True)
    place_published = models.CharField(max_length=500, null=True, blank=True)
    publisher = models.CharField(max_length=500, null=True, blank=True)
    issn = models.CharField(max_length=50, null=True, blank=True)
    note = models.CharField(max_length=1000, null=True, blank=True)
    file_attachments2 = models.CharField(max_length=500, null=True, blank=True)
    url = models.CharField(max_length=1000, null=True, blank=True)
    end_of_reference = models.CharField(max_length=500, null=True, blank=True)

    class Meta:
        ordering = ["first_authors"]
        db_table = 'table_article'
        verbose_name_plural = 'Articles'

    def str(self):
        return self.type_of_reference + " " + self.first_authors
