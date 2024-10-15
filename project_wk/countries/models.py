from django.db import models

class Country(models.Model):

    CONTINENT_OPTION = [
        ('Africa', 'Africa'),
        ('Asia', 'Asia'),
        ('Europe', 'Europe'),
        ('North America', 'North America'),
        ('Oceania', 'Oceania'),
        ('South America', 'South America'),
    ]

    nation = models.CharField(max_length=56, unique=True)
    population = models.PositiveIntegerField()
    continent = models.CharField(max_length=13, choices=CONTINENT_OPTION, null=True)
    
    class Meta:
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'

    def __str__(self):
        return '{:s}, {:s} ({:d})'.format(self.nation, self.continent, self.population)