from django import template

register = template.Library()

@register.simple_tag(takes_context=True)
def get_post_display(context, user):
    # Si l'utilisateur actuel est le même que l'utilisateur passé en paramètre
    if user == context['user']:
        return 'vous'
    return user.username
