from django.urls import path

from shop import views

app_name = 'shop'

urlpatterns = [
    path('', views.list_product, name='list_product'),
    path('client/', views.list_client, name='list_client'),
    path('product/create/', views.create_product, name='create_product'),
    path('client/create/', views.create_client, name='create_client'),
    path('product/<int:pk>/', views.detail_product, name='detail_product'),
    path('client/<int:pk>/', views.detail_client, name='detail_client'),
    path('<int:pk>/<int:value>/', views.change_stock, name='change_stock'),
    path('product/edit/<int:pk>', views.edit_product, name='edit_product'),
    path('client/edit/<int:pk>', views.edit_client, name='edit_client'),
    path('product/delete/<int:pk>', views.delete_product, name='delete_product'),
    path('client/delete/<int:pk>', views.delete_client, name='delete_client'),
]