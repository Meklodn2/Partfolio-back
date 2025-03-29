from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    messages = models.TextField()
    date_contacted = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_contacted']
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'

    def __str__(self):
        return f"{self.name} - {self.email}"
    