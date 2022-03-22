
from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view

from .models import *
from .serializers import *
class AllUsers(APIView):
    def get(self,request):
            user=Foydalanuvchi.objects.all()
            serializer=UserSerializers(user,many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)


@api_view(['GET','POST'])
def create_user(request,id,name):
    user=Foydalanuvchi.objects.filter(t_id=id)
    if user.exists() is True:
        return Response({"status":':) Good'},status=status.HTTP_208_ALREADY_REPORTED)
    else:
        new=Foydalanuvchi.objects.create(t_id=id,name=name)
        new.save()
        return Response({"status":':)'},status=status.HTTP_201_CREATED)
#  Endi Foydalanuvchi tizim tilini olamiz
class GetLang(APIView):
    def get(self,request,id):
        try:
            user=Foydalanuvchi.objects.get(t_id=id)
            serializer=UserSerializers(user)
            return Response(serializer.data,status=status.HTTP_200_OK)

        except Foydalanuvchi.DoesNotExist:
            return Response(status=status.HTTP_204_NO_CONTENT)
@api_view(['GET','POST'])
def update_user(request,id,lang,phone):
    Foydalanuvchi.objects.filter(t_id=id).update(language=lang,phone=phone)
    return Response({"status":':) Good'},status=status.HTTP_208_ALREADY_REPORTED)


# 
class Categories(APIView):
    def get(self,request):
        category=Category.objects.all()
        serializer=CategorySerializers(category,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

# 
class Menu(APIView):
    def get(self,request,name):
        try:
            category=Category.objects.get(name=name)
            menu=Mahsulotlar.objects.filter(category=category)
            serializer=CategorySerializers(menu,many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)

        except Category.DoesNotExist:
            return Response(status=status.HTTP_204_NO_CONTENT)
       

# 
class Orders(APIView):
    def get(self,request,id):
        try:
            user=Foydalanuvchi.objects.get(t_id=id)
            orderlar=Order.objects.filter(user=user)
            serializer=OrderSerializers(orderlar,many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)

        except Foydalanuvchi.DoesNotExist:
            return Response(status=status.HTTP_204_NO_CONTENT)
class ProductDetail(APIView):
    def get(self,request,id):
        try:
            
            product=Mahsulotlar.objects.get(id=id)
            serializer=MahsulotlarSerializers(product)
            return Response(serializer.data,status=status.HTTP_200_OK)

        except Mahsulotlar.DoesNotExist:
            return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET','POST'])
def add_order(request,t_id,id):
    try:
            
        product=Mahsulotlar.objects.get(id=id)
        user=Foydalanuvchi.objects.get(t_id=t_id)
        if Order.objects.filter(user=user,product=product).exists():
            order=Order.objects.get(user=user,product=product)
            order.quantity=order.quantity+1
            order.save()
            
        else:
            order=Order.objects.create(user=user,product=product,quantity=1)
            return Response({'Order':"Created"},status=status.HTTP_200_OK)
        return Response({'Order':"Created"},status=status.HTTP_200_OK)
        
    except Mahsulotlar.DoesNotExist:
        return Response(status=status.HTTP_204_NO_CONTENT)
@api_view(['GET','POST'])
def delete_order(request,t_id):
    try:  
        user=Foydalanuvchi.objects.get(t_id=t_id)
        order=Order.objects.filter(user=user)
        order.delete()
        return Response({'Order':"Created"},status=status.HTTP_200_OK)
        
    except Foydalanuvchi.DoesNotExist:
        return Response(status=status.HTTP_204_NO_CONTENT)



@api_view(['GET','POST'])
def inc_order(request,t_id,id):
    try:  
        user=Foydalanuvchi.objects.get(t_id=t_id)
        product=Mahsulotlar.objects.get(id=id)
        order=Order.objects.get(user=user,product=product)
        order.quantity=order.quantity + 1
        order.save()
        return Response({'Order':"Added"},status=status.HTTP_200_OK)
        
    except Foydalanuvchi.DoesNotExist:
        return Response(status=status.HTTP_204_NO_CONTENT)
@api_view(['GET','POST'])
def dec_order(request,t_id,id):
    try:  
        user=Foydalanuvchi.objects.get(t_id=t_id)
        product=Mahsulotlar.objects.get(id=id)
        order=Order.objects.get(user=user,product=product)
        if order.quantity == 1:
            order.delete()
            return Response({'Order':"0"},status=status.HTTP_200_OK)
        
        else:
            order.quantity=order.quantity - 1
            order.save()
            return Response({'Order':"Ayirildi"},status=status.HTTP_200_OK)
    except Foydalanuvchi.DoesNotExist:
        return Response(status=status.HTTP_204_NO_CONTENT)



