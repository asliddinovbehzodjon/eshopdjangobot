from django.urls import path
from .views import *

urlpatterns = [
    path('create/<int:id>/<str:name>',create_user),
    path('update/<int:id>/<str:lang>/<str:phone>',update_user),
    # tilni aniqlash
    path('get/lang/<int:id>',GetLang.as_view()),
    path('categories',Categories.as_view()),
    path('menu/<str:name>',Menu.as_view()),
    path('orders/<int:id>',Orders.as_view()),
    path('product/<int:id>',ProductDetail.as_view()),
    path('order/<int:t_id>/<int:id>',add_order),
    path('clear/<int:t_id>',delete_order),
    path('inc/<int:t_id>/<int:id>',inc_order),
    path('dec/<int:t_id>/<int:id>',dec_order),
    path('alluser',AllUsers.as_view())
]
