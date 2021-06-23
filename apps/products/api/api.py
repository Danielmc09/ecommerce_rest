from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from apps.products.models import Products, Bills
from apps.products.api.serializers import ProductsSerializer, BillsSerializer

@api_view(['GET', 'POST'])
def product_api_view(request):

    # list
    if request.method == 'GET':
        # queryset
        products = Products.objects.all()
        products_serializer = ProductsSerializer(products, many=True)
        return Response(products_serializer.data, status = status.HTTP_201_CREATED)

    #create
    elif request.method == 'POST':
        products_serializer = ProductsSerializer(data = request.data)
        #validate
        if products_serializer.is_valid():
            products_serializer.save()
            return Response({'message':'Producto creado correctamente'}, status = status.HTTP_201_CREATED)
        return Response(products_serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def product_detail_api_view(request, pk=None):
    # queryset
    product = Products.objects.filter(id=pk).first()
    # validation
    if product:
        # retrieve
        if request.method == 'GET':
            product_serializer = ProductsSerializer(product)
            return Response(product_serializer.data, status = status.HTTP_200_OK)

        # update
        elif request.method == 'PUT':
            product_serializer = ProductsSerializer(product, data =  request.data)
            if product_serializer.is_valid():
                product_serializer.save()
                return Response(product_serializer.data, status = status.HTTP_200_OK)
            return Response(product_serializer.errors, status = status.HTTP_400_BAD_REQUEST)

        # delete
        elif request.method == 'DELETE':
            product.delete()
            return Response({'message':'Producto eliminado correctamente'}, status = status.HTTP_200_OK)
    else:
        return Response({'message': 'No se ha encontrado ningun producto'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def bill_api_view(request):

    # list
    if request.method == 'GET':
        # queryset
        bills = Bills.objects.all()
        bills_serializer = BillsSerializer(bills, many=True)
        return Response(bills_serializer.data, status = status.HTTP_201_CREATED)

    #create
    elif request.method == 'POST':
        bills_serializer = BillsSerializer(data = request.data)
        #validate
        if bills_serializer.is_valid():
            bills_serializer.save()
            return Response({'message':'Compra creada correctamente'}, status = status.HTTP_201_CREATED)
        return Response(bills_serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def bill_detail_api_view(request, pk=None):
    # queryset
    bills = Bills.objects.filter(id=pk).first()
    # validation
    if bills:
        # retrieve
        if request.method == 'GET':
            bills_serializer = ProductsSerializer(bills)
            return Response(bills_serializer.data, status = status.HTTP_200_OK)

        # update
        elif request.method == 'PUT':
            bills_serializer = ProductsSerializer(bills, data =  request.data)
            if bills_serializer.is_valid():
                bills_serializer.save()
                return Response(bills_serializer.data, status = status.HTTP_200_OK)
            return Response(bills_serializer.errors, status = status.HTTP_400_BAD_REQUEST)

        # delete
        elif request.method == 'DELETE':
            bills.delete()
            return Response({'message':'Compra eliminada correctamente'}, status = status.HTTP_200_OK)
    else:
        return Response({'message': 'No se ha encontrado ninguna compra'}, status=status.HTTP_400_BAD_REQUEST)