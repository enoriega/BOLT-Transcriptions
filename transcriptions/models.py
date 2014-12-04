from django.db import models
from django.forms import ModelForm

# Create your models here.

class Annotation(models.Model):

    audio = models.CharField(max_length=100)
    sentence_id = models.CharField(max_length=50)
    hyp = models.CharField(max_length=200)
    trans = models.CharField(max_length=200)
    annotated = models.BooleanField(default=False)

    def __unicode__(self):
        return self.hyp


class ENAnnotation(Annotation):
    pass

class ARAnnotation(Annotation):
    pass


class ENAnnotationForm(ModelForm):
    class Meta:
        model = ENAnnotation
        fields = ['trans']

class ARAnnotationForm(ModelForm):
    class Meta:
        model = ENAnnotation
        fields = ['trans']
