from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from category.serializer import CategorySerializer
from products.models import Product
from products.serializer import ProductListSerializer


class ProductList(APIView):

    def get(self, request):
        queryset = Product.objects.order_by('-id')
        serial = ProductListSerializer(queryset, many=True)
        return Response(serial.data)

    def post(self, request):
        serial = CategorySerializer(data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data, status.HTTP_200_OK)
        return Response(serial.data, status.HTTP_400_BAD_REQUEST)


class ProductDetailView(APIView):
    def get_object(self, pk):
        return get_object_or_404(Product, pk=pk)

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        serial = ProductListSerializer(self.get_object(pk))
        return Response(serial.data)

    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        serializer = ProductListSerializer(instance=self.get_object(pk), data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        serial = self.get_object(pk)
        serial.delete()
        return Response(status=status.HTTP_404_NOT_FOUND)

