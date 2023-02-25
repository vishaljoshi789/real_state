from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import properties_detail, properties_image, wishlist
from .forms import intrested_user_form, feedback_form
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

# Create your views here.


def index(request):
    context = {}
    properties = properties_detail.objects.all()
    numbered_property = properties.filter(numbered_property=True).order_by('property_number')
    properties = properties.filter(numbered_property=False)
    context['properties'] = properties.order_by('-id')
    context['title'] = "Home"
    context['numbered_property'] = numbered_property
    return render(request, 'mainapp/index.html', context)
    

def properties(request):
    context = {}
    properties = properties_detail.objects.all()
    if request.method == "GET":
        property_type = request.GET.get('type')
        district = request.GET.get('district')
        
        if property_type == "residential":
            filtered_properties = properties.filter(residential_property=True)
            context["Title"] = 'RESIDENTIAL PROPERTIES'
            context["is_search"] = True
            filtered_properties = filtered_properties.filter(numbered_property=False)
            numbered_property = properties.filter(numbered_property=True).order_by('property_number')
            context['numbered_property'] = numbered_property
        elif property_type == "commercial":
            filtered_properties = properties.filter(commercial_property=True)
            context["Title"] = 'COMMERCIAL PROPERTIES'
            context["is_search"] = True
            filtered_properties = filtered_properties.filter(numbered_property=False)
            numbered_property = properties.filter(numbered_property=True).order_by('property_number')
            context['numbered_property'] = numbered_property

        elif property_type == "our_projects":
            filtered_properties = properties.filter(our_property=True).order_by('-id')
            context["Title"] = 'OUR PROJECTS'
            context["is_search"] = False
            filtered_properties = filtered_properties.filter(numbered_property=False)
            numbered_property = properties.filter(numbered_property=True).order_by('property_number')
            context['numbered_property'] = numbered_property

        elif property_type == "all":
            filtered_properties = properties
            context["Title"] = 'PROJECTS'
            context["is_search"] = False
            filtered_properties = filtered_properties.filter(numbered_property=False)
            numbered_property = properties.filter(numbered_property=True).order_by('property_number')
            context['numbered_property'] = numbered_property

        else:
            filtered_properties = None

        
        if district:
            filtered_properties = filtered_properties.filter(district=district)
            print(filtered_properties)


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
    
        
    properties_img = properties.properties_img.all()
    user_form = intrested_user_form()
    if request.method == 'POST':
        if request.POST.get('type') == 'userform':
            user_form = intrested_user_form(request.POST)
            if user_form.is_valid():
                
                user = user_form.save(commit=False)
                user.pd = properties
                user.save()
            # return redirect('')
        elif request.POST.get('type') == 'wishlist':
            if request.user.is_authenticated:
                user_property = properties_detail.objects.get(id=property_id)
                user = request.user
                new_wishlist = wishlist.objects.create(
                    user=user, user_property=user_property
                )
                new_wishlist.save()
            else:
                return redirect('login')

        if request.user.is_authenticated:
            is_user_wishlist =  wishlist.objects.filter(user_property=properties).filter(user = request.user)
            if is_user_wishlist.count() != 0:
                property_wishlisted = True
            else:
                property_wishlisted = False
            context['property_wishlisted'] = property_wishlisted

            
    context["user_form"] = user_form
    context["title"] = properties.name
    context["properties_images"] = properties_img
    context["properties_detail"] = properties
    context['amenities'] = properties.other_facilities.split('\n')

    return render(request, 'mainapp/property.html', context)


# @login_required(login_url='login')
# def add_wishlist(request, property_id):
#     user_property = properties_detail.objects.get(id=property_id)
#     user = request.user
#     new_wishlist = wishlist.objects.create(
#             user=user, user_property=user_property
#     )
#     new_wishlist.save()
#     print(redirect("property")['Location']+f'?id={property_id}')
#     return redirect("property")['Location']+f'?id={property_id}'
    

@login_required(login_url="login")
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

def delete_wishlist(request, id):
    wishlist.objects.get(id=id).delete()
    return redirect('get_wishlists')

def feedback(request):
    content = {}
    form  = feedback_form()
    content['form'] = form
    if request.method == 'POST':
        form = feedback_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    return render(request, 'mainapp/feedback.html', content)


