from django.db import models

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20, null=True, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)




    def __str__(self):
        return self.name
    


class Experience(models.Model):
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    start_date = models.CharField(max_length=100)
    end_date = models.CharField(max_length=100 , blank=True, null=True)
    description = models.TextField()



    def __str__(self):
        return f"{self.title} at {self.company}"
    


class Education(models.Model):
    start_year = models.IntegerField()
    end_year = models.IntegerField()
    institution = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    degree = models.CharField(max_length=255)
    field_of_study = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.institution} ({self.start_year} - {self.end_year})"