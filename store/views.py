

# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CategorySerializer, ProductSerializer

def home(request):
    return render(request, 'home.html')

def category_page(request, id):
    category = get_object_or_404(Category, id=id)
    products = Product.objects.filter(category=category)
    return render(request, 'category.html', {'category': category, 'products': products})

@api_view(['GET'])
def category_list(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def products_by_category(request, id):
    products = Product.objects.filter(category_id=id)
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)
