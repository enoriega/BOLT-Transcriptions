from django.db import models

# Create your models here.

class Annotation(models.Model):
    
    audio = models.CharField(max_length=100)
    hyp = models.CharField(max_length=200)
    trans = models.CharField(max_length=200)

    def _unicode_(self):
        return self.hyp


class ENAnnotation(Annotation):
    pass

class ARAnnotation(Annotation):
    pass
