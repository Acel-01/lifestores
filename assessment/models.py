from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100,null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    sku = models.CharField(max_length=6, null=False, blank=False)
    price = models.DecimalField(max_digits=8, decimal_places=2, null=False, blank=False)
    image = models.ImageField(upload_to='lifestores-assessment/',null=False, blank=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.sku}"

    class Meta:
        ordering = ('created',)