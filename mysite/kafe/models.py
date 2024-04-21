from django.db import models

class UserProfile(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    age = models.PositiveIntegerField(default=0)


class Category(models.Model):
     title = models.CharField(max_length=16, unique=True)

     def __str__(self):
         return self.title


class Food(models.Model):
    name = models.CharField(max_length=16)
    description = models.TextField()
    order = models.IntegerField(default=0, verbose_name='order')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    minutes = models.PositiveIntegerField(default=0)
    spicy = models.BooleanField(default=False, verbose_name='spicy?')
    price = models.DecimalField(max_digits=10, decimal_places=2)


    def __str__(self):
        return self.name




class Rating(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    stars = models.IntegerField(choices=[(i, str(i)) for i in range(1,6)], help_text="Rate the item with 0 to 6 stars.", verbose_name="Rating")

    def __str__(self):
        return f"{self.food} - {self.user} - {self.stars} stars"


class FoodPhoto(models.Model):
    photo = models.ImageField(upload_to="images/", blank=True, null=True)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)




class Comment(models.Model):
    author = models.CharField(max_length=16)
    text = models.TextField()
    create_time = models.DateTimeField(auto_now_add=True)
    food = models.ForeignKey(to=Food, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.author} - {self.food}'