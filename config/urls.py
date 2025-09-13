# """
# URL configuration for config project.

# The `urlpatterns` list routes URLs to views. For more information please see:
#     https://docs.djangoproject.com/en/5.1/topics/http/urls/
# Examples:
# Function views
#     1. Add an import:  from my_app import views
#     2. Add a URL to urlpatterns:  path('', views.home, name='home')
# Class-based views
#     1. Add an import:  from other_app.views import Home
#     2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
# Including another URLconf
#     1. Import the include() function: from django.urls import include, path
#     2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
# """
# from django.conf import settings
# from django.contrib import admin
# from django.urls import path
# from blog import views
# from blog.views import home,projects,resume,contact_view   ,home_page , projects_page, show_resume, create_experience,delete_experience,add_education,edit_education,delete_education,resume
# from django.conf.urls.static import static

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('home/', home_page),
#     path('projects/', projects_page),
#     path('resume/', show_resume),
#     path('contact/', contact_view, name='contact'),
#     path('resume/', views.show_resume, name='resume'),
#     path('projects/', projects, name='projects'),
#     path('', home, name='home'),
#     #path('contact/', views.contact, name='contact'),
#     path('contact_me/',contact_view, name='contact_me'),
#     path('create_exp/', create_experience, name='create_exp'),
#     path('delete_experience/<int:id>/',delete_experience, name='delete_experience' ),
#     path('education/add/', add_education, name='add_education'),
#     path('education/edit/<int:education_id>/', edit_education, name='edit_education'),
#     path('education/delete/<int:education_id>/', delete_education, name='delete_education'),
    

# ] + static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])


from django.conf import settings
from django.contrib import admin
from django.urls import path
from blog.views import (
    home, projects, resume, contact_view, home_page, projects_page,
    resume, create_experience, delete_experience, add_education,
    edit_education, delete_education
)
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home_page),
    path('projects/', projects, name='projects'),
    path('resume/', resume, name='resume'),
    path('contact/', contact_view, name='contact'),
    path('contact_me/', contact_view, name='contact_me'),
    path('', home, name='home'),

    # Tajriba
    path('create_exp/', create_experience, name='create_exp'),
    path('delete_experience/<int:id>/', delete_experience, name='delete_experience'),

    # Ta'lim
    path('education/add/', add_education, name='add_education'),
    path('education/edit/<int:education_id>/', edit_education, name='edit_education'),
    path('education/delete/<int:education_id>/', delete_education, name='delete_education'),
]

# Static files
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
