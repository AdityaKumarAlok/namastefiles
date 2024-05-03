from django.urls import path
from . import views

urlpatterns = [
    path('pdftoword/', views.pdftoword, name='pdftoword'),
    path('docxtopdf/', views.docxtopdf, name='docxtopdf'),
    path('csvtopdf/', views.csvtopdf, name='csvtopdf'),
    path('pngtojpg/', views.pngtojpg, name='pngtojpg'),
    path('jpgtopng/', views.jpgtopng, name='jpgtopng'),
    path('jpgtowebp/', views.jpgtowebp, name='jpgtowebp')
]
