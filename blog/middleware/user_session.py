import datetime
from django.conf import settings
from django.contrib.auth import logout
from django.shortcuts import redirect

class UserSessionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            now = datetime.datetime.now()
            session_start_time = request.session.get('session_start_time')

            if not session_start_time:
                # Définir l'heure de début de session
                request.session['session_start_time'] = now.strftime('%Y-%m-%d %H:%M:%S')
            else:
                # Calculer la durée de session
                session_start_time = datetime.datetime.strptime(
                    session_start_time, '%Y-%m-%d %H:%M:%S'
                )
                session_duration = (now - session_start_time).total_seconds()

                # Vérifier si la durée dépasse la limite
                if session_duration > settings.SESSION_COOKIE_AGE:
                    logout(request)
                    return redirect('login')  # Rediriger vers la page de connexion

        return self.get_response(request)
