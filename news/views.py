from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

# Create your views here.

def news_view(request):
    page = """
    <h1 style="color:blue;">A Blue Heading</h1>
    <p style="color:red;">A red paragraph.</p>
    <ul>
        <li>News 1</li>
        <li>News 2</li>
        <li>News 3</li>
    </ul>
    
    """
    return HttpResponse(page)

class HomePageView(TemplateView):
    template_name = 'index.html'