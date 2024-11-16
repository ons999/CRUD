from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegisterForm
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template

#################### index ####################################### 
def index(request):
    return render(request, 'user/index.html', {'title': 'index'})

########### register here ##################################### 
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')

            ######################### mail system #################################### 
            htmly = get_template('user/Email.html')
            d = {'username': username}
            subject, from_email, to = 'Welcome', 'your_email@gmail.com', email
            html_content = htmly.render(d)
            msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            try:
                msg.send()
            except Exception as e:
                messages.error(request, f'Error sending email: {str(e)}')
            ################################################################## 
            messages.success(request, 'Your account has been created! You are now able to log in.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'user/register.html', {'form': form, 'title': 'Register Here'})


################ login forms ################################################### 
def Login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not username or not password:
            messages.error(request, 'Please enter both username and password.')
        else:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome {username}!!')
                return redirect('index')
            else:
                messages.info(request, 'Invalid username or password.')

    form = AuthenticationForm()
    return render(request, 'user/login.html', {'form': form, 'title': 'Log In'})
