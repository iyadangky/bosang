from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.index, name="index"),
    path('<int:post_id>/', views.detail, name="detail"),
    path('new/', views.new, name="new"),
    path('create/', views.create, name="create"),
    path('<int:post_id>/edit/', views.edit, name="edit"),
    path('<int:post_id>/update/', views.update, name="update"),
    path('<int:post_id>/add/', views.add, name="add"),
    path('<int:post_id>/record/', views.record, name="record"),
    path('<int:post_id>/bidding/', views.bidding, name="bidding"),
    path('<int:post_id>/tender/', views.tender, name="tender"),
    path('<int:post_id>/password/', views.password, name="password"),
    path('<int:post_id>/enter/', views.enter, name="enter"),
    path('download/', views.file_download, name='file_download'),
    path('export_content/', views.export_content, name="export_content"),
]