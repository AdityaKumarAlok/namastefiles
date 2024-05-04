from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import FileResponse
from django.utils.encoding import smart_str
from .models import ConverterUploadedFile
from .forms import UploadedFileForm
from pdf2docx import Converter
from docx2pdf import convert
from csv2pdf import convert as csvConverter
import os
from .controlers.FileControler import convert_image,resize_image_to_filesize,pdf_to_jpg_and_zip

@api_view(['POST'])
def pdftoword(request):
        form = UploadedFileForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES['file']
            file_name = (os.path.splitext(uploaded_file.name)[0]+".docx")
            pdf_location = "uploads/"+ uploaded_file.name.replace(' ', '_')
            docx_location = "uploads/docx_file/"+file_name
            ConverterUploadedFile.objects.create(file=uploaded_file)
            cv = Converter(pdf_location)
            cv.convert(docx_location)
            cv.close()
            response = FileResponse(open(docx_location, 'rb'))
            response['Content-Disposition'] = 'attachment; filename={}'.format(smart_str(docx_location))
            return response 
    
@api_view(['POST'])
def docxtopdf(request):
        form = UploadedFileForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES['file']
            file_name = (os.path.splitext(uploaded_file.name)[0]+".pdf")
            docx_location = "uploads/"+ uploaded_file.name.replace(' ', '_')
            pdf_location = "uploads/pdf_file/"+file_name
            print(pdf_location)
            ConverterUploadedFile.objects.create(file=uploaded_file)
            convert(docx_location, pdf_location)
            response = FileResponse(open(pdf_location, 'rb'))
            response['Content-Disposition'] = 'attachment; filename={}'.format(smart_str(pdf_location))
            return response 
        
@api_view(['POST']) 
def csvtopdf(request):
        form = UploadedFileForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES['file']
            file_name = (os.path.splitext(uploaded_file.name)[0]+".pdf")
            docx_location = "uploads/"+ uploaded_file.name.replace(' ', '_')
            pdf_location = "uploads/pdf_file/"+file_name
            print(pdf_location)
            ConverterUploadedFile.objects.create(file=uploaded_file)
            csvConverter(docx_location, pdf_location)
            response = FileResponse(open(pdf_location, 'rb'))
            response['Content-Disposition'] = 'attachment; filename={}'.format(smart_str(pdf_location))
            return response 
    
@api_view(['POST'])
def pngtojpg(request):
        form = UploadedFileForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES['file']
            file_name = (os.path.splitext(uploaded_file.name)[0]+".jpg")
            png_location = "uploads/"+ uploaded_file.name.replace(' ', '_')
            jpg_location = "uploads/jpg_file/"+file_name
            ConverterUploadedFile.objects.create(file=uploaded_file)
            convert_image(png_location,jpg_location)
            response = FileResponse(open(jpg_location, 'rb'))
            response['Content-Disposition'] = 'attachment; filename={}'.format(smart_str(jpg_location))
            return response 
    
@api_view(['POST'])
def jpgtopng(request):
        form = UploadedFileForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES['file']
            file_name = (os.path.splitext(uploaded_file.name)[0]+".png")
            jpeg_location = "uploads/"+ uploaded_file.name.replace(' ', '_')
            png_location = "uploads/png_file/"+file_name
            ConverterUploadedFile.objects.create(file=uploaded_file)
            convert_image(jpeg_location,png_location)
            response = FileResponse(open(png_location, 'rb'))
            response['Content-Disposition'] = 'attachment; filename={}'.format(smart_str(png_location))
            return response 

@api_view(['POST'])   
def jpgtowebp(request):
        form = UploadedFileForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES['file']
            file_name = (os.path.splitext(uploaded_file.name)[0]+".webp")
            jpeg_location = "uploads/"+ uploaded_file.name.replace(' ', '_')
            webp_location = "uploads/webp_file/"+file_name
            ConverterUploadedFile.objects.create(file=uploaded_file)
            convert_image(jpeg_location,webp_location)
            response = FileResponse(open(webp_location, 'rb'))
            response['Content-Disposition'] = 'attachment; filename={}'.format(smart_str(webp_location))
            return response 

@api_view(['POST'])   
def webptojpg(request):
        form = UploadedFileForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES['file']
            file_name = (os.path.splitext(uploaded_file.name)[0]+".jpg")
            webp_location = "uploads/"+ uploaded_file.name.replace(' ', '_')
            jpg_location = "uploads/jpg_file/"+file_name
            ConverterUploadedFile.objects.create(file=uploaded_file)
            convert_image(webp_location,jpg_location)
            response = FileResponse(open(jpg_location, 'rb'))
            response['Content-Disposition'] = 'attachment; filename={}'.format(smart_str(jpg_location))
            return response 

@api_view(['POST'])   
def webptopng(request):
        form = UploadedFileForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES['file']
            file_name = (os.path.splitext(uploaded_file.name)[0]+".png")
            webp_location = "uploads/"+ uploaded_file.name.replace(' ', '_')
            png_location = "uploads/png_file/"+file_name
            ConverterUploadedFile.objects.create(file=uploaded_file)
            convert_image(webp_location,png_location)
            response = FileResponse(open(png_location, 'rb'))
            response['Content-Disposition'] = 'attachment; filename={}'.format(smart_str(png_location))
            return response 
@api_view(['POST'])   
def pngtowebp(request):
        form = UploadedFileForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES['file']
            file_name = (os.path.splitext(uploaded_file.name)[0]+".webp")
            png_location = "uploads/"+ uploaded_file.name.replace(' ', '_')
            webp_location = "uploads/png_file/"+file_name
            ConverterUploadedFile.objects.create(file=uploaded_file)
            convert_image(png_location,webp_location)
            response = FileResponse(open(webp_location, 'rb'))
            response['Content-Disposition'] = 'attachment; filename={}'.format(smart_str(webp_location))
            return response 
@api_view(['POST'])   
def imagecompress(request):
        form = UploadedFileForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES['file']
            sizeData = int(request.data.get('size'))
            imageFormat = request.data.get('format')
            file_name = (os.path.splitext(uploaded_file.name)[0]+imageFormat)
            input_location = "uploads/"+ uploaded_file.name.replace(' ', '_')
            output_location = "uploads/compresed_file/"+file_name
            ConverterUploadedFile.objects.create(file=uploaded_file)
            resize_image_to_filesize(input_location,output_location,sizeData)
            response = FileResponse(open(output_location, 'rb'))
            response['Content-Disposition'] = 'attachment; filename={}'.format(smart_str(output_location))
            return response 
@api_view(['POST'])   
def pdftojpg(request):
        form = UploadedFileForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES['file']
            file_name = str(os.path.splitext(uploaded_file.name)[0])
            input_location = "uploads/"+ uploaded_file.name.replace(' ', '_')
            output_location = "uploads/compresed_file/zipping"
            ConverterUploadedFile.objects.create(file=uploaded_file)
            zip_name = pdf_to_jpg_and_zip(input_location,output_location)
            response = FileResponse(open(zip_name, 'rb'))
            response['Content-Disposition'] = 'attachment; filename={}'.format(smart_str(zip_name))
            return response 
            
