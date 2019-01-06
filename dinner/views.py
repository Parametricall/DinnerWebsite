from django.forms import modelformset_factory
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.views import View

from dinner.forms import AddOptions
from dinner.models import Options


def index(request):
    return render(request, 'dinner/home_page.html', {})


class Homepage(View):
    template_name = 'dinner/home_page.html'

    dinner_formset = modelformset_factory(
        fields=('dinner_name',),
        extra=0,
        model=Options
    )

    def get(self, request):
        formset = self.dinner_formset()
        context = {'formset': formset}
        return render(request, self.template_name, context)


class AddDin(View):
    template_name = 'dinner/add_dinner.html'
    form_class = AddOptions

    def get(self, request):
        form = self.form_class()
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('dinner:index'))

        context = {'form': form}
        return render(request, self.template_name, context)
