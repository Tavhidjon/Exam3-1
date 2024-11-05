from django.db import models
from django.contrib.auth.models import User


class Movie(models.Model):
    name=models.CharField(max_length=250)
    show_time=models.DateTimeField(auto_now=True)
    deadline=models.BooleanField(default=True)
    is_active=models.BooleanField(default=True)
    price=models.IntegerField()
    video=models.FileField(upload_to="static/images")
    description=models.TextField()

    def __str__(self):
        return self.name
    


class Category(models.Model):
    name=models.CharField(max_length=100)
    movie_id=models.ForeignKey(Movie,on_delete=models.CASCADE)
    def __str__(self):
        return self.name






class Show(models.Model):
    address=models.CharField(max_length=250)
    category_id=models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.address
    



class Order(models.Model):
    PAY=(
        ('card','Card'),
        ('cash','cash')
    )
    show_id=models.ForeignKey(Show, on_delete=models.CASCADE)
    user_id=models.ForeignKey(User, on_delete=models.CASCADE)
    when_ordered=models.DateTimeField(auto_now=True)
    amount=models.IntegerField()
    paying_by=models.CharField(choices=PAY,max_length=255)

    def __str__(self):
        return self.when_ordered
    









    


