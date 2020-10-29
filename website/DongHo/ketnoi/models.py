from django.db import models
from user.models import CustomerUser

# Create your models here.


class KetNoi(models.Model):
    user = models.ForeignKey(CustomerUser,on_delete=models.CASCADE)
    NoiDung = models.TextField(default='')
    NgayGui = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user