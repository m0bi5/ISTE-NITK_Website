from django import template

register = template.Library()

@register.filter(name='has_group')
def has_group(user, group_name):
    a = user.groups.filter(name='Core').exists()
    if a:
        print(user.groups.all())
    else:
        print(user.groups.all())
    return a
