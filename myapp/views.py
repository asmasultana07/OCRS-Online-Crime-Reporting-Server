# myapp/views.py
from django.shortcuts import render

from .models import Item  # Replace 'Item' with the actual name of your model
from .forms import SearchForm

def search_view(request):
    query = request.GET.get('q', '')

    if 'name:' in query:
        name_query = query.split('name:')[1].strip()
        results = Item.objects.filter(name__icontains=name_query)
    else:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['search_query']
            results = Item.objects.filter(name__icontains=query)
        else:
            results = Item.objects.all()

    return render(request, 'myapp/search.html', {'query': query, 'results': results})
