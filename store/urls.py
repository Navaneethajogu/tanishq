from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='store-home'),
    path('category/<int:id>/', views.category_page, name='category-page'),
    path('api/categories/', views.category_list),
    path('api/category/<int:id>/products/', views.products_by_category),
    
]
