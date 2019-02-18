from .models import Wine
from django.shortcuts import render
from .filters import WineFilter

def search(request):
    if request.method == 'GET':
        wine_list = Wine.objects.all()
        wine_filter = WineFilter(request.GET, queryset=wine_list)
        return render(request, 'wine.html', {'filter':wine_filter})




