from django.shortcuts import render
from rest_framework import viewsets
from .models import BorrowRecord
from .serializers import BorrowRecordSerializer

# Create your views here.
class BorrowRecordViewSet(viewsets.ModelViewSet):
    queryset = BorrowRecord.objects.all()
    serializer_class = BorrowRecordSerializer