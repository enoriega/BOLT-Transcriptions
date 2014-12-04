from django.shortcuts import render
from django.views.generic import View
from models import *
from django.shortcuts import *

# Create your views here.

class AnnView(View):
    template_name = "form.html"
    Model = None
    lang = None
    lang_label = None
    Form = None

    def get(self, request):

        elements = self.Model.objects.filter(annotated=False)

        if len(elements) == 0:
            return redirect('done')
        else:
            f = self.Form(elements[0])
            return render_to_response(self.template_name, {'form':f, 'layout':'horizontal', 'id':elements[0].id})

    def post(self, request):
        ann = elements = self.Model.objects.get(pk=request.POST['ann-id'])
        ann.annotated = True
        f = self.Form(request.POST, instance=ann)

        if f.is_valid():
            f.save()
            return redirect(lang)
        else:
            return render_to_response(self.template_name, {'form':f, 'layout':'horizontal', 'id':ann.id})


class ENView(AnnView):
    Model = ENAnnotation
    lang = "en"
    lang_label = 'english'
    Form = ENAnnotationForm


class ARView(AnnView):
    Model = ARAnnotation
    lang = "ar"
    lang_label = 'arabic'
    Form = ARAnnotationForm
