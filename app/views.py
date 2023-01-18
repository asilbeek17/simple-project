from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.generic import ListView, DetailView, FormView
# from app.form import ForgotPasswordForm
from .form import ProductModelForm
from .models import Post
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView

class BlogListView(ListView):
    model = Post
    template_name = 'home.html'

class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

# class BlogCreatview(CreateView):
#     model = Post
#     template_name = 'post_new.html'
#     fields = ['image', 'title', 'body', 'author']
#     success_url = reverse_lazy('home')

    # def form_valid(self, form):
    #     form.save()
    #     return super().form_valid(form)


class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'body']

class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')

def others(reqest):
    return render(reqest, 'others.html')

def CalculatorView(request):
    return render(request, 'calculator/calculator_1.html')

class RegisterePeople(ListView):
    model = User
    template_name = 'registered.html'

# ---------------------------------------------------------------------

def create_product(request):
    print(1121)
    if request.method == "POST":

        form = ProductModelForm(request.POST)
        if form.is_valid():

            form.save()
            success_url = reverse_lazy('home')


    form = ProductModelForm()
    context = {
        'form': form
    }

    return render(request, 'CRUD/create_product.html', context)





# class ForgotPasswordView(FormView):
#     template_name = 'forgot_password.html'
#     success_url = reverse_lazy('home')
#     form_class = ForgotPasswordForm
#
#     def from_valid(self, form):
#         form.send_email()
#         return super().form_valid(form)

