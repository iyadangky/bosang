from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.conf import settings
from .models import Post
from django.utils import timezone
import os
# from django.contrib.auth.decorators import login_required
# import csv
# from django.contrib.admin.views.decorators import staff_member_required

# Create your views here.

def index(request):
    posts = Post.objects.all()
    context = {'posts' : posts}
    return render(request, 'posts/index.html', context)

def detail(request, post_id):
    post = Post.objects.get(id=post_id)
    context = {'post' : post}
    return render(request, 'posts/detail.html', context)

def new(request):
    return render(request, 'posts/new.html')

def create(request):
    created_at = timezone.now()
    client = request.POST.get('client')
    phoneNumber = request.POST.get('phoneNumber')
    contact = request.POST.get('contact')
    carModel = request.POST.get('carModel')
    carNumber = request.POST.get('carNumber')
    birth = request.POST.get('birth')
    trim = request.POST.get('trim')
    fuel = request.POST.get('fuel')
    driveType = request.POST.get('driveType')
    airbag = request.POST.get('airbag')
    mileage = request.POST.get('mileage')
    eventDate = request.POST.get('eventDate')
    repairCost = request.POST.get('repairCost')
    proposedCompensation = request.POST.get('proposedCompensation')
    insuranceCompany = request.POST.get('insuranceCompany')
    location = request.POST.get('location')
    others1 = request.POST.get('others1')
    others2 = request.POST.get('others2')
    others3 = request.POST.get('others3')
    note = request.POST.get('note')
    image1 = request.FILES.get('image1')
    image2 = request.FILES.get('image2')
    image3 = request.FILES.get('image3')
    image4 = request.FILES.get('image4')
    image5 = request.FILES.get('image5')
    image6 = request.FILES.get('image6')
    post = Post(created_at=created_at, client=client, phoneNumber=phoneNumber, contact=contact, carModel=carModel, carNumber=carNumber, birth=birth, trim=trim, fuel=fuel, driveType=driveType, airbag=airbag, mileage=mileage, eventDate=eventDate, repairCost=repairCost, proposedCompensation=proposedCompensation, insuranceCompany=insuranceCompany, location=location, others1=others1, others2=others2, others3=others3, note=note, image1=image1, image2=image2, image3=image3, image4=image4, image5=image5, image6=image6)
    post.save()
    context = {'post' : post}
    return render(request, 'posts/create.html', context)

def edit(request, post_id):
    post = Post.objects.get(id=post_id)
    context = {'post' : post}
    return render(request, 'posts/edit.html', context)

def update(request, post_id):
    post = Post.objects.get(id=post_id)
    post.created_at = timezone.now()
    post.client = request.POST.get('client')
    post.phoneNumber = request.POST.get('phoneNumber')
    post.contact = request.POST.get('contact')
    post.carModel = request.POST.get('carModel')
    post.carNumber = request.POST.get('carNumber')
    post.birth = request.POST.get('birth')
    post.trim = request.POST.get('trim')
    post.fuel = request.POST.get('fuel')
    post.driveType = request.POST.get('driveType')
    post.airbag = request.POST.get('airbag')
    post.mileage = request.POST.get('mileage')
    post.eventDate = request.POST.get('eventDate')
    post.repairCost = request.POST.get('repairCost')
    post.proposedCompensation = request.POST.get('proposedCompensation')
    post.insuranceCompany = request.POST.get('insuranceCompany')
    post.location = request.POST.get('location')
    post.others1 = request.POST.get('others1')
    post.others2 = request.POST.get('others2')
    post.others3 = request.POST.get('others3')
    post.note = request.POST.get('note')
    post.image1 = request.FILES.get('image1')
    post.image2 = request.FILES.get('image2')
    post.image3 = request.FILES.get('image3')
    post.image4 = request.FILES.get('image4')
    post.image5 = request.FILES.get('image5')
    post.image6 = request.FILES.get('image6')
    post.save()
    context = {'post' : post}
    return render(request, 'posts/create.html', context)

def file_download(request):
    path = request.GET['path']
    file_path = os.path.join(settings.MEDIA_ROOT, path)
 
    if  os.path.exists(file_path):
        binary_file = open(file_path, 'rb')
        response = HttpResponse(binary_file.read(), content_type="application/octet-stream; charset=utf-8")
        response['Content-Disposition'] = 'attachment; filename=' + os.path.basename(file_path)
        return response
    else:
        message = '알 수 없는 오류가 발행하였습니다.'
        return HttpResponse("<script>alert('"+ message +"');history.back()'</script>")