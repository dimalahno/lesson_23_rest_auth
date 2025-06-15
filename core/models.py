from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Администратор'),
        ('manager', 'Менеджер'),
        ('user', 'Пользователь'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='user')


class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    manager = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='managed_projects')
    members = models.ManyToManyField(User, related_name='projects')

    def __str__(self):
        return self.name


class Task(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tasks')
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
