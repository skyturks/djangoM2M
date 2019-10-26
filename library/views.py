from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from library.models import Library
from django.views import View
from .forms import LibraryModelForm
# Create your views here.


class Libraries(View):
    def get(self, request):
        libraries = Library.objects.all()
        context = {
            "description": "kütüphaneler",
            "libraries": libraries
        }

        print("--------")
        print(libraries)
        return render(request, "library/libraries.html", context)
    
    

class LibraryCreate(View):

    def get(self, request):
        context = {
            "description": "Library create",
            "libraryCreateForm": LibraryModelForm
        }

        return render(request, "library/library-add.html", context)

    def post(self, request):
        user = User.objects.get(id=request.POST.get('user'))
        library = Library()

        library.title = request.POST.get('title')

        library.save()

        library.user.add(user)
        
        return redirect("library:libraries")


class LibraryShow(View):
    pass