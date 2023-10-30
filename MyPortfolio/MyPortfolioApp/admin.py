from django.contrib import admin
from .models import User,Profile,CompetitivePlateform,AdditionalInfo,Tags,Experience,Project,ContactForm,Services,MySkill

# Register your models here.
admin.site.register(User)
admin.site.register(Profile)
admin.site.register(CompetitivePlateform)
admin.site.register(AdditionalInfo)
admin.site.register(Tags)
admin.site.register(Experience)
admin.site.register(Project)
admin.site.register(ContactForm)
admin.site.register(Services)
admin.site.register(MySkill)