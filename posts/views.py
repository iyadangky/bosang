from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.conf import settings
from .models import Post
from django.utils import timezone
import os
from django.contrib.auth.decorators import login_required
import csv
from django.contrib.admin.views.decorators import staff_member_required
from django.db.models import Q
from django.core.paginator import Paginator

# Create your views here.

def index(request):
    page = request.GET.get('page', '1')
    posts = Post.objects.all().order_by('-created_at')
    paginator = Paginator(posts, 10)
    page_obj = paginator.get_page(page)
    context = {'posts' : page_obj}
    return render(request, 'posts/index.html', context)

@login_required
def detail(request, post_id):
    post = Post.objects.get(id=post_id)
    context = {'post' : post}
    return render(request, 'posts/detail.html', context)

def new(request):
    return render(request, 'posts/new.html')

def create(request):
    created_at = timezone.now()
    password = request.POST.get('password')
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
    faultRatio = request.POST.get('insuranceCompany')
    location = request.POST.get('location')
    others1 = request.POST.get('others1')
    others2 = request.POST.get('others2')
    others3 = request.POST.get('others3')
    note = request.POST.get('note')
    addition = request.POST.get('addition')
    price = request.POST.get('price')
    opinion = request.POST.get('opinion')
    image1 = request.FILES.get('image1')
    image2 = request.FILES.get('image2')
    image3 = request.FILES.get('image3')
    image4 = request.FILES.get('image4')
    image5 = request.FILES.get('image5')
    image6 = request.FILES.get('image6')
    image7 = request.FILES.get('image7')
    image8 = request.FILES.get('image8')
    image9 = request.FILES.get('image9')
    image10 = request.FILES.get('image10')
    image11 = request.FILES.get('image11')
    image12 = request.FILES.get('image12')
    image13 = request.FILES.get('image13')
    image14 = request.FILES.get('image14')
    image15 = request.FILES.get('image15')
    image16 = request.FILES.get('image16')
    image17 = request.FILES.get('image17')
    post = Post(created_at=created_at, password=password, client=client, phoneNumber=phoneNumber, contact=contact, carModel=carModel, carNumber=carNumber, birth=birth, trim=trim, fuel=fuel, driveType=driveType, airbag=airbag, mileage=mileage, eventDate=eventDate, repairCost=repairCost, proposedCompensation=proposedCompensation, insuranceCompany=insuranceCompany, faultRatio=faultRatio, location=location, others1=others1, others2=others2, others3=others3, note=note, addition=addition, price=price, opinion=opinion, image1=image1, image2=image2, image3=image3, image4=image4, image5=image5, image6=image6, image7=image7, image8=image8, image9=image9, image10=image10, image11=image11, image12=image12, image13=image13, image14=image14, image15=image15, image16=image16, image17=image17)
    post.save()
    context = {'post' : post}
    return render(request, 'posts/create.html', context)

def edit(request, post_id):
    post = Post.objects.get(id=post_id)
    context = {'post' : post}
    return render(request, 'posts/edit.html', context)

def update(request, post_id):
    post = Post.objects.get(id=post_id)
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
    post.faultRatio = request.POST.get('faultRatio')
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
    post.image7 = request.FILES.get('image7')
    post.image8 = request.FILES.get('image8')
    post.image9 = request.FILES.get('image9')
    post.image10 = request.FILES.get('image10')
    post.image11 = request.FILES.get('image11')
    post.image12 = request.FILES.get('image12')
    post.save()
    context = {'post' : post}
    return render(request, 'posts/create.html', context)

@login_required
def add(request, post_id):
    post = Post.objects.get(id=post_id)
    context = {'post' : post}
    return render(request, 'posts/add.html', context)

@login_required
def record(request, post_id):
    post = Post.objects.get(id=post_id)
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
    post.faultRatio = request.POST.get('faultRatio')
    post.location = request.POST.get('location')
    post.others1 = request.POST.get('others1')
    post.others2 = request.POST.get('others2')
    post.others3 = request.POST.get('others3')
    post.note = request.POST.get('note')
    post.addition = request.POST.get('addition')
    post.image1 = request.FILES.get('image1')
    post.image2 = request.FILES.get('image2')
    post.image3 = request.FILES.get('image3')
    post.image4 = request.FILES.get('image4')
    post.image5 = request.FILES.get('image5')
    post.image6 = request.FILES.get('image6')
    post.image13 = request.FILES.get('image13')
    post.image14 = request.FILES.get('image14')
    post.image15 = request.FILES.get('image15')
    post.image16 = request.FILES.get('image16')
    post.image17 = request.FILES.get('image17')
    post.save()
    context = {'post' : post}
    return render(request, 'posts/addition.html', context)

@login_required
def bidding(request, post_id):
    post = Post.objects.get(id=post_id)
    context = {'post' : post}
    return render(request, 'posts/bidding.html', context)

@login_required
def tender(request, post_id):
    post = Post.objects.get(id=post_id)
    post.price = request.POST.get('price')
    post.opinion = request.POST.get('opinion')
    post.save()
    return redirect('posts:index')

def password(request, post_id):
    post = Post.objects.get(id=post_id)
    context = {'post' : post}
    return render(request, 'posts/pass.html', context)

def enter(request, post_id):
    post = Post.objects.get(id=post_id)
    context = {'post' : post}
    answer = request.POST.get('answer')
    password = post.password
        
    if  str(answer) == str(password):
        return render(request, 'posts/edit.html', context)
    else:
        return redirect('posts:index')

@login_required
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

@staff_member_required
def export_content(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="regist_list.csv"'
    response.write(u'\ufeff'.encode('utf8'))

    writer = csv.writer(response)
    writer.writerow(['client', 'phoneNumber', 'contact', 'carModel', 'carNumber', 'carModel', 'birth', 'trim', 'fuel', 'driveType', 'airbag', 'mileage', 'eventDate', 'repairCost', 'proposedCompensation', 'insuranceCompany', 'faultRatio', 'others1', 'others2', 'others3', 'note', 'addition', 'price', 'opinion'])

    rows = Post.objects.all().values_list('client', 'phoneNumber', 'contact', 'carModel', 'carNumber', 'carModel', 'birth', 'trim', 'fuel', 'driveType', 'airbag', 'mileage', 'eventDate', 'repairCost', 'proposedCompensation', 'insuranceCompany', 'faultRatio', 'others1', 'others2', 'others3', 'note', 'addition', 'price', 'opinion') 
    
    for row in rows:
        writer.writerow(row)

    return response

def search(request):
    posts = Post.objects.all().order_by('-created_at')
    q = request.GET.get('q', "") 
    if q:
        posts = posts.filter(Q(carNumber__icontains=q) | Q(client__icontains=q)).distinct()
        context = {'posts' : posts,}
        return render(request, 'posts/index.html', context)
    else:
        posts = Post.objects.all().order_by('-created_at')
        context = {'posts' : posts,}
        return render(request, 'posts/index.html', context)