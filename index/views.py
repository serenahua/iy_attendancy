from django.shortcuts import render
from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = 'index/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


class CheckInView(TemplateView):
    template_name = 'index/check_in.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


class FastCheckInView(TemplateView):
    template_name = 'index/fast_check_in.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


