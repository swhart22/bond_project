from __future__ import unicode_literals

from django.db import models

from django.template.defaultfilters import slugify 

from suit_ckeditor.widgets import CKEditorWidget

from redactor.fields import RedactorField
from tinymce import models as tinymce_models


class Article(models.Model):
	headline = models.CharField(max_length=128, unique=True)
	body = tinymce_models.HTMLField()
	slug = models.SlugField()
	
	def save(self, *args, **kwargs):
		self.slug = slugify(self.headline)
		super(Article, self).save(*args, **kwargs)
	
	def __str__(self):
		return self.headline
