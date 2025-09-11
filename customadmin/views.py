from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse_lazy
from .models import Event,Gallery,Contactus,Course,Notice,Testimonie,MissionAndVission,Academics,SubAcademics,AcademicsItem,NoticeEmail
from .forms import EventForm,GalleryForm,ContactusForm,CourseForm,NoticeForm,TestimonieForm,MissionAndVission,MissionAndVissionForm,\
    AcademicsItemForm,AcademicsForm,SubAcademicsForm,NoticeEmailForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.core.mail import send_mail
from users.email import NoticeEmailSend
import csv, io
from .forms import CSVUploadForm
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
# Create your views here.
@login_required
def index(request):
    return render(request,'customadmin/index.html')

@login_required
def noticeemail(request):
    event = NoticeEmail.objects.all()
    return render(request,'customadmin/noticeemaillist.html',{'event':event})

@login_required
def add_noticeemail(request,id=None):
    print('run')
    if request.method == "POST":
        print('post')
        print(request.POST)
        obj=None
        if id:
            obj = get_object_or_404(NoticeEmail, id=id)
            form = NoticeEmailForm(request.POST,instance=obj)
        else:
            form = NoticeEmailForm(request.POST)
        if form.is_valid():
            data=form.save()
            
            messages.success(request, f'NoticeEmail has been Added successfully!')
            return redirect('customadmin:noticeemail')
        else:
            print('errr',form.errors)

            messages.error(request, f'{form.errors}')
    else:
        obj=None
        if id:
            obj = get_object_or_404(NoticeEmail, id=id)
            form = NoticeEmailForm(instance=obj)
        else:
            form = NoticeEmailForm()

    return render(request, 'customadmin/noticeemail_add.html', {'form': form,'obj':obj})

@login_required
def delete_noticeemail(request,id=None):
    if id:
        obj = get_object_or_404(NoticeEmail, id=id)
        obj.delete()

        messages.success(request, f'NoticeEmail has been removed successfully!')
        return redirect('customadmin:noticeemail')

@login_required
def event(request):
    event = Event.objects.all()
    return render(request,'customadmin/eventlist.html',{'event':event})

@login_required
def bulk_upload_emails(request):
    if request.method == "POST":
        formscv = CSVUploadForm(request.POST, request.FILES)
        if formscv.is_valid():
            csv_file = request.FILES["file"]

            if not csv_file.name.endswith('.csv'):
                messages.error(request, "This is not a CSV file")
                return redirect("customadmin:bulk_upload_emails")

            # Read file
            data_set = csv_file.read().decode("UTF-8")
            io_string = io.StringIO(data_set)
            next(io_string) 
            emails_to_create = []
            invalid_emails = []
            for row in csv.reader(io_string, delimiter=","):
                email = row[0].strip()
                if email:  
                    try:
                        validate_email(email)  
                        if not NoticeEmail.objects.filter(email=email).exists():
                            emails_to_create.append(NoticeEmail(email=email))
                    except ValidationError:
                        invalid_emails.append(email)

            if emails_to_create:
                NoticeEmail.objects.bulk_create(emails_to_create, ignore_conflicts=True)
                messages.success(request, f"{len(emails_to_create)} valid emails uploaded successfully!")

            if invalid_emails:
                messages.warning(request, f"Invalid emails skipped: {', '.join(invalid_emails)}")
            return redirect("customadmin:noticeemail")
    else:
        formscv = CSVUploadForm()

    return render(request, "customadmin/bulkupload.html", {"form": formscv})

@login_required
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

@login_required
def delete_event(request,id=None):
    if id:
        obj = get_object_or_404(Event, id=id)
        obj.delete()

        messages.success(request, f'Event has been removed successfully!')
        return redirect('customadmin:enent')


@login_required
def gallery(request):
    gallery = Gallery.objects.all()
    return render(request,'customadmin/gallery.html',{'gallery':gallery})

@login_required
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

@login_required
def delete_gallery(request,id=None):
    if id:
        obj = get_object_or_404(Gallery, id=id)
        obj.delete()

        messages.success(request, f'Gallery has been removed successfully!')
        return redirect('customadmin:gallery')

@login_required
def contactus(request):
    contactus = Contactus.objects.all().order_by("-id")
    return render(request,'customadmin/contact.html',{'contactus':contactus})


@login_required
def delete_contactus(request,id=None):
    if id:
        obj = get_object_or_404(Contactus, id=id)
        obj.delete()

        messages.success(request, f'Contact has been removed successfully!')
        return redirect('customadmin:contactus')

@login_required
def view_contactus(request,id=None):
    # print('run')
    form=None
    # print(id)
    if id:
        obj = get_object_or_404(Contactus, id=id)
        form = ContactusForm(instance=obj)
    return render(request, 'customadmin/contact_view.html', {'form': form,'obj':obj})


@login_required
def course(request):
    course = Course.objects.all()
    return render(request,'customadmin/course.html',{'course':course})

@login_required
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

@login_required
def delete_course(request,id=None):
    if id:
        obj = get_object_or_404(Course, id=id)
        obj.delete()

        messages.success(request, f'Course has been removed successfully!')
        return redirect('customadmin:course')


@login_required
def calendar_events(request):
    month = int(request.GET.get("month", 1))
    year = int(request.GET.get("year", 2025))
    events = Event.objects.filter(start_date__year=year, start_date__month=month).values('start_date','name','description')
    return JsonResponse(list(events), safe=False)



@login_required
def notice(request):
    notice = Notice.objects.all()
    return render(request,'customadmin/notice.html',{'notice':notice})

@login_required
def add_notice(request,id=None):
    print('run')
    maillist = [i["email"] for i in NoticeEmail.objects.values("email").distinct()]
    print(maillist)
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
            data=form.save()
            try:
                NoticeEmailSend(data,maillist)
            except Exception as e:
                print('error:',e)

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

@login_required
def delete_notice(request,id=None):
    if id:
        obj = get_object_or_404(Notice, id=id)
        obj.delete()

        messages.success(request, f'Notice has been removed successfully!')
        return redirect('customadmin:notice')


@login_required
def testimonial(request):
    testimonie = Testimonie.objects.all()
    return render(request,'customadmin/testimonie.html',{'testimonie':testimonie})

@login_required
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

@login_required
def delete_testimonial(request,id=None):
    if id:
        obj = get_object_or_404(Testimonie, id=id)
        obj.delete()

        messages.success(request, f'Testimonie has been removed successfully!')
        return redirect('customadmin:testimonial')


@login_required
def our_vission_mission(request):
    data = MissionAndVission.objects.all()
    return render(request,'customadmin/vission.html',{'data':data})

@login_required
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

@login_required
def delete_our_vission_mission(request,id=None):
    if id:
        obj = get_object_or_404(MissionAndVission, id=id)
        obj.delete()

        messages.success(request, f'Mission And Vission has been removed successfully!')
        return redirect('customadmin:our_vission_mission')

@login_required
def academics(request):
    academics = Academics.objects.all()
    return render(request,'customadmin/academics.html',{'academics':academics})

@login_required
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

@login_required
def delete_academics(request,id=None):
    if id:
        obj = get_object_or_404(Academics, id=id)
        obj.delete()

        messages.success(request, f'Academics has been removed successfully!')
        return redirect('customadmin:academics')


@login_required
def subacademics(request):
    subAcademics = SubAcademics.objects.all()
    return render(request,'customadmin/subAcademics.html',{'subAcademics':subAcademics})

@login_required
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

@login_required
def delete_subacademics(request,id=None):
    if id:
        obj = get_object_or_404(SubAcademics, id=id)
        obj.delete()

        messages.success(request, f'SubAcademics has been removed successfully!')
        return redirect('customadmin:subacademics')

@login_required
def academicsitem(request):
    subAcademics = AcademicsItem.objects.all()
    return render(request,'customadmin/Academicsitem.html',{'subAcademics':subAcademics})

@login_required
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

@login_required
def delete_academicsitem(request,id=None):
    if id:
        obj = get_object_or_404(AcademicsItem, id=id)
        obj.delete()

        messages.success(request, f'AcademicsItem has been removed successfully!')
        return redirect('customadmin:academicsitem')





