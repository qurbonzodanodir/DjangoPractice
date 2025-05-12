from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.template.loader import render_to_string


menu = ["About us", "Add article", "Feedback", "Login", "Logout"]

class MyClass:
    def __init__(self,a,b):
        self.a = a
        self.b = b


def index(request):
    data = {
        'title':'Home Page',
        'menu': menu,
        'float':28.54,
        'lst':[1,2,3,'abc',True],
        'set':{1,2,3,4,5},
        'dict':{'name':'Vlad', 'age': 25},
        'obj': MyClass(10, 20),
        }
    return render(request,'women/index.html',context=data)




def about(request):
    return render(request,'women/about.html',{'title':'About Page'})



def archive(request,year):
    if year > 2023:
        return redirect('/')



def categories(request,cat_id):
    return HttpResponse(f"<h1>Hello, You're at categories page Women</h1> <p> Category ID:{cat_id}</p>")


def categories_by_slug(request,cat_slug):
    if request.GET:
        print(request.GET)
    return HttpResponse(f"<h1>Hello, You're at categories by slag page </h1> <p> Category Slug:{cat_slug}</p>")