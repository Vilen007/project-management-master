from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.core.validators import MaxValueValidator, MinValueValidator


class State(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name



class Type(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name


class Access(models.Model):
    UserId = models.OneToOneField(User, on_delete=models.CASCADE)
    createproject = models.BooleanField(default=False)
    listProjet = models.BooleanField(default=False)
    accesProjet = models.BooleanField(default=False)
    detailsProjet = models.BooleanField(default=False)
    ajouterUtilisateur = models.BooleanField(default=False)

    def _str_(self):
        return str(self.UserId)


class Project(models.Model):
    userId = models.ManyToManyField(User, related_name='user_project')  # users:many2many
    name = models.CharField(max_length=50, default = "")
    state = models.ForeignKey(State, on_delete=models.SET_NULL, null=True, default='OPEN')
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    end_date = models.DateTimeField(null=True, blank=True )
    complete_per = models.FloatField(max_length=2, validators = [MinValueValidator(0), MaxValueValidator(100)], default = 0)

    # tasks/ one2many
    picture = models.ImageField()

    description = models.TextField(default='Description')

    def __str__(self):
        return self.name


class Task(models.Model):
    project_Id = models.ForeignKey(Project, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=25, null=True)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    type = models.ForeignKey(Type, on_delete=models.SET_NULL, null=True)
    state = models.ForeignKey(State, on_delete=models.SET_NULL, null=True)
    description = models.TextField(default='Description')


    # date = models.DateTimeField(default=True)
    # end_date = models.DateTimeField(default=True, blank=True)
    def __str__(self):
        return self.name


    # def _str_(self):
    #     return str(self.name)

class Info(models.Model):
    project_Id = models.ForeignKey(Project, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=25, null=True)
    port = models.IntegerField()
    #domain_name = models.URLField(max_length=200)
    version = models.CharField(max_length=200, null=True)
    type = models.CharField(max_length=200, null=True)
    backup = models.BooleanField(default=True, verbose_name="Backup")
    file = models.FileField(upload_to='upload', blank=True)
    git = models.CharField(max_length=200)
    notes = models.TextField(default='notes')

    def __str__(self):
        return self.name

class Comment(models.Model):
    # task = models.ForeignKey(Task, on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name="comments", on_delete=models.CASCADE)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}'.format(str(self.user.username))

class Commenttask(models.Model):
    # task = models.ForeignKey(Task, on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name="taskcomments", on_delete=models.CASCADE)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    task_id = models.IntegerField()

    def __str__(self):
        return '{}'.format(str(self.user.username))

    # def __str__(self):
    #     return '%s - %s' % (self.user.username, self.name)

# class TaskTm(models.Model):
#     project_Id = models.ForeignKey(Project, null=True, on_delete=models.CASCADE)
#     name = models.CharField(max_length=25, null=True)
#     created_at = models.DateTimeField(default=datetime.now, blank=True)
#     end_date = models.DateTimeField(null=True, blank=True)
#     type = models.ForeignKey(Type, on_delete=models.SET_NULL, null=True)
#     percentage = models.IntegerField()
#     description = models.TextField(default='Description')
#
#
#     # date = models.DateTimeField(default=True)
#     # end_date = models.DateTimeField(default=True, blank=True)
#     def __str__(self):
#         return self.name