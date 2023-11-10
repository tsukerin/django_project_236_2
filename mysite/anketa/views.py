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
	success_url = reverse_lazy('anketa:ProfessionsView')

	paginate_by = item_for_page
	def get_context_data(self, *, object_list=None, **kwargs):
		context = super(ProfessionsView,self).get_context_data(**kwargs)
		context['sometry'] = self.model._meta.verbose_name_plural
		context['col1name'] = self.model._meta.get_field("title").verbose_name
		context['collastname'] = 'Cервисы'
		return context

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class ProfessionUpdate(UpdateView):
	model = Professions
	template_name_suffix = '_update_form'
	fields = '__all__'
	success_url = '/anketa/professions/'

	def get_context_data(self, *, object_list=None, **kwargs):
		context = super(ProfessionUpdate,self).get_context_data(**kwargs)
		context['sometry'] = self.model._meta.verbose_name
		context['slovar'] = {'title'}
		context['hidenslovar'] = {'id'}
		context['dopslovar'] = {'updated_at','erem','edesc','created_at'}
		context['model'] = self.model
		return context

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class ProfessionDetail(DetailView):
	model = Professions
	context_object_name = 'profession_one'
	success_url = '/anketa/professions/'

	def get_context_data(self, *, object_list=None, **kwargs):
		context = super(ProfessionDetail,self).get_context_data(**kwargs)
		context['sometry'] = self.model._meta.verbose_name
		context['slovar'] = {'title'}
		context['hidenslovar'] = {'id'}
		context['dopslovar'] = {'updated_at','erem','edesc','created_at'}
		context['model'] = self.model
		return context

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class ProfessionCreate(CreateView):
	model = Professions
	context_object_name = 'profession_one'
	success_url = '/anketa/professions/'

	template_name_suffix = '_create_form'
	fields = '__all__'
	def get_context_data(self, *, object_list=None, **kwargs):
		context = super(ProfessionCreate,self).get_context_data(**kwargs)
		context['sometry'] = self.model._meta.verbose_name
		context['model'] = self.model
		context['slovar'] = {'title'}
		context['hidenslovar'] = {'id'}
		context['dopslovar'] = {'updated_at','erem','edesc','created_at'}
		return context

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class ProfessionDelete(DeleteView):
	model = Professions
	success_url = '/anketa/professions/'

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class SkillsView(ListView):
	model = Skills
	context_object_name = 'skills_list'
	success_url = reverse_lazy('anketa:SkillsView')

	paginate_by = item_for_page
	def get_context_data(self, *, object_list=None, **kwargs):
		context = super(SkillsView,self).get_context_data(**kwargs)
		context['sometry'] = self.model._meta.verbose_name_plural
		context['col1name'] = self.model._meta.get_field("title").verbose_name
		context['collastname'] = 'Cервисы'
		return context

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class SkillsUpdate(UpdateView):
	model = Skills
	template_name_suffix = '_update_form'
	fields = '__all__'
	success_url = '/anketa/skills/'

	def get_context_data(self, *, object_list=None, **kwargs):
		context = super(SkillsUpdate,self).get_context_data(**kwargs)
		context['sometry'] = self.model._meta.verbose_name
		context['slovar'] = {'title'}
		context['hidenslovar'] = {'id'}
		context['dopslovar'] = {'updated_at','erem','edesc','created_at'}
		context['model'] = self.model
		return context

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class SkillsDetail(DetailView):
	model = Skills
	context_object_name = 'skills_one'
	success_url = '/anketa/skills/'

	def get_context_data(self, *, object_list=None, **kwargs):
		context = super(SkillsDetail,self).get_context_data(**kwargs)
		context['sometry'] = self.model._meta.verbose_name
		context['slovar'] = {'title'}
		context['hidenslovar'] = {'id'}
		context['dopslovar'] = {'updated_at','erem','edesc','created_at'}
		context['model'] = self.model
		return context

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class SkillsCreate(CreateView):
	model = Skills
	context_object_name = 'skills_one'
	success_url = '/anketa/skills/'

	template_name_suffix = '_create_form'
	fields = '__all__'
	def get_context_data(self, *, object_list=None, **kwargs):
		context = super(SkillsCreate,self).get_context_data(**kwargs)
		context['sometry'] = self.model._meta.verbose_name
		context['model'] = self.model
		context['slovar'] = {'title'}
		context['hidenslovar'] = {'id'}
		context['dopslovar'] = {'updated_at','erem','edesc','created_at'}
		return context

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class SkillsDelete(DeleteView):
	model = Skills
	success_url = '/anketa/skills/'

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class QuestionsView(ListView):
	model = Questions
	context_object_name = 'questions_list'
	success_url = reverse_lazy('anketa:QuestionsView')

	paginate_by = item_for_page
	def get_context_data(self, *, object_list=None, **kwargs):
		context = super(QuestionsView,self).get_context_data(**kwargs)
		context['sometry'] = self.model._meta.verbose_name_plural
		context['col1name'] = self.model._meta.get_field("title").verbose_name
		context['col2name'] = self.model._meta.get_field("score").verbose_name
		context['col3name'] = self.model._meta.get_field("skills").verbose_name
		context['collastname'] = 'Cервисы'
		return context

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class QuestionsUpdate(UpdateView):
	model = Questions
	template_name_suffix = '_update_form'
	fields = '__all__'
	success_url = '/anketa/questions/'

	def get_context_data(self, *, object_list=None, **kwargs):
		context = super(QuestionsUpdate,self).get_context_data(**kwargs)
		context['sometry'] = self.model._meta.verbose_name
		context['slovar'] = {'title','score'}
		context['secslovar'] = {'skills'}
		context['hidenslovar'] = {'id'}
		context['dopslovar'] = {'updated_at','erem','edesc','created_at'}
		context['model'] = self.model
		return context

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class QuestionsDetail(DetailView):
	model = Questions
	context_object_name = 'questions_one'
	success_url = '/anketa/questions/'

	def get_context_data(self, *, object_list=None, **kwargs):
		context = super(QuestionsDetail,self).get_context_data(**kwargs)
		context['sometry'] = self.model._meta.verbose_name
		context['slovar'] = {'title','score'}
		context['secslovar'] = {'skills'}
		context['hidenslovar'] = {'id'}
		context['dopslovar'] = {'updated_at','erem','edesc','created_at'}
		context['model'] = self.model
		return context

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class QuestionsCreate(CreateView):
	model = Questions
	context_object_name = 'questions_one'
	success_url = '/anketa/questions/'

	template_name_suffix = '_create_form'
	fields = '__all__'
	def get_context_data(self, *, object_list=None, **kwargs):
		context = super(QuestionsCreate,self).get_context_data(**kwargs)
		context['sometry'] = self.model._meta.verbose_name
		context['model'] = self.model
		context['slovar'] = {'title','score'}
		context['secslovar'] = {'skills'}
		context['hidenslovar'] = {'id'}
		context['dopslovar'] = {'updated_at','erem','edesc','created_at'}
		return context

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class QuestionsDelete(DeleteView):
	model = Questions
	success_url = '/anketa/questions/'

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
