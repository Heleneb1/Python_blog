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
    elif not user:
        return 'anonyme'
    return getattr(user, 'username', 'inconnu')

from django.utils.dateparse import parse_datetime

@register.filter
def get_posted_at_display(created_at):
    # Convertir la chaîne en datetime si nécessaire
    if isinstance(created_at, str):
        created_at = parse_datetime(created_at)
    
    # Vérifie si created_at est une date valide
    if not created_at:
        return "Date invalide"
    
    # Calculer le nombre de secondes depuis la création
    seconds_ago = (timezone.now() - created_at).total_seconds()
    
    # Retourner un message basé sur l'ancienneté de la date
    if seconds_ago <= HOUR:
        return f'Publié il y a {int(seconds_ago // MINUTE)} minutes.'
    elif seconds_ago <= DAY:
        return f'Publié il y a {int(seconds_ago // HOUR)} heures.'
    
    return f'Publié le {created_at.strftime("%d %b %y à %Hh%M")}'