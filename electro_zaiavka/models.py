from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime, timedelta
from django.core.validators import MinValueValidator, MaxValueValidator


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


class Request(models.Model):
    name_required = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    start_date = models.DateField(default=datetime.now)
    end_date = models.DateField(default=datetime.now() + timedelta(days=6))
    request_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    status = models.ForeignKey(RequestStatus, on_delete=models.CASCADE)
    ratings = models.ManyToManyField(Rating, blank=True)

    def __str__(self):
        return self.description


class Comment(models.Model):
    request = models.ForeignKey(Request, on_delete=models.CASCADE)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)


class User(AbstractUser):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    image = models.ImageField(blank=True, null=True)
    requests = models.ManyToManyField('electro_zaiavka.Request', blank=True, related_name='request_users')
    work = models.BooleanField(default=False)


