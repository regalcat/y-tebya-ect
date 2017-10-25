from django.core.urlresolvers import reverse
from django.views.generic import TemplateView
from django.http import HttpResponse

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Game

class GameDashboardView(LoginRequiredMixin, TemplateView):

    template_name = "game_dashboard.html"

    def get_context_data(self, **kwargs):
        context = super(GameDashboardView, self).get_context_data(**kwargs)
        context['recent_games'] = Game.objects
        return context
