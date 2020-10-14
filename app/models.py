from django.db import models


class Species(models.Model):
    species_name = models.CharField(max_length=50)
    weight_uom = models.CharField(max_length=3)

    def __str__(self):
        return self.species_name


class Animal(models.Model):
    species = models.ForeignKey(Species, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    birth_date = models.DateField()
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    adoption_fee = models.DecimalField(max_digits=5, decimal_places=2)
    is_male = models.BooleanField()

    def __str__(self):
        return "%s the %s" % (self.name, self.species)
