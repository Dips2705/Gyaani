from django.shortcuts import render,redirect
from django.views import generic
from django.views.generic import View
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .forms import UserForm
from django.http import HttpResponse 
from django.contrib.auth import authenticate,login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm

@login_required
def home(request):
    return render(request, 'core/home.html')

class UserFormView(View):
	form_class = UserForm
	template_name='core/registration_form.html'

	def get(self, request):
		form=self.form_class(None)
		return render(request, self.template_name,{'form': form})

	def post(self, request):
		form=self.form_class(request.POST)

		if form.is_valid():
			user = form.save(commit=False)
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user.set_password(password)
			user.save()

			user=authenticate(username=username, password=password)

			if user is not None:
				if user.is_active:
					login(request,user)
					return redirect('core:index')
		return render(request,self.template_name,{'form': form})


