from rest_framework.decorators import api_view,authentication_classes,permission_classes
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
# from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from home.serializers import PersonSerializer
from home.models import Person
from rest_framework import generics
from .models import UploadedImage
from .serializers import UploadedImageSerializer
from django.shortcuts import render

# Create your views here.

@api_view(['GET','POST','PUT'])

def index(request):
    if request.method == 'GET':
        course = {
            'course_name' : 'python',
            'learn'  : ['flask','django','fastApi'],
            'price' : 550
        }
    if request.method == 'POST':
        course = {
            "message" : "success"
        }    

    return Response(course)

@api_view(['GET','POST','PUT','PATCH','DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def person(request):
    try:
        if request.method == 'GET':
            person = Person.objects.all()
            serialize = PersonSerializer(person,many=True)
            return Response(serialize.data)
        if request.method == 'POST':
            data = request.data
            serialize = PersonSerializer(data = data)
            if serialize.is_valid():
                serialize.save()
                return Response({"status":200,"message":"successfull add"})
            return Response(serialize.errors)
        if request.method == 'PUT':
            data = request.data
            obj  = Person.objects.get(id=data['id'])
            serialize = PersonSerializer(obj,data = data)
            if serialize.is_valid():
                serialize.save()
                return Response({"status":200,"message":"successfull edit put method"})
            return Response(serialize.errors)
        if request.method == 'PATCH':
            data = request.data
            obj  = Person.objects.get(id=data['id'])
            serialize = PersonSerializer(obj,data = data,partial=True)
            if serialize.is_valid():
                serialize.save()
                return Response({"status":200,"message":"successfull edit patch method"})     
            return Response(serialize.errors)
        if request.method == 'DELETE':
            data = request.data
            obj = Person.objects.get(id=data['id'])
            obj.delete()       
            return Response({"status":200,"message":"successfull delete"})
    except Exception as e:
        return Response({"status":500,"message":e})
    
class UploadedImageList(generics.ListCreateAPIView):
    queryset = UploadedImage.objects.all()
    serializer_class = UploadedImageSerializer

class UploadedImageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = UploadedImage.objects.all()
    serializer_class = UploadedImageSerializer   
def index(request):
    images = UploadedImage.objects.all()
    return render(request,'index.html',{'images':images})     