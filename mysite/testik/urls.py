from django.conf import settings
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static

from mysite.testik.views import *
from mysite.home import views
app_name = 'testik'
urlpatterns = [
    #path('admin/', admin.site.urls),
    path('Sertif/', SertifView.as_view(), name='Sertif'),
    path('Sertif/update/<int:pk>/', SertifUpdate.as_view(), name='SertifUpdate'),
    path('Sertif/detail/<int:pk>/', SertifDetail.as_view(), name='SertifDetail'),
    path('Sertif/create/', SertifCreate.as_view(), name='SertifCreate'),
    path('Sertif/delete/<int:pk>/', SertifDelete.as_view(), name='SertifDelete'),

    path('Answers/', AnswersView.as_view(), name='Answers'),
    path('Answers/update/<int:pk>/', AnswersUpdate.as_view(), name='AnswersUpdate'),
    path('Answers/detail/<int:pk>/', AnswersDetail.as_view(), name='AnswersDetail'),
    path('Answers/create/', AnswersCreate.as_view(), name='AnswersCreate'),
    path('Answers/delete/<int:pk>/', AnswersDelete.as_view(), name='AnswersDelete'),
    
]
