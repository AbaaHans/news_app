
import django
from django.shortcuts import render
from django.core.mail import send_mail
from django.contrib import messages
from .models import News, Category, Comment


# Create your views here.
def home(request):
    premiere_news= News.objects.first()
    troisieme_news=News.objects.all()[0:2]
    three_category=Category.objects.all()

    return render(request, 'index.html',
    {'premiere_news':premiere_news,
    'troisieme_news':troisieme_news,
    'three_category':three_category}) 

#Toutes les news

def All_new(request):
    all_news=News.objects.all()
    return render(request, 'all-news.html', {'all_news':all_news})  


#détails

def Detail(request,id):
    news=News.objects.get(pk=id)
    if request.method == 'POST':
        name=request.POST['name']
        email=request.POST['email']
        comment=request.POST['message']
        Comment.objects.create( news=news, name=name, email=email, comment=comment )
        messages.success(request, 'Votre commentaire a bien été soumis.')
    category_create=news.category_create.id
    rel_art = News.objects.filter(category_create=category_create)
    comments=Comment.objects.filter(news=news,status=False).order_by('-id')
    return render(request, 'detail.html',
    {'articles':news,
    'art':rel_art,
    'comments':comments})


#toutes les catégoris

def All_category(request):
    cats=Category.objects.all()

    return render(request, 'categories.html',
    {'cats':cats})


def Categorie_infos(request,id):
    category_create =Category.objects.get(pk=id)
    articles=News.objects.filter(category_create=category_create)
    return render(request, 'categorie-info.html',
    {'cat_info':articles,
    'category':category_create})


def Contact(request):
    # if request.method == 'POST':
    #     fname= request.POST['fullname']
    #     phone= request.POST['phone'],
    #     email= request.POST['email'],
    #     subject= request.POST['subject'],
    #     message=request.POST['message'],
    #     data ={
    #         'fname':fname,
    #         'phone': phone,
    #         'email':email,
    #         'subject':subject,
    #         'message':message
    #     }
    #     message = '''
    #     New message: {}

    #     From: {}
    #     '''.format(data['message'], data['email'])
    #     send_mail(data['subject'], message, '', ['brownshans@gmail.com'])
    return render(request, 'contact.html',{})