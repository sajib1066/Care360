from django.views.generic import View
from django.shortcuts import render


class HomePageView(View):
    """ Home view """
    template_name = 'dashboard.html'

    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, self.template_name, context)
