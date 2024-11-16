from django.shortcuts import render,HttpResponseRedirect
from .forms import StudentRegistration
from  .models import User
from django.shortcuts import redirect
# Create your views here.
#This is a function which helps to us add new data and show them
def add_show(request):
    if request.method=='POST':
        fm=StudentRegistration(request.POST)
        if fm.is_valid():
            nm=fm.cleaned_data['name']
            em=fm.cleaned_data['email']
            pw=fm.cleaned_data['password']
            reg=User(name=nm,email=em,password=pw)
            reg.save()
           #fm.save() By it we also save all the data input by user 
           #And also by cleaned_data and save() method dictionary we can save the data in database
        fm=StudentRegistration()# it is used to set the form blank after submission...
        return redirect('/crudope')
    else:
        fm=StudentRegistration()
    stud=User.objects.all()
    return render(request, 'crudoperation/addandshow.html',{'form':fm,'stu':stud})


# This function will helps to delete data from admin...
def delete_data(request,id):
    if request.method=='POST':
        pi=User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/crudope')


#This function willl update/edit 
# def update_data(request,id):
#     if request.method=='POST':
#         pi=User.objects.get(pk=id)
#         fm=StudentRegistration(request.POST,instance=pi)
#         if fm.is_valid():
#             fm.save()
#         else:
#              pi=User.objects.get(pk=id)
#              fm=StudentRegistration(instance=pi)
#         return render(request,'crudoperation/updatestudent.html',{'form':fm})
from django.shortcuts import render, get_object_or_404, redirect
from .forms import StudentRegistration
from .models import User
def update_data(request, id):
    # Get the existing user instance based on the provided ID
    user_instance = get_object_or_404(User, pk=id)

    if request.method == 'POST':
        # Create a form using the existing instance with updated POST data
        form = StudentRegistration(request.POST, instance=user_instance)
        if form.is_valid():
            form.save()
            # Redirect to a success page or back to the main list
            return redirect('/crudope')  # Update this URL based on your needs
    else:
        # Pre-fill the form with the existing instance data
        form = StudentRegistration(instance=user_instance)

    # Render the template with the form
    return render(request, 'crudoperation/updatestudent.html', {'form': form})