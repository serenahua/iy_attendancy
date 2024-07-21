from django.shortcuts import render
from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = 'manage/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


class VendorListView(TemplateView):
    template_name = 'manage/vendor_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


class VendorFormView(TemplateView):
    template_name = 'manage/vendor_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


class EventListView(TemplateView):
    template_name = 'manage/event_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


class EventFormView(TemplateView):
    template_name = 'manage/event_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


class EventVendorListView(TemplateView):
    template_name = 'manage/event_vendor_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


