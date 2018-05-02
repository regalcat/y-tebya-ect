from django.core.urlresolvers import reverse
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.db.models import Q

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Game
from ..users.models import User

class GameDashboardView(LoginRequiredMixin, TemplateView):

    template_name = "game_dashboard.html"

    def get_context_data(self, **kwargs):
        context = super(GameDashboardView, self).get_context_data(**kwargs)
        user = User.objects.get(username=kwargs['username'])
        context['recent_games'] = Game.objects.filter(Q(player1=user) | Q(player2=user))
        return context
