from django import template
from django.utils import timezone

MINUTE = 60
HOUR = 60 * MINUTE
DAY = 24 * HOUR

register = template.Library()

@register.simple_tag(takes_context=True)
def get_post_display(context, user):
    # Si l'utilisateur actuel est le même que l'utilisateur passé en paramètre
    if user == context['user']:
        return 'vous'
    elif not user :
        return 'anonyme'
    return user

@register.filter
def get_posted_at_display(created_at):
    seconds_ago = (timezone.now() - created_at).total_seconds()
    if seconds_ago <= HOUR:
        return f'Publié il y a {int(seconds_ago // MINUTE)} minutes.'
    elif seconds_ago <= DAY:
        return f'Publié il y a {int(seconds_ago // HOUR)} heures.'
    return f'Publié le {created_at.strftime("%d %b %y à %Hh%M")}'
    
