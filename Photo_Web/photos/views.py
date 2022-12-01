from django.shortcuts import render
from .models import Category, Photo

def home(request):
    category = request.GET.get('category')
    if category == None:
        photos = Photo.objects.all().order_by('-id')[:6]
    else:
        photos = Photo.objects.filter(category__name = category)

    categories = Category.objects.all()

    context = {'categories': categories, 'photos': photos}
    return render(request, 'photos/home.html', context)

def about(request):
    return render(request, 'photos/about.html', {'title': 'About'})

def gallery(request):
    category = request.GET.get('category')
    if category == None:
        photos = Photo.objects.all()
    else:
        photos = Photo.objects.filter(category__name=category)

    categories = Category.objects.all()

    context = {'categories': categories, 'photos': photos, 'title': 'Gallery'}
    return render(request, 'photos/gallery.html', context)

def viewPhoto(request, pk):
    photo = Photo.objects.get(id=pk)
    return render(request, 'photos/photo.html', {'photo': photo})

