from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import Answers, Sertif

item_for_page = 15

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class AnswersView(ListView):
    model = Answers
    context_object_name = 'answers_list'
    success_url = reverse_lazy('testik:answers')

    paginate_by = item_for_page

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class AnswersCreate(CreateView):
    model = Answers
    template_name = 'testik/answers_form.html'
    fields = '__all__'
    success_url = reverse_lazy('testik:answers')

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class AnswersUpdate(UpdateView):
    model = Answers
    template_name = 'testik/answers_form.html'
    fields = '__all__'
    success_url = reverse_lazy('testik:answers')

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class AnswersDelete(DeleteView):
    model = Answers
    success_url = reverse_lazy('testik:answers')

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class SertifView(ListView):
    model = Sertif
    context_object_name = 'sertif_list'
    success_url = reverse_lazy('testik:sertif')

    paginate_by = item_for_page

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class SertifCreate(CreateView):
    model = Sertif
    template_name = 'testik/sertif_form.html'
    fields = '__all__'
    success_url = reverse_lazy('testik:sertif')

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class SertifUpdate(UpdateView):
    model = Sertif
    template_name = 'testik/sertif_form.html'
    fields = '__all__'
    success_url = reverse_lazy('testik:sertif')

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class SertifDelete(DeleteView):
    model = Sertif
    success_url = reverse_lazy('testik:sertif')

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class SertifDetail(DetailView):
    model = Sertif
    template_name = 'testik/sertif_form.html'
    fields = '__all__'
    success_url = reverse_lazy('testik:sertif')