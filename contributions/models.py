from django.db import models


class Neighbor(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.name


class Contribution(models.Model):
    neighbor = models.ForeignKey(Neighbor, on_delete=models.CASCADE, related_name='contributions')
    date = models.DateField(auto_now_add=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.neighbor.name} - {self.amount} on {self.date}'
