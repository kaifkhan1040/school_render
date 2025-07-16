from django import forms
from users.models import CustomUser
from django.forms import EmailInput
from django.forms import ModelForm, TextInput, EmailInput, CharField, PasswordInput, ChoiceField, BooleanField, \
    NumberInput, DateInput
from .models import Event,Gallery,Contactus,Course,Notice,Testimonie,MissionAndVission,Academics,\
    SubAcademics,AcademicsItem
from ckeditor.widgets import CKEditorWidget
from datetime import date, timedelta
from django.core.exceptions import ValidationError

class EventForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control valid'})
        self.fields['description'].widget.attrs.update({'class': 'form-control valid'})
        self.fields['start_date'].widget.attrs.update({'class': 'form-control valid'})
        self.fields['end_date'].widget.attrs.update({'class': 'form-control valid'})


    class Meta:
            model = Event
            fields = ('name','description','start_date','end_date')
            widgets = {
            'start_date':DateInput(attrs={
                'type': 'date',
                'class': "form-control mb-2",}),
             'end_date':DateInput(attrs={
                'type': 'date',
                'class': "form-control mb-2",
                'placeholder':"date hai"}),
                }

class GalleryForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'form-control valid'})
        self.fields['image'].widget.attrs.update({'class': 'form-control valid'})
        self.fields['description'].widget.attrs.update({'class': 'form-control valid'})
        self.fields['video'].widget.attrs.update({'class': 'form-control valid','multiple':True})


    class Meta:
            model = Gallery
            fields = ('title','image','description','video')
            widgets = {

            'image': forms.ClearableFileInput(attrs={'allow_multiple_selected': True}),
            'video': forms.ClearableFileInput(attrs={'allow_multiple_selected': True})

            }

    def clean_Video(self):
        video = self.cleaned_data.get('Video')
        if video and not video.name.endswith('.mp4'):
            raise forms.ValidationError("Only MP4 files are allowed.")
        return video


class ContactusForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['student_name'].widget.attrs.update({'class': 'form-control valid','placeholder':'Student Name'})
        self.fields['parents_name'].widget.attrs.update({'class': 'form-control valid','placeholder':'Parents Name'})
        self.fields['parents_mobile_number'].widget.attrs.update({'class': 'form-control valid','placeholder':'Parents Mobile Number'})
        self.fields['child_date_of_birth'].widget.attrs.update({'class': 'form-control valid','placeholder':'Child Date Of Birth'})
        self.fields['select_class_looking_for'].widget.attrs.update({'class': 'form-control valid','placeholder':'Select Class Looking For'})


    class Meta:
            model = Contactus
            fields = ('student_name','parents_name','parents_mobile_number','child_date_of_birth','select_class_looking_for')
            widgets = {
            'child_date_of_birth':DateInput(attrs={
                'type': 'date',
                'class': "form-control mb-2",
                'placeholder': 'Enter Child Date of Birth',}),}
    child_date_of_birth = forms.DateField(
        input_formats=['%d-%m-%Y'],
        widget=forms.TextInput(attrs={
            'type': 'text',
            'class': 'form-control valid',
            'placeholder': 'Enter Child Date of Birth'
        })
    )
    def clean_child_date_of_birth(self):
        dob = self.cleaned_data.get('child_date_of_birth')
        if dob:
            today = date.today()
            min_age_date = today - timedelta(days=2.5 * 365.25)  # 2.5 years as days
            if dob > min_age_date:
                raise ValidationError("Child must be at least 2.5 years old.")
        return dob



class CourseForm(ModelForm):
    description = forms.CharField(widget=CKEditorWidget())
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'form-control valid','placeholder':'Your Name'})
        self.fields['fees'].widget.attrs.update({'class': 'form-control valid','placeholder':'Your Email'})
        self.fields['image'].widget.attrs.update({'class': 'form-control valid','placeholder':'Your Subject'})
        self.fields['description'].widget.attrs.update({'class': 'form-control valid','placeholder':'Write your message'})


    class Meta:
            model = Course
            fields = ('title','fees','image','description')

class NoticeForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'form-control valid'})
        self.fields['description'].widget.attrs.update({'class': 'form-control valid'})
        self.fields['date'].widget.attrs.update({'class': 'form-control valid'})
        self.fields['file'].widget.attrs.update({'class': 'form-control valid'})


    class Meta:
            model = Notice
            fields = ('title','description','date','file')
            widgets = {
            'date':DateInput(attrs={
                'type': 'date',
                'class': "form-control mb-2",
                'placeholder': 'Enter Child Date of Birth',}),}

class TestimonieForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
            model = Testimonie
            fields = '__all__'

class MissionAndVissionForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
            model = MissionAndVission
            fields = '__all__'

class AcademicsForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
            model = Academics
            fields = '__all__'

class SubAcademicsForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
            model = SubAcademics
            fields = '__all__'

class AcademicsItemForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
            model = AcademicsItem
            fields = '__all__'