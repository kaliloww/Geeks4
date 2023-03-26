from django.shortcuts import render
from .forms import UserRegistrationForm
from django.views import generic
from django.urls import reverse_lazy

# def register(request):
#     if request.method=="POST":
#         user_form= UserRegistrationForm(request.POST)
#         if user_form.is_valid():
#             new_user=user_form.save(commit=False)
#             new_user.set_password(user_form.cleaned_data['password'])
#             new_user.save()
#             return render(request, "registration/register_done.html",{"user": new_user})
#     else:
#         user_form=UserRegistrationForm()
#     return render(request, "registration/register.html", {"form":user_form})

class RegisterView(generic.ListView):
    form_class=UserRegistrationForm
    success_url=reverse_lazy("login")
    template_name = 'registration/register.html'
    def post(self, request,*args, **kwargs):
        user_form= UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user=user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, "registration/register_done.html",{"user": new_user})
        return render(request, "registration/register.html", {"form":user_form})
    