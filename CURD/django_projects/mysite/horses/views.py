from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from horses.models import Breed, Horse
from horses.forms import BreedForm

class HorseList(LoginRequiredMixin, View):
    def get(self, request):
        mc = Breed.objects.all().count()
        al = Horse.objects.all()

        ctx = {'breed_count': mc, 'horse_list': al}
        return render(request, 'horses/horse_list.html', ctx)


class BreedView(LoginRequiredMixin, View):
    def get(self, request):
        ml = Breed.objects.all()
        ctx = {'breed_list': ml}
        return render(request, 'horses/breed_list.html', ctx)

class BreedCreate(LoginRequiredMixin, View):
    template = 'horses/breed_form.html'
    success_url = reverse_lazy('horses:all')

    def get(self, request):
        form = BreedForm()
        ctx = {'form': form}
        return render(request, self.template, ctx)

    def post(self, request):
        form = BreedForm(request.POST)
        if not form.is_valid():
            ctx = {'form': form}
            return render(request, self.template, ctx)

        breed = form.save()
        return redirect(self.success_url)

class BreedUpdate(LoginRequiredMixin, View):
    model = Breed
    success_url = reverse_lazy('horses:all')
    template = 'horses/breed_form.html'

    def get(self, request, pk):
        breed = get_object_or_404(self.model, pk=pk)
        form = BreedForm(instance=breed)
        ctx = {'form': form}
        return render(request, self.template, ctx)

    def post(self, request, pk):
        breed = get_object_or_404(self.model, pk=pk)
        form = BreedForm(request.POST, instance=breed)
        if not form.is_valid():
            ctx = {'form': form}
            return render(request, self.template, ctx)

        form.save()
        return redirect(self.success_url)

class BreedDelete(LoginRequiredMixin, View):
    model = Breed
    success_url = reverse_lazy('horses:all')
    template = 'horses/breed_confirm_delete.html'

    def get(self, request, pk):
        breed = get_object_or_404(self.model, pk=pk)
        form = BreedForm(instance=breed)
        ctx = {'breed': breed}
        return render(request, self.template, ctx)

    def post(self, request, pk):
        breed = get_object_or_404(self.model, pk=pk)
        breed.delete()
        return redirect(self.success_url)

class HorseCreate(LoginRequiredMixin, CreateView):
    model = Horse
    fields = '__all__'
    success_url = reverse_lazy('horses:all')


class HorseUpdate(LoginRequiredMixin, UpdateView):
    model = Horse
    fields = '__all__'
    success_url = reverse_lazy('horses:all')


class HorseDelete(LoginRequiredMixin, DeleteView):
    model = Horse
    fields = '__all__'
    success_url = reverse_lazy('horses:all')
