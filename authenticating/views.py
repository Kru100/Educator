from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import *
from .emails import *

class registerAPI(APIView):
    def post(self, request):
        try:
            data = request.data
            serializer = UserSerializer(data = data)
            if serializer.is_valid():                
                serializer.save()
                OTP_email(serializer.data['email'])
                
                return Response({
                    'status': 200,
                    'message': 'Successfully registered',
                    'data': serializer.data,
                    
                })
            
            return Response({
                    'status': 400,
                    'message': 'Something is wrong',
                    'data': serializer.errors,
                    
                })  
            
        except Exception as e:
            print(e)
              
class verificationAPI(APIView):
    
    def post(self, request):
        try:
            data = request.data
            serializer = VerifiedUserSerializer(data = data)
            if serializer.is_valid():   
                email = serializer.data['email']
                OTP = serializer.data['OTP']
                user = User.objects.filter(email = email)                         
            
                try:
                    if not user.exists():                    
                        return Response({
                        'status': 400,
                        'message': 'Invalid Email',
                        'data': serializer.data,
                        })     
                except Exception as e:
                    print(e)           
                print(1)    
                if user[0].otp != OTP:
                    return Response({
                    'status': 400,
                    'message': 'Wrong OTP',
                    'data': {},
                })
                
                
                user[0].is_verified = True
                user[0].save()
                    
                return Response({
                    'status': 200,
                    'message': 'Successfully registered',
                    'data': serializer.data,
                    
                })
            return Response({
                    'status': 400,
                    'message': 'Something is wrong',
                    'data': serializer.errors,                    
                })  
                
                
        except Exception as e:
            print(e)
            
# class LoginAPI(APIView):
    
#     def post(self, request):
#         try:
#             data = request.data
#             serializer = LoginSeri(data = data)
#             if serializer.is_valid():
#                 email = serializer.data['email']
#                 password = serializer.data['password']
                
#             return Response({
#                     'status': 400,
#                     'message': 'Something is wrong',
#                     'data': serializer.errors,                    
#                 })  
#         except Exception as e:
#             print(e)
