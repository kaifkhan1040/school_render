from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
from .models import Student
# def hello(request):
#     return HttpResponse( 'hello jango for the first time')
def hello(request):
    return render( request, 'first-app/form.html')
def form_submit(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        email = request.POST.get('email')
        last_name = request.POST.get('last_name')
        Student.objects.create(
            first_name=first_name,
            email=email,
            last_name=last_name
        )
        print(first_name, email, last_name)
        # Here you can process the data, save it to the database, etc.
       
   
    return render(request,'first-app/form_submit.html')