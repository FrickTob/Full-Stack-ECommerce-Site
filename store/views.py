from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from store.models import Product
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ProductSerializer

def index(request):
    return HttpResponse("Hello World. You're at the polls index.")

@api_view(['GET'])
def getProducts(request):
    searchString = request.query_params.get('search').lower()
    products = Product.objects.all()
    products = filter(lambda x : searchString in x.product_title.lower(), products)
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getProduct(request, pk):
    product = Product.objects.get(id=pk)
    serializer = ProductSerializer(product)
    return Response(serializer.data)

@api_view(['PUT'])
def removeProduct(request, pk):
    numToRemove = request.data
    product = Product.objects.get(id=pk)
    if product.product_quantity >= numToRemove:
        product.product_quantity -= numToRemove
        product.save()
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    return Response("Not Enough in Stock")

@api_view(['PUT'])
def addProduct(request, pk):
    numToAdd = request.data
    product = Product.objects.get(id=pk)
    product.product_quantity += int(numToAdd)
    product.save()
    serializer = ProductSerializer(product)
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteProduct(request, pk):
    product = Product.objects.get(id=pk)
    product.delete()
    return Response("Delete Success")
