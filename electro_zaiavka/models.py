from datetime import date, timedelta

from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class RequestStatus(models.Model):
    status_name = models.CharField(max_length=100)

    def __str__(self):
        return self.status_name


class Rating(models.Model):
    value = models.PositiveIntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(5)])


class User(AbstractUser):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    image = models.ImageField(blank=True, null=True)
    work = models.BooleanField(default=False)


class Request(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name_required = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    start_date = models.DateField(default=date.today)
    end_date = models.DateField(default=date.today() + timedelta(days=6))
    request_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    status = models.ForeignKey(RequestStatus, on_delete=models.CASCADE)
    ratings = models.ForeignKey(Rating, on_delete=models.CASCADE)

    def __str__(self):
        return self.name_required


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    request = models.ForeignKey(Request, on_delete=models.CASCADE)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
