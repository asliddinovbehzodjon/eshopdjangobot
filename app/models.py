from django.db import models

# Create your models here.
class Foydalanuvchi(models.Model):
    name=models.CharField(max_length=500,null=True,blank=True)
    t_id=models.IntegerField(unique=True,null=True,blank=True)
    language=models.CharField(max_length=10,default='uz')
    phone=models.CharField(unique=True,null=True,blank=True,max_length=400)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name='Foydalanuvchi  '
        verbose_name_plural='Foydalanuvchilar  '
class Category(models.Model):
    name=models.CharField(max_length=400)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name='Kategoriya  '
        verbose_name_plural='Kategoriyalar  '
class Mahsulotlar(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    name=models.CharField(max_length=400)
    cost=models.IntegerField()
    image=models.ImageField(upload_to='products')
    desc=models.TextField()
    def __str__(self):
        return self.name
    class Meta:
        verbose_name='Mahsulot  '
        verbose_name_plural='Mahsulot   '

class Order(models.Model):
        user=models.ForeignKey(Foydalanuvchi,on_delete=models.CASCADE)
        product=models.ForeignKey(Mahsulotlar,on_delete=models.CASCADE)
        quantity=models.IntegerField()
        create_at=models.DateTimeField(auto_now_add=True)
        def __str__(self):
            return self.user.name
        @property
        def cost(self):
            return self.product.cost
        @property
        def product_id(self):
            return self.product.id
        @property
        def all(self):
            total= self.product.cost * self.quantity
            return total
