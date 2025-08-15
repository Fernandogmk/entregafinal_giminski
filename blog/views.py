from django.shortcuts import render

# Create your views here.
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Page
from .forms import PageForm

class HomeView(TemplateView):
    template_name = 'blog/home.html'

class AboutView(TemplateView):
    template_name = 'blog/about.html'

class PageListView(ListView):
    model = Page
    template_name = 'blog/page_list.html'
    context_object_name = 'pages'

class PageDetailView(DetailView):
    model = Page
    template_name = 'blog/page_detail.html'

class PageCreateView(LoginRequiredMixin, CreateView):
    model = Page
    form_class = PageForm
    template_name = 'blog/page_form.html'
    success_url = reverse_lazy('blog:page_list')

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        obj.save()
        messages.success(self.request, 'Página creada.')
        return super().form_valid(form)

class PageUpdateView(LoginRequiredMixin, UpdateView):
    model = Page
    form_class = PageForm
    template_name = 'blog/page_form.html'
    success_url = reverse_lazy('blog:page_list')

class PageDeleteView(LoginRequiredMixin, DeleteView):
    model = Page
    template_name = 'blog/page_confirm_delete.html'
    success_url = reverse_lazy('blog:page_list')
