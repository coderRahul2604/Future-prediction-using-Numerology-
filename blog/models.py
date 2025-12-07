from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.utils.translation import gettext_lazy as _

class User(AbstractUser):
    # Add your custom fields here
    STATUS_CHOICES = (
        ('writer', 'Writer'),
        ('reader', 'Reader'),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='reader')

    # Add related_name to avoid clash with auth.User
    groups = models.ManyToManyField(
        Group,
        verbose_name=_('groups'),
        blank=True,
        related_name='blog_user_groups',
        related_query_name='user',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        related_name='blog_user_permissions',
        related_query_name='user',
        help_text=_('Specific permissions for this user.'),
    )

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=User.STATUS_CHOICES)

    def __str__(self):
        return self.user.username
