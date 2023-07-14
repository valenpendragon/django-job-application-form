from django.shortcuts import render
from .forms import ApplicationForm
from .models import Form
from django.contrib import messages
from django.core.mail import EmailMessage


def index(request):
    if request.method == "POST":
        form = ApplicationForm(request.POST)
        print(f"form: {form}")
        print(f"form-validation: {form.is_valid()}")
        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            email = form.cleaned_data["email"]
            occupation = form.cleaned_data["occupation"]
            date = form.cleaned_data["date"]
            print(f"first name: {first_name}")
            print(f"last name: {last_name}")
            print(f"email: {email}")
            print(f"occupation: {occupation}")
            print(f"date: {date}")

            Form.objects.create(first_name=first_name, last_name=last_name,
                                occupation=occupation, email=email,
                                date=date)

            message_body = f"A new job application was submitted.\n" \
                           f"Thank you, \n{first_name}"
            email_msg = EmailMessage("Form submission confirmation",
                                     message_body, to=[email])
            email_msg.send()

            messages.success(request, "Form submitted successfully.")
    return render(request, "index.html")


def about(request):
    return render(request, 'about.html')
