from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import properties_detail, properties_image, wishlist
from .forms import intrested_user_form
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

# Create your views here.


def index(request):
    context = {}
    properties = properties_detail.objects.all()
    context['properties'] = properties
    context['title'] = "Home"
    return render(request, 'mainapp/index.html', context)
    

def properties(request):
    context = {}
    # property_id = request.GET.get('id')
    # properties = properties_detail.objects.get(id=property_id)
    # properties_img = properties.properties_img.all()
    # user_form = intrested_user_form()
    # if request.method == 'POST':
    #     user_form = intrested_user_form(request.POST)
    #     if user_form.is_valid():
            
    #         user = user_form.save(commit=False)
    #         user.pd = properties
    #         user.save()
    #         return redirect('index')
            
    # context["user_form"] = user_form
    # context["title"] = properties.area
    # context["properties_images"] = properties_img
    # context["properties_detail"] = properties

    properties = properties_detail.objects.all()
    numbered_property = properties.filter(numbered_property=True).order_by('property_number').values()
    # print(numbered_property)
    # filtered_properties = False

    if request.method == "GET":
        property_type = request.GET.get('type')
        district = request.GET.get('district')
        if property_type == "residential":
            filtered_properties = properties.filter(residential_property=True)
            context["Title"] = 'Residential'
            context["is_search"] = True
        elif property_type == "commercial":
            filtered_properties = properties.filter(commercial_property=True)
            context["Title"] = 'Commercial'
            context["is_search"] = True

        elif property_type == "our_projects":
            filtered_properties = properties.filter(our_property=True)
            context["Title"] = 'Our Projects'
            context["is_search"] = False

        else:
            filtered_properties = None

        
        if district:
            districtLo=district.lower()
            filtered_properties = filtered_properties.filter(district=districtLo)

        context["property_type"] = property_type
        context["district"] = district

        context["properties"] = filtered_properties
        # context[""]
    # context["residential"] = residential
    # context["our_projects"] = our_projects
    # context["commercial"] = commercial

    return render(request, 'mainapp/properties.html', context)

def property(request):
    context = {}
    property_id = request.GET.get('id')
    properties = properties_detail.objects.get(id=property_id)
    if request.user.is_authenticated:
        is_user_wishlist =  wishlist.objects.filter(user_property=properties).filter(user = request.user)
        if is_user_wishlist.count() != 0:
            property_wishlisted = True
        else:
            property_wishlisted = False
        context['property_wishlisted'] = property_wishlisted
        
    properties_img = properties.properties_img.all()
    user_form = intrested_user_form()
    if request.method == 'POST':
        user_form = intrested_user_form(request.POST)
        if user_form.is_valid():
            
            user = user_form.save(commit=False)
            user.pd = properties
            user.save()
            # return redirect('')
            
    context["user_form"] = user_form
    context["title"] = properties.area
    context["properties_images"] = properties_img
    context["properties_detail"] = properties

    return render(request, 'mainapp/property.html', context)


@login_required(login_url='login')
def add_wishlist(request, property_id):
    user_property = properties_detail.objects.get(id=property_id)
    user = request.user
    new_wishlist = wishlist.objects.create(
            user=user, user_property=user_property
    )
    new_wishlist.save()
    return redirect('index')

def get_wishlists(request):
    wishlists = wishlist.objects.filter(user=request.user)
    context = {'wishlists': wishlists}
    return render(request, 'mainapp/wishlists.html', context)

def about(request):
    return HttpResponse("About")

def contact(request):
    return HttpResponse("Contact")

def loginPage(request):
    page = 'login'
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            print('login failed')


    return render(request, 'mainapp/login_register.html', {'page':page})

def logoutPage(request):
    logout(request)
    return redirect('index')

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            
            login(request, user)
            return redirect('index')
            
    page = 'register'
    form = UserCreationForm()
    context = {'form': form, 'page':page}
    return render(request, 'mainapp/login_register.html', context)


