from django.db import models
from ckeditor.fields import RichTextField
from django.core.exceptions import ValidationError

# Create your models here.

class Event(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    start_date = models.DateField()
    end_date = models.DateField(null=True,blank=True)

    def __str__(self):
        return self.name

def validate_mp4(file):
    if not file.name.endswith('.mp4'):
        raise ValidationError("Only MP4 files are allowed.")

class Gallery(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='gallery_images/',blank=True,null=True)
    video = models.FileField(upload_to='gallery_video/',validators=[validate_mp4],blank=True,null=True)
    description = models.TextField(blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Contactus(models.Model):
    student_name = models.CharField(max_length=255)
    parents_name = models.CharField(max_length=255)
    parents_mobile_number = models.CharField(max_length=10)
    child_date_of_birth = models.DateField(null=True,blank=True)
    select_class_looking_for  = models.CharField(choices=[('P.Nursery','P.Nursery'),('Nursery','Nursery'),('LKG','LKG'),('UKG','UKG'),('1ST','1ST'),('2ND','2ND'),('3RD','3RD'),('4TH','4TH'),('5TH','5TH')])

    def __str__(self):
        return self.name

class Notice(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField()
    file = models.FileField(upload_to='notices/', blank=True, null=True)

    class Meta:
        ordering = ['-date']
        verbose_name = "Notice"
        verbose_name_plural = "Notices"

    def __str__(self):
        return self.title


class Course(models.Model):
    title = models.CharField(max_length=200)
    description = RichTextField()
    fees = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='course_images/', null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Testimonie(models.Model):
    message=models.TextField()
    name=models.CharField(max_length=25)
    image=models.ImageField(upload_to='testimonie/image/')

class MissionAndVission(models.Model):
    point = models.CharField(max_length=2000)
    category = models.CharField(max_length=30,choices=(('Our Vision','Our Vision'),('Our Mission','Our Mission')))

class Academics(models.Model):
    name = models.CharField(max_length=150)
    file= models.FileField(upload_to='academics/main/',null=True,blank=True)

    def __str__(self):
        return self.name

class SubAcademics(models.Model):
    academics = models.ForeignKey(Academics,on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    file= models.FileField(upload_to='academics/sub/',null=True,blank=True)

    def __str__(self):
        return self.name

class AcademicsItem(models.Model):
    subacademics =models.ForeignKey(SubAcademics,on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    file= models.FileField(upload_to='academics/main/',null=True,blank=True)

    def __str__(self):
        return self.name