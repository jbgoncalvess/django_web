#from django.shortcuts import render
from django.views.generic import TemplateView

# def index(request):
#     context = {
#         'disciplina': 'Desenvolvimento Web',
#         'tecnologia': 'Python e Django'
#     }
# return render(request,'index.html', context)
class IndexView(TemplateView):
    template_name = 'index.html'