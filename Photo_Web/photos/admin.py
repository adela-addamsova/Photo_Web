from django.contrib import admin

# přidává prvky, které je dále možné spravovat v admin přihlášení stránky

from .models import Photo, Category

admin.site.register(Category)
admin.site.register(Photo)
