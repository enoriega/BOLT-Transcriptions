from django.shortcuts import render
from django.views.generic import View
from models import *
from django.shortcuts import *

# Create your views here.

class AnnView(View):
    template_name = "transcriptions/form.html"
    Model = None
    lang = None
    lang_label = None
    Form = None

    def get(self, request):

        pending = self.Model.objects.filter(annotated=False)
        skipped = self.Model.objects.filter(skipped=True)

        if len(pending) == 0 and len(skipped) == 0:
            return redirect('done')
        else:
            element = pending[0] if len(pending) > 0 else skipped[0]

            f = self.Form(instance=element)
            return render_to_response(self.template_name, {'form':f, 'layout':'horizontal', 'id':element.pk, 'audio':element.audio})

    def post(self, request):
        ann = elements = self.Model.objects.get(pk=request.POST['ann-id'])
        ann.annotated = True

        f = self.Form(request.POST, instance=ann)

        if f.is_valid():
            f.save()
            return redirect(self.lang)
        else:
            return render_to_response(self.template_name, {'form':f, 'layout':'horizontal', 'id':ann.id, 'audio':ann.audio})


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
