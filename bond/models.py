from __future__ import unicode_literals

from django.db import models

from django.template.defaultfilters import slugify 

from suit_ckeditor.widgets import CKEditorWidget

from redactor.fields import RedactorField
from tinymce import models as tinymce_models


class Article(models.Model):
	headline = models.CharField(max_length=128, unique=True)
	header = models.URLField("header Image URL (900px by 300px)")
	body = tinymce_models.HTMLField()
	slug = models.SlugField("slug (autogenerates, don't mess with this)")
	
	def save(self, *args, **kwargs):
		self.slug = slugify(self.headline)
		super(Article, self).save(*args, **kwargs)
	
	def __str__(self):
		return self.headline
