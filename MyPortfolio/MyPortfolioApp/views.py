from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Profile,Project,Services,ContactForm
from .SMTP import SendMail
from .FormSerializer import ContactFormSerailizer


# Create your views here.
def HomePage(request):
    querset = Profile.objects.all()
    if querset == None:
        return render(request,'index.html')
    else:
        queryobj = querset[0]
        project = Project.objects.filter(Profile = queryobj)
        return render(request,'index.html',{'queryobj':queryobj,'project':project})
    
    
def ModifiedValues(form):
    UpdatedList={}
    Name = form.get("name").split(' ')
    FirstName = Name[0]
    UpdatedList["FirstName"]=FirstName
    LastName=""
    for i in range(1,len(Name)):            
        LastName +=Name[i]
        LastName+=' '
    UpdatedList["LastName"]=LastName 
    Email = form.get("email")   
    UpdatedList["Email"]=Email
    Description = form.get("message")
    UpdatedList["Description"]=Description
    __services =[]
    for name in form.getlist("website"):
        __services.append(Services.objects.get(Name =name))   
    UpdatedList["__services"]=__services   
    return UpdatedList




from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist

def PostForm(request):
    try:
        form = request.POST
        form = ModifiedValues(form)

        # Send the initial confirmation email
      #  SendMail(form, form["__services"], form["Description"], "piyushkumarcse44@gmail.com", True)

        # Create a ContactForm instance and set the many-to-many field 'Services'
        contact_form = ContactForm.objects.create(
            FirstName=form["FirstName"],
            LastName=form['LastName'],
            Email=form['Email'],
            Description=form['Description']
        )
        contact_form.Services.set(form["__services"])

        # Send an email to the provided email address
      #  SendMail(form, "", "", form['Email'], False)

        
        return redirect(HomePage)
        

    except ObjectDoesNotExist:
        return HttpResponse("Object not found", status=404)  # Return a 404 response for object not found

    except Exception as e:
        # Handle other exceptions here and return an appropriate response
        return HttpResponse(f"An error occurred: {str(e)}", status=500)  # Return a 500 response for other errors

   


    
    
    
    

    
