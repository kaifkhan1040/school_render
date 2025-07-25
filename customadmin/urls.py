from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='home'),
    path('event/', views.event, name='enent'),
    path('add-event/', views.add_event, name='add_event'),
    path('update-event/<int:id>/', views.add_event, name='update_event'),
    path('delete-event/<int:id>/', views.delete_event, name='delete_event'),
    path('gallery/', views.gallery, name='gallery'),
    path('add-gallery/', views.add_gallery, name='add_gallery'),
    path('update-gallery/<int:id>/', views.add_gallery, name='update_gallery'),
    path('delete-gallery/<int:id>/', views.delete_gallery, name='delete_gallery'),
    path('course/', views.course, name='course'),
    path('add-course/', views.add_course, name='add_course'),
    path('update-course/<int:id>/', views.add_course, name='update_course'),
    path('delete-course/<int:id>/', views.delete_course, name='delete_course'),
    path('contactus/', views.contactus, name='contactus'),
    path('view-contactus/<int:id>/', views.view_contactus, name='view_contactus'),
    path('delete-contactus/<int:id>/', views.delete_contactus, name='delete_contactus'),
    path('calendar_events/', views.calendar_events, name='calendar_events'),
    path('notice/', views.notice, name='notice'),
    path('add-notice/', views.add_notice, name='add_notice'),
    path('update-notice/<int:id>/', views.add_notice, name='update_notice'),
    path('delete-notice/<int:id>/', views.delete_notice, name='delete_notice'),
    path('testimonial/', views.testimonial, name='testimonial'),
    path('add-testimonial/', views.add_testimonial, name='add_testimonial'),
    path('update-testimonial/<int:id>/', views.add_testimonial, name='update_testimonial'),
    path('delete-testimonial/<int:id>/', views.delete_testimonial, name='delete_testimonial'),
    path('our_vission_mission/', views.our_vission_mission, name='our_vission_mission'),
    path('add-our_vission_mission/', views.add_our_vission_mission, name='add_our_vission_mission'),
    path('update-our_vission_mission/<int:id>/', views.add_our_vission_mission, name='update_our_vission_mission'),
    path('delete-our_vission_mission/<int:id>/', views.delete_our_vission_mission, name='delete_our_vission_mission'),
    path('academics/', views.academics, name='academics'),
    path('add-academics/', views.add_academics, name='add_academics'),
    path('update-academics/<int:id>/', views.add_academics, name='update_academics'),
    path('delete-academics/<int:id>/', views.delete_academics, name='delete_academics'),
    path('subacademics/', views.subacademics, name='subacademics'),
    path('add-subacademics/', views.add_subacademics, name='add_subacademics'),
    path('update-subacademics/<int:id>/', views.add_subacademics, name='update_subacademics'),
    path('delete-subacademics/<int:id>/', views.delete_subacademics, name='delete_subacademics'),
    path('academicsitem/', views.academicsitem, name='academicsitem'),
    path('add-academicsitem/', views.add_academicsitem, name='add_academicsitem'),
    path('update-academicsitem/<int:id>/', views.add_academicsitem, name='update_academicsitem'),
    path('delete-academicsitem/<int:id>/', views.delete_academicsitem, name='delete_academicsitem'),

]