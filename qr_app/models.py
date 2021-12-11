from django.db import models

# Create your models here.
class Attendance (models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    url = models.CharField(max_length=250)
    qr_code = models.ImageField(upload_to='images/')


    def __str__(self):
        return str(self.name)
    