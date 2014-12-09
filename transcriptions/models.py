from django.db import models
from django.forms import ModelForm
import pdb

# Create your models here.

class Annotation(models.Model):

    audio = models.CharField(max_length=100)
    sentence_id = models.CharField(max_length=50)
    hyp = models.CharField(max_length=200)
    trans = models.CharField(max_length=200)
    annotated = models.BooleanField(default=False)
    skipped = models.BooleanField(default=False)

    def __unicode__(self):
        return self.hyp


class ENAnnotation(Annotation):
    pass

class ARAnnotation(Annotation):
    pass

class AnnotationForm(ModelForm):
    def clean(self):

        if not self.instance is None and "skip" in self.data:
            self.instance.skipped = True

class ENAnnotationForm(AnnotationForm):
    class Meta:
        model = ENAnnotation
        fields = ['trans']



class ARAnnotationForm(AnnotationForm):
    class Meta:
        model = ENAnnotation
        fields = ['trans']
