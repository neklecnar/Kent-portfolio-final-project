from django.shortcuts import render
from KentPortfolio.models import Contact

def base (request):
    return render(request,'base.html')

def about (request):
    return render(request,'about.html')

def portfolio (request):
    return render(request,'portfolio.html')

def contact (request):
    if request.method=='POST':
        fname = request.POST['fname']
        email = request.POST['email']
        message = request.POST['message']

        contact = Contact(fname=fname, email=email, message=message)
        contact.save()
        print("contact form has been submitted")

    return render(request,'contact.html')
