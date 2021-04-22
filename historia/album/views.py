from django.shortcuts import get_object_or_404
from django.template import loader
from django.http import HttpResponse

from .models import SiteInfo, Category, Document, Donor


def _get_basic_context():
    return {
        'site_info': SiteInfo.get_data(),
        'categories': Category.objects.all(),
    }


def index(request):
    template = loader.get_template('album/index.html')
    context = _get_basic_context()
    context['last_documents'] = Document.objects.all()[:23]
    context['documents_number'] = Document.objects.all().count()
    context['donors_number'] = Donor.objects.all().count()
    return HttpResponse(template.render(context, request))


def about(request):
    template = loader.get_template('album/about.html')
    context = _get_basic_context()
    return HttpResponse(template.render(context, request))


def category(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    template = loader.get_template('album/category.html')
    context = _get_basic_context()
    context['category'] = category
    documents = Document.objects.filter(category=category)
    context['documents'] = documents
    return HttpResponse(template.render(context, request))


def document(request, document_id):
    document = get_object_or_404(Document, pk=document_id)
    template = loader.get_template('album/document.html')
    context = _get_basic_context()
    context['document'] = document
    return HttpResponse(template.render(context, request))
