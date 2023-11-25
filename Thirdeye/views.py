from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
# from Services.models import Services
# from Services.models import SaveEnquery
# from Home.models import SaveEnquery
from Home.models import FormSubmit



def Homepage(request):
    # This is to make changes in template(Html)
    return render(request,"index.html")

def ThankYou(request):
    # This is to make changes in template(Html)
    return render(request,"ThankYou.html")


def contact(request):
    finalAns=str('0')
    try:
        # n = str(request.GET['name1'])
        #  finalAns = str(request.GET['name1'])
        if request.method=="POST":
            # n = str(request.POST['name'])
            finalAns = str(request.POST['name1'])
            return HttpResponseRedirect("/services/") #This is used to redirect page

    except:
        pass
    return render(request,"contact.html",{'output' : finalAns})

def SaveEnquery(request):
        
        if request.method == 'POST':
        # Handle form submission
            name = request.POST.get('name')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            description = request.POST.get('description')
            en=FormSubmit(name=name, email=email, phone=phone, description=description)
            en.save()
        # return render(request,"contact.html")
            return HttpResponseRedirect("/ThankYou/") #This is used to redirect page

        # else:
        # # Render the form
        #      return render(request,"contact.html")
   

def services(request):
    return render(request,"services.html")

def clients(request):
    return render(request,"clients.html")

def Order(request):
    return render(request,"order.html")



