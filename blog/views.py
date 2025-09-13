

from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required,permission_required
from django.http import HttpResponse, HttpResponseForbidden
from django.core.mail import send_mail
# Create your views here.


from .models import Contact,Experience,Education

from .forms import ExperienceForm,EducationForm

def home_page(request):
    return render(request, 'index.html')

def projects_page(request):
    return render(request, 'projects.html')

def resume_page(request):
    return render(request,'resume.html')

def resume(request):
    return render(request, 'resume.html')

def projects(request):
    return render(request, 'projects.html')

def home(request):
    return render(request, 'index.html')

# def contact(request):
#     return render(request, 'contact.html')

def contact_view(request):
    if request.method == "POST":
        name = request.POST.get("name","").strip()
        email = request.POST.get("email","").strip()
        phone = request.POST.get("phone", "").strip()
        message = request.POST.get("message", "").strip()



        if not name or not email or not message:
            return HttpResponse("Barcha maydonlarni to'ldiring!", status=400)

        contact = Contact(name=name, email=email, phone=phone,message=message)
        contact.save()
        # send_mail(
        #     f"Contact request from {name}",
        #     message,
        #     email,
        #     ['uzcoding54@gmail.com'],
        #     fail_silently=False,
        # )
        return HttpResponse("Thanks for your message!.")
    return render(request,'contact.html')


def create_experience(request):
    if request.method == "POST":
        form = ExperienceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('resume')
    else:
        form = ExperienceForm()

    return render(request,'create_experience.html',{'form':form})


# def show_resume(request):
#     experiences = Experience.objects.all()
#     return render(request,'resume.html', {'experiences' : experiences})




@login_required

def delete_experience(request, id):
    if not request.user.is_staff and not request.user.is_superuser:
        return HttpResponseForbidden("Siz ushbu malumotlarni uchirolmaysiz!")
    


    experience = get_object_or_404(Experience, id=id)
    experience.delete()
    return redirect('resume')


@login_required
def add_education(request):
    if request.method == 'POST':
        form = EducationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('resume')
    else:
        form = EducationForm()
    return render(request, 'add_education.html', {'form': form})

@login_required
def edit_education(request, education_id):
    education = get_object_or_404(Education, id=education_id)
    if request.method == 'POST':
        form = EducationForm(request.POST, instance=education)
        if form.is_valid():
            form.save()
            return redirect('resume')
    else:
        form = EducationForm(instance=education)
    return render(request, 'edit_education.html', {'form': form})

@login_required
@permission_required('yourapp.can_delete_education', raise_exception=True)
def delete_education(request, education_id):
    education = get_object_or_404(Education, id=education_id)
    if request.method == "POST":
        education.delete()
        return redirect('resume')
    return render(request, 'delete_education.html', {'education': education})

# def resume(request):
#     educations = Education.objects.all()
#     return render(request, "resume.html", {'educations' : educations})

def resume(request):
    experiences = Experience.objects.all()
    educations = Education.objects.all()
    return render(request, 'resume.html', {'experiences': experiences, 'educations': educations})
