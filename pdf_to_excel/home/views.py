from django.shortcuts import render,HttpResponse
from .models import FilesUpload
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
# Create your views here.
from .converter import *
from django.http import StreamingHttpResponse
from wsgiref.util import FileWrapper
import mimetypes
file=""
from django.http import HttpResponse,HttpResponseNotFound
import os
def index(request):
            
    
    return render(request,"index.html")

def convert(request):
    if request.method=='POST':
        """file2=request.FILES['document']
        
        
        document=FilesUpload(file=file2)
        document.save(file2)
        print(file2)
        #file=c(file2)
        print(file)"""
        if 'FE' in request.POST:
            file2=request.FILES['document']
        
        
            document=FilesUpload(file=file2)
            document.save(file2)
            print(file2)
            # file=c(file2)
            print(file)                    
            return render(request,"download.html")
        if 'SE' in request.POST:
            file2=request.FILES['document']
        
        
            document=FilesUpload(file=file2)
            document.save(file2)
            print(file2)
            # file=s(file2)
            print(file)                    
            return render(request,"download.html")
        if 'TE' in request.POST:
            file2=request.FILES['document']
        
        
            document=FilesUpload(file=file2)
            document.save(file2)
            print(file2)
            # file=t(file2)
            print(file)                    
            return render(request,"download.html")
        if 'TE' in request.POST:
            file2=request.FILES['document']
        
        
            document=FilesUpload(file=file2)
            document.save(file2)
            print(file2)
            # file=b(file2)
            print(file)                    
            return render(request,"download.html")
    return render(request,"convert.html")
def waprfile(request):
    

    file_location = 'pr_33.csv'

    try:    
        with open(file_location, 'r') as f:
           file_data = f.read()

        # sending response 
        response = HttpResponse(file_data, content_type='application/vnd.ms-excel')
        response['Content-Disposition'] = 'attachment; filename="pr_33.csv"'
        
        if os.path.exists("pr_33.csv"):
            os.remove("pr_33.csv")
        else:
            print("The file does not exist")
    except IOError:
        # handle file not exist case here
        response = HttpResponseNotFound('<h1>File not exist</h1>')

    return response


def download(request):
    # file1=c(file)
    response=HttpResponse(file)
    
    return render(request,"download.html")
