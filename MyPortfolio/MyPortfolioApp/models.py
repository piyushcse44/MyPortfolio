from django.db import models
import uuid

# Create your models here.

class User(models.Model):
    Id = models.UUIDField(default=uuid.uuid4,editable=False,primary_key=True,unique=True)
    FirstName = models.CharField(max_length=200,null=False,blank=False,default="Piyush")
    LastName =models.CharField(max_length=200,null=False,blank=False,default="Kumar")
    Email = models.EmailField(max_length=200,null=False,blank=False,default="piyushkumarcse44@gmail.com")
    PhoneNo = models.CharField(max_length=15,null=False,blank=False,default="1234567890")
    Photo = models.ImageField(null=False,blank=False,default='images/default.png')
    BirthDay = models.DateField(null=False,blank=False,default="2002-06-29")
    LinkedinProfile = models.URLField(null=False,blank=False,default="www.linkedin.com")
    GithubProfile = models.URLField(null=False,blank=False,default="www.github.com")
    Twitter = models.URLField(null=False,blank=False,default="www.Twitter.com")
    Instagram = models.URLField(null=False,blank=False,default="www.Instagram.com")
    Pinterest = models.URLField(null=False,blank=False,default="www.Pintrest.com")
    Youtube =  models.URLField(null=False,blank=False,default="www.Yoube.com")
    Cv = models.URLField(null=False,blank=False,default="https://drive.google.com/file/d/1DZLy7mRCW3ocaPoy_stLyxq5VrnSmbEF/view?usp=drive_link")
    CollegeName = models.CharField( max_length=200,null=False,blank=False,default="GoodCollege")
    CollegeAddress = models.CharField(max_length=200,null=False,blank=False,default="india")
    CollegeDegree = models.CharField(max_length=200,null=True,blank=True,default="B.tech")
    CollegeStream = models.CharField(max_length=200,null=False,blank=False,default='Computer Science')
    CollegePassingYear = models.CharField(max_length=200,null=False,blank=False,default="2024")

    def __str__(self):
        return self.FirstName




class CompetitivePlateform(models.Model):
    Id = models.UUIDField(default=uuid.uuid4,primary_key=True,editable=False,unique=True)
    Name = models.CharField(max_length=200,null=False,blank=False,default="Codechef")
    Photo = models.ImageField(null=False,blank=False,default="images/default.png")
    UserId = models.CharField(max_length=200,null=False,blank=False,default="piyush_cse")
    User = models.ForeignKey(User,on_delete=models.PROTECT)
    ProfileLink = models.URLField(null=False,blank=False,default="www.codechef.com")

    def __str__(self):
        return self.Name

class AdditionalInfo(models.Model):
    Id = models.IntegerField(primary_key=True,editable=False,unique=True)
    ProjectFinished = models.IntegerField(null=False,blank=False,default=10)
    DigitalAward = models.IntegerField(null=False,blank=False,default=10)
    YearOfExperience = models.IntegerField(null=False,blank=False,default=10)
    HappyCustomer = models.IntegerField(null=False,blank=False,default=10)

class Tags(models.Model):
    Id = models.UUIDField(default=uuid.uuid4,primary_key=True,editable=False,unique=True)
    Name = models.CharField(max_length=200,null=False,blank=False,default="Django")

    def __str__(self):
        return self.Name
    

class MySkill(models.Model):
    Id = models.UUIDField(default=uuid.uuid4,primary_key=True,editable=False,unique=True)
    Name = models.CharField(max_length=200,null=False,blank=False,default="c++")
    logo = models.ImageField(null=False,blank=False,default="#")

    def __str__(self):
        return self.Name



class Experience(models.Model):
    Id = models.UUIDField(default=uuid.uuid4,primary_key=True,editable=False,unique=True)
    CompanyName = models.CharField(max_length=200,null=False,blank=False,default="Codechef")
    CompanyLogo = models.ImageField(null=False,blank=False,default="images/default.png")
    Position = models.CharField(max_length=200,null=False,blank=False,default="DoubtSolver")
    Location = models.CharField(max_length=200,null=False,blank=False,default="Delhi")
    Start_Duration = models.DateField(null=False,blank=False,default="2023-02-02")
    End_Duration = models.DateField(null=False,blank=False,default="2023-06-02")
    Tags = models.ManyToManyField(Tags)
    Description = models.TextField()
    Certificate = models.ImageField(null=False,blank=False,default="images/default.png")

    def __str__(self):
        return self.CompanyName


class Services(models.Model):
    Id = models.UUIDField(default=uuid.uuid4,primary_key=True,editable=False,unique=True)
    Name = models.CharField(max_length=200,null=False,blank=False,default="Website")
    Price = models.CharField(max_length=30,null=False,blank=False,default="$50")
    logo = models.CharField(max_length=200,null=False,blank=False,default="bi-globe")
    Description = models.TextField(null=True,blank=True)

    DiscoveryMore = models.URLField(null=False,blank=False,max_length=200,default="wwww.wikipedia.com")

    def __str__(self):
        return self.Name


class Profile(models.Model):

    Id = models.UUIDField(default=uuid.uuid4,primary_key=True,editable=False,unique=True)
    GrettingMsg = models.CharField(max_length=200,null=False,blank=False,default="Hello friend!")
    About = models.CharField(max_length=200,null=False,blank=False,default="I am a professional Full stack web developer. Feel free to get in touch with me. ")
    User = models.OneToOneField(User,on_delete=models.PROTECT)
    MySkill = models.ManyToManyField(MySkill)
    Experience = models.ManyToManyField(Experience,default=None)
    Services = models.ManyToManyField(Services)
    OpenToWork = models.CharField(max_length=200,null=False,blank=False,default="I’m available for freelance work.")
    subject = models.CharField(max_length=200,null=False,blank=False,default="a little bit about Joshua")
    Description = models.TextField(null=True,blank=True)
    FrontPhoto = models.ImageField(null=False,blank=False,default="images/default.png")
    FrontPhoto1=models.ImageField(null=False,blank=FrontPhoto,default="images/default.png")
    AdditionalInfo = models.OneToOneField(AdditionalInfo,on_delete=models.PROTECT)


    def __str__(self):
        return self.User.FirstName





class Project(models.Model):
    Id = models.UUIDField(default=uuid.uuid4,editable=False,primary_key=True,unique=True)
    Title = models.CharField(max_length=200,null=False,blank=False,default="Directory For Developer")
    Profile = models.ForeignKey(Profile,on_delete=models.PROTECT)
    brand = models.CharField(max_length=200,null=False,blank=False,default="")
    TeamSize = models.IntegerField(null=False,blank=False,default=4)
    Role = models.CharField(max_length=200,null=False,blank=False,default="Backend Developer")
    Start_Duration = models.DateField(null=False,blank=False,default="2023-02-02")
    End_Duration = models.DateField(null=False,blank=False,default="2023-06-02")
    Tags = models.ManyToManyField(Tags)
    ProjectImage = models.ImageField(blank=False,null=False,default="images/defaule.png")
    Description = models.TextField()
    GithubLink = models.URLField(max_length=200,default="github.com")
    LiveLink = models.URLField(max_length=200,default="Pythonanywhere.com")

    def __str__(self):
        return self.Title
    


class ContactForm(models.Model):
    Id = models.UUIDField(default=uuid.uuid4,editable=False,primary_key=True,unique=True)
    FirstName = models.CharField(max_length=200,null=False,blank=False,default="Piyush")
    LastName =models.CharField(max_length=200,null=False,blank=False,default="Kumar")
    Email = models.EmailField(max_length=200,null=False,blank=False,default="piyushkumarcse44@gmail.com") 
    Services = models.ManyToManyField(Services)
    Description = models.TextField()

    def __str__(self):
        return self.FirstName
    

    







    

    
    



