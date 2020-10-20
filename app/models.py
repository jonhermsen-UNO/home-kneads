from django.db import models


class Species(models.Model):
    name = models.CharField(max_length=50)
    icon = models.CharField(max_length=15)
    weight_uom = models.CharField(max_length=3)

    def __str__(self):
        return "%s (%s)" % (self.name, self.weight_uom)


class Animal(models.Model):
    ordering = ['species__name', '-birth_date']

    species = models.ForeignKey(Species, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    birth_date = models.DateField()
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    adoption_fee = models.DecimalField(max_digits=5, decimal_places=2)
    is_male = models.BooleanField()
    image = models.ImageField(upload_to='animals')

    def __str__(self):
        return "%s the %s" % (self.name, self.species)
