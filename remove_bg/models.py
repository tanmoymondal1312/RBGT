from django.db import models

class UserSession(models.Model):
    session_key = models.CharField(max_length=50, unique=True)
    session_created_at = models.DateTimeField(auto_now_add=True)

class Images(models.Model):
    image = models.ImageField(upload_to='images/')
    image_name = models.CharField(max_length=100,blank=True,null=True)
    session = models.ForeignKey(UserSession, on_delete=models.CASCADE, verbose_name="Related Session")

    def __str__(self):
        return f"Image with orginal name: {self.image_name}"
