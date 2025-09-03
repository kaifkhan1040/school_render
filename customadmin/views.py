from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse_lazy
from .models import Event,Gallery,Contactus,Course,Notice,Testimonie,MissionAndVission,Academics,SubAcademics,AcademicsItem
from .forms import EventForm,GalleryForm,ContactusForm,CourseForm,NoticeForm,TestimonieForm,MissionAndVission,MissionAndVissionForm,\
    AcademicsItemForm,AcademicsForm,SubAcademicsForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
# Create your views here.
def index(request):
    return render(request,'customadmin/index.html')

def event(request):
    event = Event.objects.all()
    return render(request,'customadmin/eventlist.html',{'event':event})

def add_event(request,id=None):
    print('run')
    if request.method == "POST":
        print('post')
        print(request.POST)
        obj=None
        if id:
            obj = get_object_or_404(Event, id=id)
            form = EventForm(request.POST,instance=obj)
        else:
            form = EventForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, f'Event has been Added successfully!')
            return redirect('customadmin:enent')
        else:
            print('errr',form.errors)

            messages.error(request, f'{form.errors}')
    else:
        obj=None
        if id:
            obj = get_object_or_404(Event, id=id)
            form = EventForm(instance=obj)
        else:
            form = EventForm()

    return render(request, 'customadmin/event_add.html', {'form': form,'obj':obj})

def delete_event(request,id=None):
    if id:
        obj = get_object_or_404(Event, id=id)
        obj.delete()

        messages.success(request, f'Event has been removed successfully!')
        return redirect('customadmin:enent')


def gallery(request):
    gallery = Gallery.objects.all()
    return render(request,'customadmin/gallery.html',{'gallery':gallery})

def add_gallery(request,id=None):
    print('run')
    if request.method == "POST":
        print('post')
        print(request.POST)
        obj=None
        if id:
            obj = get_object_or_404(Gallery, id=id)
            print('data:',obj)
            form = GalleryForm(request.POST,request.FILES,instance=obj)
        else:
            form = GalleryForm(request.POST,request.FILES)
        if form.is_valid():
            images = request.FILES.getlist('image')
            videos = request.FILES.getlist('video')
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            if images:
                for img in images:
                    Gallery.objects.create(title=title,description=description,image=img)
            if videos:
                for vid in videos:
                    Gallery.objects.create(title=title,description=description,video=vid)

            messages.success(request, f'Gallery been updated successfully!')
            return redirect('customadmin:gallery')
        else:
            print('errr',form.errors)

            messages.error(request, f'{form.errors}')
    else:
        obj=None
        print(id)
        if id:
            obj = get_object_or_404(Gallery, id=id)
            print
            form = GalleryForm(instance=obj)
        else:
            form = GalleryForm()

    return render(request, 'customadmin/gallery_add.html', {'form': form,'obj':obj})

def delete_gallery(request,id=None):
    if id:
        obj = get_object_or_404(Gallery, id=id)
        obj.delete()

        messages.success(request, f'Gallery has been removed successfully!')
        return redirect('customadmin:gallery')

def contactus(request):
    contactus = Contactus.objects.all().order_by("-id")
    return render(request,'customadmin/contact.html',{'contactus':contactus})


def delete_contactus(request,id=None):
    if id:
        obj = get_object_or_404(Contactus, id=id)
        obj.delete()

        messages.success(request, f'Contact has been removed successfully!')
        return redirect('customadmin:contactus')

def view_contactus(request,id=None):
    # print('run')
    form=None
    # print(id)
    if id:
        obj = get_object_or_404(Contactus, id=id)
        form = ContactusForm(instance=obj)
    return render(request, 'customadmin/contact_view.html', {'form': form,'obj':obj})


def course(request):
    course = Course.objects.all()
    return render(request,'customadmin/course.html',{'course':course})

def add_course(request,id=None):
    print('run')
    if request.method == "POST":
        print('post')
        print(request.POST)
        obj=None
        if id:
            obj = get_object_or_404(Course, id=id)
            print('data:',obj)
            form = CourseForm(request.POST,request.FILES,instance=obj)
        else:
            form = CourseForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()

            messages.success(request, f'Course been updated successfully!')
            return redirect('customadmin:course')
        else:
            print('errr',form.errors)

            messages.error(request, f'{form.errors}')
    else:
        obj=None
        print(id)
        if id:
            obj = get_object_or_404(Course, id=id)

            form = CourseForm(instance=obj)
        else:
            form = CourseForm()

    return render(request, 'customadmin/course_add.html', {'form': form,'obj':obj})

def delete_course(request,id=None):
    if id:
        obj = get_object_or_404(Course, id=id)
        obj.delete()

        messages.success(request, f'Course has been removed successfully!')
        return redirect('customadmin:course')


def calendar_events(request):
    month = int(request.GET.get("month", 1))
    year = int(request.GET.get("year", 2025))

    events = Event.objects.filter(start_date__year=year, start_date__month=month).values('start_date','name','description')
    return JsonResponse(list(events), safe=False)



def notice(request):
    notice = Notice.objects.all()
    return render(request,'customadmin/notice.html',{'notice':notice})

def add_notice(request,id=None):
    print('run')
    if request.method == "POST":
        print('post')
        print(request.POST)
        obj=None
        if id:
            obj = get_object_or_404(Notice, id=id)
            print('data:',obj)
            form = NoticeForm(request.POST,request.FILES,instance=obj)
        else:
            form = NoticeForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()

            messages.success(request, f'notice been updated successfully!')
            return redirect('customadmin:notice')
        else:
            print('errr',form.errors)

            messages.error(request, f'{form.errors}')
    else:
        obj=None
        print(id)
        if id:
            obj = get_object_or_404(Notice, id=id)

            form = NoticeForm(instance=obj)
        else:
            form = NoticeForm()

    return render(request, 'customadmin/notice_add.html', {'form': form,'obj':obj})

def delete_notice(request,id=None):
    if id:
        obj = get_object_or_404(Notice, id=id)
        obj.delete()

        messages.success(request, f'Notice has been removed successfully!')
        return redirect('customadmin:notice')


def testimonial(request):
    testimonie = Testimonie.objects.all()
    return render(request,'customadmin/testimonie.html',{'testimonie':testimonie})

def add_testimonial(request,id=None):
    print('run')
    if request.method == "POST":
        print('post')
        print(request.POST)
        obj=None
        if id:
            obj = get_object_or_404(Testimonie, id=id)
            print('data:',obj)
            form = TestimonieForm(request.POST,request.FILES,instance=obj)
        else:
            form = TestimonieForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()

            messages.success(request, f'Testimonie been updated successfully!')
            return redirect('customadmin:testimonial')
        else:
            print('errr',form.errors)

            messages.error(request, f'{form.errors}')
    else:
        obj=None
        print(id)
        if id:
            obj = get_object_or_404(Testimonie, id=id)

            form = TestimonieForm(instance=obj)
        else:
            form = TestimonieForm()

    return render(request, 'customadmin/testimonie_add.html', {'form': form,'obj':obj})

def delete_testimonial(request,id=None):
    if id:
        obj = get_object_or_404(Testimonie, id=id)
        obj.delete()

        messages.success(request, f'Testimonie has been removed successfully!')
        return redirect('customadmin:testimonial')


def our_vission_mission(request):
    data = MissionAndVission.objects.all()
    return render(request,'customadmin/vission.html',{'data':data})

def add_our_vission_mission(request,id=None):
    print('run')
    if request.method == "POST":
        print('post')
        print(request.POST)
        obj=None
        if id:
            obj = get_object_or_404(MissionAndVission, id=id)
            print('data:',obj)
            form = MissionAndVissionForm(request.POST,request.FILES,instance=obj)
        else:
            form = MissionAndVissionForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()

            messages.success(request, f'Mission And Vission been updated successfully!')
            return redirect('customadmin:our_vission_mission')
        else:
            print('errr',form.errors)

            messages.error(request, f'{form.errors}')
    else:
        obj=None
        print(id)
        if id:
            obj = get_object_or_404(MissionAndVission, id=id)

            form = MissionAndVissionForm(instance=obj)
        else:
            form = MissionAndVissionForm()

    return render(request, 'customadmin/vission_add.html', {'form': form,'obj':obj})

def delete_our_vission_mission(request,id=None):
    if id:
        obj = get_object_or_404(MissionAndVission, id=id)
        obj.delete()

        messages.success(request, f'Mission And Vission has been removed successfully!')
        return redirect('customadmin:our_vission_mission')

def academics(request):
    academics = Academics.objects.all()
    return render(request,'customadmin/academics.html',{'academics':academics})

def add_academics(request,id=None):
    print('run')
    if request.method == "POST":
        print('post')
        print(request.POST)
        obj=None
        if id:
            obj = get_object_or_404(Academics, id=id)
            print('data:',obj)
            form = AcademicsForm(request.POST,request.FILES,instance=obj)
        else:
            form = AcademicsForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()

            messages.success(request, f'Academics been updated successfully!')
            return redirect('customadmin:academics')
        else:
            print('errr',form.errors)

            messages.error(request, f'{form.errors}')
    else:
        obj=None
        print(id)
        if id:
            obj = get_object_or_404(Academics, id=id)

            form = AcademicsForm(instance=obj)
        else:
            form = AcademicsForm()

    return render(request, 'customadmin/academics_add.html', {'form': form,'obj':obj})

def delete_academics(request,id=None):
    if id:
        obj = get_object_or_404(Academics, id=id)
        obj.delete()

        messages.success(request, f'Academics has been removed successfully!')
        return redirect('customadmin:academics')


def subacademics(request):
    subAcademics = SubAcademics.objects.all()
    return render(request,'customadmin/subAcademics.html',{'subAcademics':subAcademics})

def add_subacademics(request,id=None):
    print('run')
    if request.method == "POST":
        print('post')
        print(request.POST)
        obj=None
        if id:
            obj = get_object_or_404(SubAcademics, id=id)
            print('data:',obj)
            form = SubAcademicsForm(request.POST,request.FILES,instance=obj)
        else:
            form = SubAcademicsForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()

            messages.success(request, f'SubAcademics been updated successfully!')
            return redirect('customadmin:subacademics')
        else:
            print('errr',form.errors)

            messages.error(request, f'{form.errors}')
    else:
        obj=None
        print(id)
        if id:
            obj = get_object_or_404(SubAcademics, id=id)

            form = SubAcademicsForm(instance=obj)
        else:
            form = SubAcademicsForm()

    return render(request, 'customadmin/subacademics_add.html', {'form': form,'obj':obj})

def delete_subacademics(request,id=None):
    if id:
        obj = get_object_or_404(SubAcademics, id=id)
        obj.delete()

        messages.success(request, f'SubAcademics has been removed successfully!')
        return redirect('customadmin:subacademics')

def academicsitem(request):
    subAcademics = AcademicsItem.objects.all()
    return render(request,'customadmin/Academicsitem.html',{'subAcademics':subAcademics})

def add_academicsitem(request,id=None):
    print('run')
    if request.method == "POST":
        print('post')
        print(request.POST)
        obj=None
        if id:
            obj = get_object_or_404(AcademicsItem, id=id)
            print('data:',obj)
            form = AcademicsItemForm(request.POST,request.FILES,instance=obj)
        else:
            form = AcademicsItemForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()

            messages.success(request, f'AcademicsItem been updated successfully!')
            return redirect('customadmin:academicsitem')
        else:
            print('errr',form.errors)

            messages.error(request, f'{form.errors}')
    else:
        obj=None
        print(id)
        if id:
            obj = get_object_or_404(AcademicsItem, id=id)

            form = AcademicsItemForm(instance=obj)
        else:
            form = AcademicsItemForm()

    return render(request, 'customadmin/Academicsitem_add.html', {'form': form,'obj':obj})

def delete_academicsitem(request,id=None):
    if id:
        obj = get_object_or_404(AcademicsItem, id=id)
        obj.delete()

        messages.success(request, f'AcademicsItem has been removed successfully!')
        return redirect('customadmin:academicsitem')





