from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import properties_detail, properties_image
from .forms import intrested_user_form


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
    properties_img = properties.properties_img.all()
    user_form = intrested_user_form()
    if request.method == 'POST':
        user_form = intrested_user_form(request.POST)
        if user_form.is_valid():
            
            user = user_form.save(commit=False)
            user.pd = properties
            user.save()
            return redirect('index')
            
    context["user_form"] = user_form
    context["title"] = properties.area
    context["properties_images"] = properties_img
    context["properties_detail"] = properties

    return render(request, 'mainapp/property.html', context)

def wishlist(request):
    return HttpResponse("Wishlist")

def about(request):
    return HttpResponse("About")

def contact(request):
    return HttpResponse("Contact")
