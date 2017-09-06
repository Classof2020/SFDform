from django.db import models

# Create your models here.
class Programming_Competition(models.Model):
    full_name = models.CharField(max_length=50,verbose_name="Full Name")
    email = models.EmailField(verbose_name="Email")
    phone_no = models.IntegerField(verbose_name="Phone no.")
    programming_language = models.CharField(max_length=60,verbose_name="Programming Language")

    def __str__(self):
        return self.name

class NOSKode(models.Model):
    team_name = models.CharField(max_length=30,verbose_name="Team Name")
    total_team_members = models.IntegerField(verbose_name="Total Team members")
    team_leader = models.CharField(max_length=30,verbose_name="Team Leader")
    phone_number = models.IntegerField(verbose_name="Phone no.")
    email = models.EmailField(verbose_name="Email")
    project_title = models.CharField(max_length=50,verbose_name="Project title")
    project_description = models.TextField(verbose_name="Project Description")

    def __str__(self):
        return self.name
