from django.db import models

class Home(models.Model):
    
    logo = models.CharField(max_length=50)
    login = models.CharField(max_length=20)
    text = models.CharField(max_length=70)
    link = models.CharField(max_length=80)
    brend = models.CharField(max_length=90)
    
    
    def __str__(self):
        return self.login
        return self.logo
        return self.text
        return self.link
        return self.brend
     
