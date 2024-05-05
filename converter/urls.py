from django.urls import path
from . import views

urlpatterns = [
    path('pdftoword/', views.pdftoword, name='pdftoword'),
    path('docxtopdf/', views.docxtopdf, name='docxtopdf'),
    path('csvtopdf/', views.csvtopdf, name='csvtopdf'),
    path('pngtojpg/', views.pngtojpg, name='pngtojpg'), #Image Converter Starts From This Line
    path('jpgtopng/', views.jpgtopng, name='jpgtopng'),
    path('jpgtowebp/', views.jpgtowebp, name='jpgtowebp'),
    path('webptojpg/', views.webptojpg, name='webptojpg'),
    path('webptopng/', views.webptopng, name='webptopng'),
    path('pngtowebp/', views.pngtowebp, name='pngtowebp'),
    path('imagecompress/', views.imagecompress, name='imagecompress'),
    path('pdftojpg/', views.pdftojpg, name='pdftojpg'),
    
]
