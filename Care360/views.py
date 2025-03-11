from django.views.generic import View
from django.shortcuts import redirect


class HomePageView(View):
    """ Home view """
    template_name = 'dashboard.html'

    def get(self, request, *args, **kwargs):
        return redirect('dashboard:dashboard')
