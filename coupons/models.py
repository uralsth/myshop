from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Coupon(models.Model):
    code = models.CharField(max_length=50, unique=True)
    valid_form = models.DateTimeField()
    valid_to = models.DateTimeField()
    discount = models.IntegerField(validators=(MinValueValidator(0), MaxValueValidator(10)))
    active = models.BooleanField()

    def __str__(self):
        return self.code
