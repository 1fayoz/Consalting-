from django.shortcuts import render
from .models import Contact_info,Picture, About, Offer, Result, Servies, Blog, Projcet,Register, Blog, Feedback,AboutUs, Enter
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage



def home(request):
    contact_info = Contact_info.objects.last()
    picture = Picture.objects.all()
    about = About.objects.last()
    offer = Offer.objects.all()
    result = Result.objects.last()
    servies = Servies.objects.all()
    project = Projcet.objects.all()
    blogs = Blog.objects.all()
    feedback = Feedback.objects.all()

    if request.method == 'POST':
        print(request.POST) 
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        select = request.POST.get('select')
        phone_number = request.POST.get('phone_number')
        message = request.POST.get('message')

        Register.objects.create(
            full_name = first_name,
            last_name = last_name,
            phone = phone_number,
            select = select,
            message = message
        )

    if request.method == "POST":
        print(request.POST)
    
    P = Paginator(blogs, 2)
    page_number = request.GET.get('page')
    try:
        page_obj = P.get_page(page_number)
    except PageNotAnInteger :
        page_obj = P.page(1)
    except EmptyPage:
        page_obj = P.page(P.num_pages)
    # context = {"page_obj": pag/e_obj}

    return render(request, 'index.html', { 'contact_info':contact_info,
                                          'picture': picture,
                                          'about':about,
                                          'offer': offer,
                                          'result':result,
                                          'servies':servies,
                                          'project':project,
                                          'blogs': page_obj,
                                          'feedback': feedback
                                            })

    

def about(request):
    abouts = About.objects.last()
    contact_info = Contact_info.objects.last()
    aboutus = AboutUs.objects.last()
    enter = Enter.objects.last()
    result = Result.objects.last()
    feedback = Feedback.objects.all()
    blogs = Blog.objects.all()
    
    P = Paginator(blogs, 2)
    page_number = request.GET.get('page')
    try:
        page_obj = P.get_page(page_number)
    except PageNotAnInteger :
        page_obj = P.page(1)
    except EmptyPage:
        page_obj = P.page(P.num_pages)


    return render(request, 'about.html',{
        'about':abouts,
        'contact_info':contact_info,
        'aboutus':aboutus,
        'enter':enter,
        'result':result,
        'feedback': feedback,
        'blogs': page_obj,

    })

def project(request):
    projects = Offer.objects.all()
    return render(request, 'project.html')

def servis(request):
    servises = Servies.objects.all()
    return render(request, 'services.html')

def blog(request):
    blogs = Blog.objects.all()
    contact_info = Contact_info.objects.last()
    P = Paginator(blogs, 2)
    page_number = request.GET.get('page')
    try:
        page_obj = P.get_page(page_number)
    except PageNotAnInteger :
        page_obj = P.page(1)
    except EmptyPage:
        page_obj = P.page(P.num_pages)
    # context = {"page_obj": pag/e_obj}
    return render(request, 'blog.html',{
        'contact_info':contact_info,
        'blogs':page_obj

    })

def contact(request):
    contact_info = Contact_info.objects.last()
    return render(request, 'contact.html', {'contact_info':contact_info})
