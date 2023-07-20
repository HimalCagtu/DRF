from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Item
from .serializers import ItemSerializer
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.views import APIView
# Create your views here.
@api_view(['GET'])
def list(request):
    # dics ={'name':'Amazon',
    #        'Age':243}
    items = Item.objects.all()
    serializer = ItemSerializer(items, many=True)

    return Response(serializer.data)
@api_view(['POST'])
def create(request):

    serializer = ItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response("Sucessfull")
    

@api_view(['DELETE'])
def delete(reequest, pk):
    items = Item.objects.get(id=pk)

    items.delete()
    return Response('Item deleted')
@api_view(['GET','PUT'])
def update(request, pk):

    item = Item.objects.get(id=pk)
    serializer = ItemSerializer(instance=item)

    itm = ItemSerializer(data=request.data, instance=item)
    if itm.is_valid():
        itm.save()
        return Response(itm.data, status=status.HTTP_200_OK)

    return Response(serializer.data)

@api_view(['PATCH'])
def patch(request, id):
    try:
        item = Item.objects.get(id=id)
        serializer = ItemSerializer(instance=item, data=request.data, partial=True)
        if not serializer.is_valid():
            return Response({'da':'sss'})
        serializer.save()
        return Response({'data':serializer.data, 'stauts':status.HTTP_100_CONTINUE})
    except :
        return Response({'messages':'sorry'})
# class MyAPIview(APIView):
#     authentication_classes = [JWTAuthentication]