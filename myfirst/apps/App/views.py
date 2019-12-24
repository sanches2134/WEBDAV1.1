from django.http import HttpResponse,HttpResponseRedirect
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework.decorators import api_view
import os


@api_view(('GET',))
def index(request):
    We_d=os.path.dirname(os.path.realpath(__file__))
    Qe_d=We_d+request.path
    os.chdir(Qe_d)
    return(Response(os.listdir(path='.')))


def cut(url):
    lenght=len(url)
    if lenght==42:
        return(url[0:lenght-7])
    else:
        return(url[0:lenght-9])



@api_view(('GET',))
def create(request):
    Uname=request.GET.get("name")
    We_d=os.path.dirname(os.path.realpath(__file__))
    Qe_d=We_d+request.path
    os.mkdir(cut(Qe_d)+Uname)
    return(Response(os.listdir(path='.')))

@api_view(('GET',))
def delete(request):
    Uname=request.GET.get("name")
    We_d=os.path.dirname(os.path.realpath(__file__))
    Qe_d=We_d+request.path
    os.rmdir(cut(Qe_d)+Uname)
    return(Response(os.listdir(path='.')))

@api_view(('GET',))
def download(request):
    We_d=os.path.dirname(os.path.realpath(__file__))
    Qe_d=We_d+request.path
    Fname=request.GET.get("name")
    Pfile=cut(Qe_d)+Fname
    file=open(Pfile,"r")
    response=HttpResponse(file,content_type='application/msword')
    response['Content-Disposition']='attachment; filename='+Fname
    return response
   