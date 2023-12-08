from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from controller.models import Relay,Admin,Data
from datetime import datetime,timedelta
import firebase_admin
from firebase_admin import credentials,messaging

class UpdateRelay(APIView):
    def post(self, request):
        try:
            gId=request.POST.get('Id',None)
            gValue=request.POST.get('Value',None)
            r=Relay.objects.filter(Id=gId).first()
            if(r!=None):
                r.Value=gValue
                r.save()
                return Response({'Response': 'Success'})
            return Response({'Response': 'Not Exist'})
        except:
            return Response({'Response': 'Failed'})

class GetRelay(APIView):
    def post(self, request):
        try:
            gId=request.POST.get('Id',None)
            gValue=request.POST.get('Value',None)
            r=Relay.objects.filter(Id=gId).first()
            if(r!=None):
                return Response({'Response': 'Success',"Relay":r.Value})
            return Response({'Response': 'Not Exist'})
        except:
            return Response({'Response': 'Failed'})

class Login(APIView):
    def post(self, request):
        try:
            gUsername=request.POST.get('Username',None)
            gPassword=request.POST.get('Password',None)
            gToken=request.POST.get('Token',None)
            a=Admin.objects.filter(Username=gUsername).first()
            if(a!=None):
                a=Admin.objects.filter(Username=gUsername,Password=gPassword).first()
                if(a!=None):
                    a.Token=gToken
                    a.save()
                    return Response({'Response': 'Success'})
                return Response({'Response': 'Password Incorrect'})
            return Response({'Response': 'Not Exist'})
        except:
            return Response({'Response': 'Failed'})
        
class InsertData(APIView):
    def post(self, request):
        try:
            gTension=request.POST.get('Tension',0)
            gCourant=request.POST.get('Courant',0)
            gPuissance=request.POST.get('Puissance',0)
            gEnergie=request.POST.get('Energie',0)
            gPrice=request.POST.get('Price',0)
            Data.objects.create(Tension=gTension,Courant=gCourant,Puissance=gPuissance,Energie=gEnergie,Price=gPrice)
            return Response({'Response': 'Success'})
        except:
            return Response({'Response': 'Failed'})
        
class GetAllData(APIView):
    def post(self, request):
        try:
            dateStart = request.POST.get('date_Start', datetime.now())#yyyy-MM-dd kk:mm __range
            dateEnd = request.POST.get('date_End', (datetime.now() - timedelta(days=90)))#yyyy-MM-dd kk:mm
            d=Data.objects.filter(Temps__range=(dateStart,dateEnd)).all()
            serialized_obj = serializers.serialize('json',d)
            return Response({'Response': 'Success',"Data":serialized_obj})    
        except:
            return Response({'Response': 'Failed'})
           