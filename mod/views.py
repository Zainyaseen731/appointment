from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse
from .models import Post
from .models1 import Appointment,AppointmentTimeSlot
from .form import SearchForm,DataStore,Data_taking
from django.contrib.auth.models import User,auth
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def main(request): 
    context={
    }
    template="main.html"
    return render(request,template,context)





def signup(request):
    form=SearchForm(request.POST or None)
    if form.is_valid():
        first_name=(form.cleaned_data.get("first_name"))
        last_name=(form.cleaned_data.get("last_name"))
        username=(form.cleaned_data.get("username"))
        email=(form.cleaned_data.get("email"))
        password1=(form.cleaned_data.get("password1"))
        password2=(form.cleaned_data.get("password2"))
        print(first_name)
        print(last_name)
        print(username)
        print(email)
        print(password1)
        print(password2)

        if password1==password2:
            if User.objects.filter(username=username).exists():
                #raise forms.ValidationError("You cannot post more than once every x minutes")
                messages.info(request,"User name taken")
                return redirect('/signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email is taken")
                return redirect('/signup')
            else:
                user=User.objects.create_user(first_name=first_name,last_name=last_name,username=username,
                email=email,password=password1)
                user.save()
                return redirect('/login')
        
    return render(request,"form.html",{'form':form})


def login(request):
    form1=DataStore(request.POST or None)
    if form1.is_valid():
        username=(form1.cleaned_data.get("username"))
        password=(form1.cleaned_data.get("password"))
        print(username)
        print(password)
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/home')
        else:
            return redirect('/login')
    return render(request,"in.html",{'form':form1})


@login_required
def home(request):
    qs=Post.objects.all()
    context={
        'object':qs
    }
    template="detail.html"
    return render(request,template,context)



def Datat(request):
    form2 = Data_taking(request.POST or None)
    if form2.is_valid():
        first_name = (form2.cleaned_data.get("first_name"))
        last_name = (form2.cleaned_data.get("last_name"))
        email = (form2.cleaned_data.get("email"))
        note = (form2.cleaned_data.get("note"))
        date = (form2.cleaned_data.get("date"))
        time=(form2.cleaned_data.get("time"))
        qs1=AppointmentTimeSlot.objects.all()
        num = ((date.isoweekday() % 7) - 1)

        print(type(num))
        for i in qs1:
            if int(i.appointment_day)==num:
                count=Appointment.objects.filter(time=time, num=(i.appointment_day)).count()
                if count<=6:
                    if Appointment.objects.filter(time=time,num=(i.appointment_day)).exists():
                        status_code = 400
                        message = "The request is not valid."
                        explanation = "This time slot is alwasy buzzy.Chose another slot."
                        return render(request, "timetaking.html", {'form': form2, 'message': message, 'explanation': explanation})
                        # return JsonResponse({'message': message, 'explanation': explanation}, status=status_code)
                    else:
                        user = Appointment.objects.create(first_name=first_name, last_name=last_name,email=email,note=note,
                                              date=date,time=time ,num=(i.appointment_day))
                        user.save()
                        break
                else:
                    status_code = 400
                    message = "The request is not valid."
                    explanation = "Please wiset next day."
                    return render(request, "timetaking.html",{'form': form2, 'message': message, 'explanation': explanation})
                    #return JsonResponse({'message': message, 'explanation': explanation}, status=status_code)



       # user1=AppointmentTimeSlot.objects.create(appointment_day=((date.isoweekday() % 7)-1),appointment_time=time)
       # user1.save()
        print(first_name)
        print(last_name)
        print(email)
        print(note)
        print(date)
        print((date.isoweekday() % 7)-1)
    return render(request, "timetaking.html", {'form': form2})

def Booked(request):
    qs=Appointment.objects.all()
    context={
        'object':qs
    }
    template="Booked.html"
    return render(request,template,context)