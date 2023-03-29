from django.shortcuts import render

# Create your views here.

from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.views import APIView

# @api_view(['GET'])
# def home(request):
#     student_objs = Student.objects.all()
#     serializer = StudentSerializer(student_objs , many=True)
#     return Response({"status":200,"payload": serializer.data})

# @api_view(['POST'])
# def post_student(request):
#     data = request.data

#     serializer = StudentSerializer(data=request.data)

#     if not serializer.is_valid():
#         print(serializer.errors)
#         return Response({'status':403, 'error':serializer.errors , 'message':'Something went wrong'})

#     serializer.save()
#     print(data)
#     return Response({'status' : 200, 'payload' : data, 'message' : 'you sent'})

# @api_view(['PUT','PATCH'])
# def update_student(request, id):
#     try:
#         student_obj = Student.objects.get(id=id)

#         serializer = StudentSerializer(student_obj , data =request.data, partial = True)
#         if not serializer.is_valid():
#             print(serializer.errors)
#             return Response({'status':403, 'error':serializer.errors , 'message':'Something went wrong'})
        
#         serializer.save()
#         print(serializer.data)
#         return Response({'status' : 200, 'payload' : serializer.data, 'message' : 'you sent'})
    
#     except Exception as e:
#         print(e)
#         return Response({'status':403,'message':'invalid id'})
    
# @api_view(['DELETE'])
# def delete_student(request,id):
#     try:
#         student_obj = Student.objects.get(id=id)
#         student_obj.delete()
#         return Response({'status' : 200, 'message' : 'deleted'})
#     except Exception as e:
#         print(e)
#         return Response({'status' : 403, 'message' : 'invalid_id'}) 


class StudentAPI(APIView):

    def get(self, request):
        student_objs = Student.objects.all()
        serializer = StudentSerializer(student_objs , many=True)
        return Response({"status":200,"payload": serializer.data}) 

    def post(self, request):
        data = request.data

        serializer = StudentSerializer(data=request.data)

        if not serializer.is_valid():
            print(serializer.errors)
            return Response({'status':403, 'error':serializer.errors , 'message':'Something went wrong'})

        serializer.save()
        print(data)
        return Response({'status' : 200, 'payload' : data, 'message' : 'you sent'})

    def put(self, request):
        try:
            student_obj = Student.objects.get(id=request.data['id'])

            serializer = StudentSerializer(student_obj , data =request.data, partial = True)
            if not serializer.is_valid():
                print(serializer.errors)
                return Response({'status':403, 'error':serializer.errors , 'message':'Something went wrong'})
            
            serializer.save()
            print(serializer.data)
            return Response({'status' : 200, 'payload' : serializer.data, 'message' : 'you sent'})
    
        except Exception as e:
            print(e)
            return Response({'status':403,'message':'invalid id'})  

    def patch(self, request):
        try:
            student_obj = Student.objects.get(id=request.data['id'])

            serializer = StudentSerializer(student_obj , data =request.data, partial = True)
            if not serializer.is_valid():
                print(serializer.errors)
                return Response({'status':403, 'error':serializer.errors , 'message':'Something went wrong'})
            
            serializer.save()
            print(serializer.data)
            return Response({'status' : 200, 'payload' : serializer.data, 'message' : 'you sent'})
    
        except Exception as e:
            print(e)
            return Response({'status':403,'message':'invalid id'}) 

    def delete(self, request):
        try:
            id=request.GET.get('id')
            student_obj = Student.objects.get(id=id)
            student_obj.delete()
            return Response({'status' : 200, 'message' : 'deleted'})
        except Exception as e:
            print(e)
            return Response({'status' : 403, 'message' : 'invalid_id'})  

