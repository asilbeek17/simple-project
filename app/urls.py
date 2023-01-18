from django.urls import path
from app.views import *

urlpatterns = [
    path('post/<int:pk>/delete/', BlogDeleteView.as_view(), name='post_delete'),
    path('post/<int:pk>/edit/', BlogUpdateView.as_view(), name='post_edit'),
    # path('post/new/', BlogCreatview.as_view(), name='post_new'),
    path('', BlogListView.as_view(), name='home'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
    path('others/', others, name='others'),
    path('calculator/', CalculatorView, name='calculator'),
    path('registered/', RegisterePeople.as_view(), name='registered'),
    path('create/', create_product, name='create'),
    # path('forgot-password/', ForgotPasswordView.as_view(), name='forgot-password'),
]