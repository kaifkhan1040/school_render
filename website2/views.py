from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from customadmin.forms import ContactusForm
from django.contrib import messages
from customadmin.models import Gallery,Event,Notice,Testimonie,MissionAndVission,Academics
from django.http import FileResponse, Http404
import os

def chunked(lst, n):
        return [lst[i:i+n] for i in range(0, len(lst), n)]
# from customadmin.models import CarCompany, CarModel, Trim, ServiceCategory, ServiceItem, TrimServicePrice
# Create your views here.
def index(request):
    # car=CarCompany.objects.all()
    # def chunked(lst, n):
    #     return [lst[i:i+n] for i in range(0, len(lst), n)]
    # category=ServiceCategory.objects.all()

    # car_brands_grouped = chunked(car, 4)
    form=ContactusForm()
    gallery=Gallery.objects.filter(image__isnull=False).exclude(image='')
    gallery_group = chunked(gallery, 3)
    print('*'*100)
    notices=Notice.objects.all()
    print('*'*1000)
    print('notice:',notices)
    testimonie=Testimonie.objects.all()
    vission=MissionAndVission.objects.filter(category='Our Vision')
    mission=MissionAndVission.objects.filter(category='Our Mission')
    academics=Academics.objects.all()

    # print(gallery_group)
    # for i in gallery_group:
    #     print(i)

    testimonie_grouped = chunked(testimonie, 2)
    # print(gallery_group)
    # for i in gallery_group:
    #     print(i)
    return render(request,'web2/index.html',{
        # 'car_brands_grouped':car_brands_grouped,'car':car,
                                            'form':form,'gallery_group':gallery_group,'notices':notices,'is_index':True,
                                            'testimonie_grouped':testimonie_grouped,'vission':vission,'mission':mission,
                                            'academics':academics
                                            })

def about(request):
    academics=Academics.objects.all()
    return render(request,'web2/about.html',{'is_about':True,'academics':academics})
from django.utils.safestring import mark_safe


def contact(request):
    form=ContactusForm()
    print('*'*100)
    if request.method=="POST":
        form=ContactusForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, f'Thank you for reaching out to us. Our team will get back to you shortly.')
            return redirect('web2:index')
        else:
            print('errr',form.errors)
            error_messages = '<br>'.join(
                [f"{error}" for field_errors in form.errors.values() for error in field_errors]
            )
            messages.error(request, mark_safe(error_messages))
            return redirect('web2:index')
    academics=Academics.objects.all()
    return render(request,'web2/contactus.html',{'form':form,'academics':academics})

def gallery(request):
    gallery=Gallery.objects.filter(image__isnull=False).exclude(image='')
    gallery_group = chunked(gallery, 3)
    academics=Academics.objects.all()
    return render(request,'web2/gallery.html',{'gallery_group':gallery_group,'is_gallery':True,'academics':academics})

def gallery_video(request):
    gallery=Gallery.objects.filter(video__isnull=False).exclude(video='')
    gallery_group_video = chunked(gallery, 3)
    academics=Academics.objects.all()
    return render(request,'web2/gallery.html',{'gallery_group_video':gallery_group_video,'is_gallery':True,'academics':academics})

def addmission(request):
    academics=Academics.objects.all()
    return render(request,'web2/addmission.html',{'academics':academics})

def fee(request):
    academics=Academics.objects.all()
    return render(request,'web2/fee.html',{'is_fee':True,'academics':academics})

def download_pdf(request):
    filepath = os.path.join('static', 'Registration_Form.pdf')
    try:
        return FileResponse(open(filepath, 'rb'), content_type='application/pdf')
    except FileNotFoundError:
        raise Http404("PDF not found")