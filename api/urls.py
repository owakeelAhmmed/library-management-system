from django.urls import path, include
from rest_framework.routers import DefaultRouter
from books.views import BookViewSet, AuthorViewSet
from members.views import MemberViewSet
from borrow.views import BorrowRecordViewSet




router = DefaultRouter()
router.register(r'books', BookViewSet, basename='book')
router.register(r'authors', AuthorViewSet, basename='author')
router.register(r'members', MemberViewSet, basename='member')
router.register(r'borrow-records', BorrowRecordViewSet, basename='borrowrecord')


urlpatterns = [
    path('', include(router.urls))
]
