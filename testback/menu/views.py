from django.http import HttpResponse
from django.shortcuts import render
from .models import *


def get_parent_category(request):
    categories = []
    for cat in Category.objects.all():
        if cat.is_have_parent() == None:
            categories.append(cat)
    return render(request, 'menu/index.html', {'categories': categories})


def get_category(request, id):
    categories = []
    parent = Category.objects.get(pk=id)
    parents = [parent]
    while parent.is_have_parent()!=None:
        parent = parent.parent
        parents.append(parent)
    for parent in parents:
        for child in Category.objects.filter(parent__id=parent.id):
            if child not in categories:
                categories.append(child)
        if parent not in categories:
            categories.append(parent)
    categories.reverse()
    for cat in Category.objects.filter(parent__id=None):
        if cat.is_have_parent() == None and cat not in categories:
            categories.append(cat)
    return render(request, 'menu/index.html', {'categories': categories})