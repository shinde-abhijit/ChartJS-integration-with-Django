from django.db import models

# Create your models here.
class CountryPopulation(models.Model):
    country_name = models.CharField(max_length=100)
    population = models.PositiveIntegerField()

    class Meta:
        verbose_name="Country Population"
        verbose_name_plural="Country Population"
    
    def __str__(self):
        return self.country_name