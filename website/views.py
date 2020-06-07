from django.shortcuts import render
from django.core.mail import send_mail
# Create your views here.
def index(request):
    return render(request, 'index.html', {})

def about(request):
    return render(request, 'about.html', {})

def service(request):
    return render(request, 'service.html', {})

def contact(request):
    if request.method =='POST':
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']

        send_mail(
            message_name ,#subject
            message + "\n\n\n Email From: " + message_email, #Body message
            message_email, #From email
            ['chengetai09@yahoo.com'],
            fail_silently=False,
        )
        return render(request, 'contact.html', {'message_name':message_name})
    else:
        return render(request, 'contact.html', {})
