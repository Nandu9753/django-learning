from home.views import index,person,UploadedImageList, UploadedImageDetail
from django.urls import path
from django.urls import path, include
from books.views import AuthorList, AuthorDetail, BookList, BookDetail
from rozarpay import views
urlpatterns = [
    path('index/', index),
    path('person/',person),
    path('authors/', AuthorList.as_view(), name='author-list'),
    path('authors/<int:pk>/', AuthorDetail.as_view(), name='author-detail'),
    path('books/', BookList.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetail.as_view(), name='book-detail'),
    path('images/', UploadedImageList.as_view(), name='image-list'),
    path('images/<int:pk>/', UploadedImageDetail.as_view(), name='image-detail'),
    path('create-razorpay-order/', views.create_razorpay_order, name='create-razorpay-order'),
    path('razorpay-payment-success/', views.razorpay_payment_success, name='razorpay-payment-success'),
]