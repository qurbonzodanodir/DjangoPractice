from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.template.loader import render_to_string


menu = ["About us", "Add article", "Feedback", "Login", "Logout"]

data_db =[
    {"id":1, "title":'Анджеллина Джоли', 'content':'Биография', 'is_published':True},
    {"id":2, "title":'Марго Робби', 'content':'Биография', 'is_published':False},
    {"id":3, "title":'Джулия Робертс', 'content':'Биография', 'is_published':True},
    {"id":4, "title":'Jim Carey', 'content':'Биография', 'is_published':True}
]

def index(request):
    data = {
        'title':'Home Page',
        'menu': menu,
        'posts': data_db,
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