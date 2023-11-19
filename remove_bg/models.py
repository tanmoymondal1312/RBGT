from django.db import models

class UserSession(models.Model):
    session_key = models.CharField(max_length=50, unique=True)
    session_created_at = models.DateTimeField(auto_now_add=True)

class Images(models.Model):
    image = models.ImageField(upload_to='images/')
    session = models.ForeignKey(UserSession, on_delete=models.CASCADE, verbose_name="Related Session")

    def __str__(self):
        return f"Image associated with session: {self.session.session_key}"
