from django.db import models

class User(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    stream = models.CharField(max_length=100) # e.g. "Software Engineering", "Data Science"

    def __str__(self):
        return self.username

class Module(models.Model):
    title = models.CharField(max_length=200)
    stream = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title

class UserActivity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    activity_type = models.CharField(max_length=50) # "viewed", "completed"
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} {self.activity_type} {self.module}"
