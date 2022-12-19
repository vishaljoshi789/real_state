from random import choices
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

status_choices = (("Under Construction", "Under Construction"),("Just Launched", "Just Launched"), ("Ready to Move", "Ready to Move"), ("Sold Out", "Sold Out"))

residential_property_type_choices = (("Studio", "Studio"), ("1 BHK", "1 BHK"), ("2 BHK", "2 BHK"), ("3 BHK", "3 BHK"), ("House", "House"), ("Villa", "Villa"), ("Plots", "Plots"))

commercial_property_type_choices = (("Office Space", "Office Space"), ("Food Court", "Food Court"), ("Shopping Complex", "Shopping Complex"), ("Retail Shops", "Retail Shops"), ("Plots", "Plots"), ("Hotel", "Hotel"))

district_choices = (("Dehradun", "Dehradun"), ("Haridwar", "Haridwar"), ("Chamoli", "Chamoli"), ("Rudraprayag", "Rudraprayag"), ("Tehri", "Tehri"), ("Uttarkashi", "Uttarkashi"), ("Pauri", "Pauri"), ("Almora", "Almora"), ("Nanital", "Nanital"), ("Pithoragarh", "Pithoragarh"), ("Udham Singh Nagar", "Udham Singh Nagar"), ("Bageshwar", "Bageshwar"), ("Champawat", "Champawat"))

def property_images_path(instance, filename):

    return 'images/property_image/{0}/{1}'.format(instance.pd.name, filename)

def property_poster_path(instance, filename):

    return 'images/property_image/{0}/poster/{1}'.format(instance.name, filename)


class properties_detail(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(null=True, blank=True)
    poster = models.ImageField(upload_to=property_poster_path, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=255,choices=status_choices, blank=True, default="Ready to Move", null=True)
    price = models.IntegerField(null=True)
    area = models.CharField(max_length=255, blank=True, null=True)
    district = models.CharField(max_length=255,choices=district_choices, blank=True, null=True) 
    pin_code = models.CharField(max_length=255, blank=True, null=True)
    other_facilities = models.TextField(blank=True, null=True)

    residential_property = models.BooleanField(default=False)
    residential_property_type = models.CharField(max_length=255,choices=residential_property_type_choices, blank=True, null=True)
    commercial_property = models.BooleanField(default=False)
    commercial_property_type = models.CharField(max_length=255,choices=commercial_property_type_choices, blank=True, null=True)
    our_property = models.BooleanField(default=True)
    out_property_type = models.CharField(max_length=255, blank=True, null=True)

    featured_property = models.BooleanField(default=False)
    
    numbered_property = models.BooleanField(default=False)
    property_number = models.IntegerField(null=True, blank=True, unique=True)

    bathroom = models.CharField(max_length=255, blank=True, null=True)
    kitchen = models.CharField(max_length=255, blank=True, null=True)
    bedroom = models.CharField(max_length=255, blank=True, null=True)


    owner_name = models.CharField(max_length=255, blank=True, null=True)
    owner_address = models.CharField(max_length=255, blank=True, null=True)
    owner_phone = models.CharField(max_length=255, blank=True, null=True)
    owner_discription = models.CharField(max_length=1000, blank=True, null=True)
    owner_discription = models.CharField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return str(self.name)
    
class properties_image(models.Model):
    pd = models.ForeignKey(properties_detail, related_name='properties_img', on_delete=models.CASCADE)
    image = models.ImageField(upload_to=property_images_path, blank=True)
    img_caption = models.CharField(max_length=255, blank=True)


class intrested_user(models.Model):
    pd = models.ForeignKey(properties_detail, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=True)
    phone_no = models.CharField(max_length=15, blank=True)
    email = models.CharField(max_length=255, blank=True)
    address = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return str(self.name)

class wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_property = models.ForeignKey(properties_detail, on_delete=models.CASCADE)

    def __str__(self):
        return self.user_property.name 


