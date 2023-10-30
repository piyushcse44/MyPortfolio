from django.shortcuts import render
from django.http import HttpResponse
from .models import Profile,Project,Services

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


def PostForm(request):
    form = request.POST
    form = ModifiedValues(form)
    

    
    
    return HttpResponse("form submitted")
    

    
