from django.views.generic import TemplateView

# Create your views here.
class PhotoView(TemplateView): template_name = 'photo.html'

def get_context_data(self, **kwargs):
    p = kwargs['name']
    p = f'/static/images/{p}'
    return dict(photo=p)