
from django.shortcuts import render
from .models import Contact


def contact(request):
    if request.method == 'POST':
        contact = Contact()
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        contact.name = name
        contact.email = email
        contact.subject = subject
        contact.message = message
        print(type(contact.name))
        print(contact.name)

        if name == "" or email == "" or subject =="" or message == "":
            print("Please enter more data")
            return render(request, 'contact.html')
        else:
            contact.save()
            print("Post request recieved")
            context = {
                    'name': contact.name
            }
            return render(request, 'thank-you.html' , context)
    return render(request, 'contact.html')



