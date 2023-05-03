from django.shortcuts import render
from.models import PythonModel
from.serialization import PythonSer
from rest_framework.views import APIView,Response
from rest_framework import response,status
# Create your views here.
class PythonView(APIView):
    def get(self,r):
        pyobj=PythonModel.objects.all()
        ser=PythonSer(pyobj,many=True)
        return Response(ser.data)
    def post(self,r):
        serobj=PythonSer(data=r.data)
        if serobj.is_valid():
            serobj.save()
            return Response(serobj.data,status=status.HTTP_201_CREATED)
        return Response(serobj.errors,status=status.HTTP_400_BAD_REQUEST)
class PythonViewUpDel(APIView):
    def put(self,r,pk):
        obj=PythonModel.objects.get(pk=pk)
        serobj=PythonSer(obj,data=r.data)
        if serobj.is_valid():
            serobj.save()
            return Response(serobj.data,status=status.HTTP_201_CREATED)
        return Response(serobj.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self,r,pk):
        obj=PythonModel.objects.get(pk=pk)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
