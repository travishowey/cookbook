from django.shortcuts import render, redirect
from.models import Recipe
from django.http import HttpResponse
from django.template import loader
import pdfkit
from .forms import ItemForm
from django.core.paginator import Paginator
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# Create your views here.


def index(request):
    item_list = Recipe.objects.all()[2:5]
    context = {
        'item_list': item_list,
    }
    return render(request, 'howeydoin/index.html', context)


def detail(request, item_id):
    item = Recipe.objects.get(pk=item_id)
    context = {
        'item': item,
    }
    return render(request, 'howeydoin/detail.html', context)


def allrecipes(request):
    item_list = Recipe.objects.all()
    recipe_search = request.GET.get('recipe_search')
    if recipe_search != '' and recipe_search is not None:
        item_list = item_list.filter(name__icontains=recipe_search)
    paginator = Paginator(item_list, 5)
    page = request.GET.get('page')
    item_list = paginator.get_page(page)

    context = {
        'item_list': item_list,
    }
    return render(request, 'howeydoin/allrecipes.html', context)


def aboutus(request):
    return render(request, 'howeydoin/about.html')


def download(request, item_id):
    recipe = Recipe.objects.get(pk=item_id)
    template = loader.get_template('howeydoin/download.html')
    html = template.render({'recipe': recipe})
    options = {
        'page-size': 'Letter',
        'encoding': 'UTF-8'
    }
    pdf = pdfkit.from_string(html, False, options)
    response = HttpResponse(pdf, content_type='application/pdf+')
    response['Content-Disposition'] = 'attachment'
    filename = "recipe.pdf"

    return response


def questions(request):
    return render(request, 'howeydoin/questions.html')


def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('home:index')

    return render(request, 'howeydoin/item-form.html', {'form': form})
