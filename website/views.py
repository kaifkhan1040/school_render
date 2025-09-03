from django.shortcuts import render, redirect, get_object_or_404
from customadmin.forms import ContactusForm
from django.contrib import messages
from customadmin.models import Gallery,Event,Notice

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
    gallery=Gallery.objects.all()
    gallery_group = chunked(gallery, 3 if len(gallery)<2 else 1)
    notices=Notice.objects.all()
    print('*'*1000)
    print('notice:',notices)
    
    return render(request,'web/index.html',{
        # 'car_brands_grouped':car_brands_grouped,'car':car,
                                            'form':form,'gallery':gallery_group,"notices":notices
                                            })

def about(request):
    return render(request,'web/aboutus.html')


def contact(request):
    form=ContactusForm()
    if request.method=="POST":
        form=ContactusForm(request.POST)
        if form.is_valid():
            form.save()
            
            messages.success(request, f'contact form submitted successfully!')
            return redirect('web:index')
        else:
            print('errr',form.errors)
            
            messages.error(request, f'{form.errors}')
    return render(request,'web/contactus.html',{'form':form})

def gallery(request):
    gallery=Gallery.objects.all()
    gallery_group = chunked(gallery, 3 if len(gallery)<2 else 1)
    return render(request,'web/gallery.html',{'gallery':gallery_group})

def addmission(request):
    return render(request,'web/addmission.html')