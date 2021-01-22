from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *


def index(request):
    return HttpResponse("Hello!.")
# Create your views here.
class EmployeeApiView(APIView):
    def get(self,request):
        allEmployee=Employee.objects.all().values()
        return Response({"Message":"List of Employee", "Employee List":allEmployee})
def post(self,request):
    Employee.objects.create(id=request.data["id"],
                            Name=request.data["Name"],
                            Email=request.data["Email"],
                            PhoneNumber=request.data["PhoneNumber"],
                            Adhar=request.data["Adhar_card"],
                            Pan= request.data["Pan_card"],)
    Employee=Employee.objects.all().filter(id=request.data["id"]).values()
    return Response({"Message":"New Employee Added!", "Employee":Employee})
