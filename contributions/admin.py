from django.contrib import admin
from .models import Contribution, Neighbor


@admin.register(Neighbor)
class NeighborAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone']


@admin.register(Contribution)
class ContributionAdmin(admin.ModelAdmin):
    list_display = ['neighbor', 'amount', 'date']
    list_filter = ['date']
