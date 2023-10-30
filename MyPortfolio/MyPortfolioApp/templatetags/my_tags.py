from django import template
from MyPortfolioApp.models import Profile

register = template.Library()


@register.simple_tag(name='increase')
def increase(x):
    x+=1
    return x

@register.simple_tag(name='IdName')
def IdName(x):
    x=str(x)
    return "inlineCheckbox"+x
    

    