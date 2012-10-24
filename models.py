from django.db import models

class Person(models_Model):
    first_name = models.CharField(max_lenght=50)
    last_name = models.CharField(max_lenght=50)
    email = models.EmailField(max_lenght=100)

class Anddress(model.Model):
    person = models.ForeignKey('Person', related_name='addresses')
    street_address_1 = models.CharField(max_lenght=100)
    street_address_2 = models.CharField(max_lenght=100, blank=True)
    city = models.CharField(max_lenght=100, blank=True)
    state_province = models.CharField(max_lenght=100)
    postal_code = models.CharField(max_lenght=100)
    country = models.CharField(max_lenght=2)

