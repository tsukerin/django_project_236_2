from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import DeleteView, CreateView, DetailView, UpdateView, ListView
from mysite.anketa.models import Professions, Skills, Questions, Model_prof, Blank, Human

item_for_page = 15

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class ProfessionsView(ListView):
    model = Professions
    context_object_name = 'professions_list'
    success_url = reverse_lazy('anketa:professions')

    paginate_by = item_for_page

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class SkillsView(ListView):
    model = Skills
    context_object_name = 'skills_list'
    success_url = reverse_lazy('anketa:skills')

    paginate_by = item_for_page

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class QuestionsView(ListView):
    model = Questions
    context_object_name = 'questions_list'
    success_url = reverse_lazy('anketa:questions')

    paginate_by = item_for_page

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class ModelProfView(ListView):
    model = Model_prof
    context_object_name = 'modelprof_list'
    success_url = reverse_lazy('anketa:modelprof')

    paginate_by = item_for_page

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class BlankView(ListView):
    model = Blank
    context_object_name = 'blank_list'
    success_url = reverse_lazy('anketa:blank')

    paginate_by = item_for_page

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class HumanView(ListView):
    model = Human
    context_object_name = 'human_list'
    success_url = reverse_lazy('anketa:human')

    paginate_by = item_for_page
