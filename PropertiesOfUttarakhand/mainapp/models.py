from random import choices
from django.db import models

# Create your models here.

status_choices = (("uc", "Under Construction"),("js", "Just Launched"), ("rm", "Ready to Move"), ("so", "Sold Out"))

residential_property_type_choices = (("stdio", "Studio"), ("1bhk", "1 BHK"), ("2bhk", "2 BHK"), ("3bhk", "3 BHK"), ("house", "House"), ("villa", "Villa"), ("plots", "Plots"))

commercial_property_type_choices = (("officespace", "Office Space"), ("foodcourt", "Food Court"), ("shoppingcomplex", "Shopping Complex"), ("retailshops", "Retail Shops"), ("plots", "Plots"), ("hotel", "Hotel"))

district_choices = (("dehradun", "Dehradun"), ("haridwar", "Haridwar"), ("chamoli", "Chamoli"), ("rudraprayag", "Rudraprayag"), ("tehri", "Tehri"), ("uttarkashi", "Uttarkashi"), ("pauri", "Pauri"), ("almora", "Almora"), ("nanital", "Nanital"), ("pithoragarh", "Pithoragarh"), ("usnagar", "Udham Singh Nagar"), ("bageshwar", "Bageshwar"), ("champawat", "Champawat"))

def property_images_path(instance, filename):

    return 'images/property_image/{0}/{1}'.format(instance.pd.name, filename)

def property_poster_path(instance, filename):

    return 'images/property_image/{0}/poster/{1}'.format(instance.name, filename)


class properties_detail(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(null=True)
    poster = models.ImageField(upload_to=property_poster_path, blank=True, null=True)
    area = models.CharField(max_length=255, blank=True)
    resdential_property_type = models.CharField(max_length=255,choices=residential_property_type_choices, blank=True)
    commercial_property_type = models.CharField(max_length=255,choices=commercial_property_type_choices, blank=True)
    status = models.CharField(max_length=255,choices=status_choices, blank=True, default="rm")
    price = models.IntegerField(blank=True)
    locality = models.CharField(max_length=255, blank=True)
    district = models.CharField(max_length=255,choices=district_choices, blank=True) 
    pin_code = models.CharField(max_length=255, blank=True)
    other_amenities = models.CharField(max_length=255, blank=True)

    residential_property = models.BooleanField(default=False)
    commercial_property = models.BooleanField(default=False)
    our_property = models.BooleanField(default=False)

    owner_name = models.CharField(max_length=255, blank=True)
    owner_address = models.CharField(max_length=255, blank=True)
    owner_phone = models.CharField(max_length=255, blank=True)
    owner_discription = models.CharField(max_length=1000, blank=True)

    def __str__(self):
        return str(self.name)
    
class properties_image(models.Model):
    pd = models.ForeignKey(properties_detail, related_name='properties_img', on_delete=models.CASCADE)
    image = models.ImageField(upload_to=property_images_path, blank=True)
    img_caption = models.CharField(max_length=255, blank=True)


class intrested_user(models.Model):
    pd = models.ForeignKey(properties_detail, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=True)
    phone_no = models.IntegerField(blank=True)
    email = models.CharField(max_length=255, blank=True)
    address = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return str(self.name)