from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings


def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            email_subject = form.cleaned_data["subject"]
            email_message = form.cleaned_data['message']
            send_mail(email_subject, email_message,
                      settings.DEFAULT_FROM_EMAIL, ['abhigupta7b@gmail.com'])
            messages.success(request, 'Successfully Sent The Message!')

    form = ContactForm()
    context = {'form': form}
    return render(request, 'base/index.html', context)
