from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from accountapp.forms import AccountUpdateForm
from accountapp.models import HelloWorld


# Create your views here.

def hello_world(request):

    if request.user.is_authenticated:

        if request.method == "POST":

            temp = request.POST.get('hello_world_input')

            new_hello_world=HelloWorld()
            new_hello_world.text = temp
            new_hello_world.save()



            return HttpResponseRedirect(reverse('accountapp:hello_world'))
        else:
            hello_world_list = HelloWorld.objects.all()
            return render(request, 'practice/hello_world.html',context={'hello_world_list': hello_world_list})

    else :
        return HttpResponseRedirect(reverse('accountapp:login'))



class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'practice/create.html'


class AccountDetailView(DetailView):
    model = User
    template_name = 'practice/detail.html'
    context_object_name = 'target_user'


class AccountUpdateView(UpdateView):
    model = User
    form_class = AccountUpdateForm
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'practice/update.html'
    context_object_name = 'target_user'

    def get(self,*args,**kwargs):
        if self.request.user.is_authenticated and self.get_object() == self.request.user:
            return super().get(*args,**kwargs)
        else:
            return HttpResponseForbidden
    def post(self,*args,**kwargs):
        if self.request.user.is_authenticated and self.get_object() == self.request.user:
            return super().post(*args,**kwargs)
        else:
            return HttpResponseForbidden
class AccountDeleteView(DeleteView):
    model = User
    success_url = reverse_lazy('accountapp:login')
    template_name = 'practice/delete.html'
    context_object_name = 'target_user'

    def get(self,*args,**kwargs):
        if self.request.user.is_authenticated and self.get_object() == self.request.user:
            return super().get(*args,**kwargs)
        else:
            return HttpResponseForbidden
    def post(self,*args,**kwargs):
        if self.request.user.is_authenticated and self.get_object() == self.request.user:
            return super().post(*args,**kwargs)
        else:
            return HttpResponseForbidden



