from rest_framework import serializers
from .models import Foydalanuvchi,Category,Mahsulotlar, Order


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model=Foydalanuvchi
        fields='__all__'

# 
class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields='__all__'
# 
class MahsulotlarSerializers(serializers.ModelSerializer):
    class Meta:
        model=Mahsulotlar
        fields='__all__'
    def to_representation(self, instance):
            rep = super(MahsulotlarSerializers, self).to_representation(instance)
            rep['category'] = instance.category.name
            return rep

class OrderSerializers(serializers.ModelSerializer):
    class Meta:
        
        model=Order
        fields=['user','product','quantity','all','product_id']
    def to_representation(self, instance):
            rep = super(OrderSerializers, self).to_representation(instance)
            rep['product'] = instance.product.name
            return rep
