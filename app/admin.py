from django.contrib import admin

# Register your models here.
from .models import Foydalanuvchi,Category,Mahsulotlar, Order
@admin.register(Foydalanuvchi)
class FoydalanuvchiAdmin(admin.ModelAdmin):
    list_display=['name','t_id','language']
    search_fields=['name','t_id']
# #################
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=['name']
    search_fields=['name']

# ##############
@admin.register(Mahsulotlar)
class MahsulotAdmin(admin.ModelAdmin):
    list_display=['name','cost','category']
    search_fields=['name','category']
admin.site.register(Order)
