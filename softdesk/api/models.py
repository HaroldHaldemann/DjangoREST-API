from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=True)


class Project(models.Model):
    BACKEND = 'BACKEND'
    FRONTEND = 'FRONTEND'
    IOS = 'IOS'
    ANDROID = 'ANDROID'
    TYPES_CHOICES = (
        (BACKEND, 'Back-end'),
        (FRONTEND, 'Front-end'),
        (IOS, 'iOS'),
        (ANDROID, 'Android')
    )

    title = models.CharField(max_length=155)
    description = models.CharField(max_length=5000)
    type = models.CharField(max_length=12, choices=TYPES_CHOICES)
    author_user_id = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )


class Contributor(models.Model):
    user_id = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    project_id = models.ForeignKey(to=Project, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('project_id', 'user_id')


class Issue(models.Model):
    LOW = 'LOW'
    MEDIUM = 'MEDIUM'
    HIGH = 'HIGH'
    PRIORITY_CHOICES = (
        (LOW, 'Low'),
        (MEDIUM, 'Medium'),
        (HIGH, 'High')
    )

    BUG = 'BUG'
    IMPROVEMENT = 'IMPROVEMENT'
    TASK = 'TASK'
    TAGS_CHOICES = (
        (BUG, 'Bug'),
        (IMPROVEMENT, 'Improvement'),
        (TASK, 'Task')
    )

    TODO = 'TODO'
    WIP = 'WIP'
    DONE = 'DONE'
    STATUS_CHOICES = (
        (TODO, 'To-do'),
        (WIP, 'WIP'),
        (DONE, 'Done')
    )

    title = models.CharField(max_length=155)
    description = models.CharField(max_length=5000)
    created_time = models.DateTimeField(auto_now_add=True)

    priority = models.CharField(max_length=12, choices=PRIORITY_CHOICES)
    tag = models.CharField(max_length=12, choices=TAGS_CHOICES)
    status = models.CharField(max_length=12, choices=STATUS_CHOICES)

    author_user_id = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='issue_author')

    assignee_user_id = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        default=author_user_id,
        related_name='issue_assignee')

    project_id = models.ForeignKey(
        to=Project,
        on_delete=models.CASCADE,
        related_name='issues'
    )


class Comment(models.Model):
    description = models.CharField(max_length=5000)
    created_time = models.DateTimeField(auto_now_add=True)

    author_user_id = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='comment_author')

    issue_id = models.ForeignKey(
        to=Issue,
        on_delete=models.CASCADE,
        related_name='comments')
