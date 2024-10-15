from django.shortcuts import render
from .models import Country

def index(request):
    countries = Country.objects.all()
    continent = { continent_type: Country.objects.filter(
      continent=continent_type) for continent_type, _ in Country.CONTINENT_OPTION}
        
    ctx = {
            'countries' : countries,
            'continent' : continent,
    }
    return render(request,'countries/index.html',context=ctx)

def search_feature(request):

    if request.method == 'POST':
        search_query = request.POST['search_query']
        posts = Country.objects.filter(nation__icontains=search_query)
        return render(request, 'countries/query_result.html', {'query': search_query, 'posts':posts})
    else:
        return render(request, 'countries/query_result.html', {'query': search_query})
