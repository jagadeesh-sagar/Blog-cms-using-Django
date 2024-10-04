from django.views.generic import ListView, DetailView, TemplateView
from .models import Post, HomePost


class Home(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = HomePost.objects.all()
        return context


class Blog(ListView):
    model = Post
    template_name = 'blog.html'
    context_object_name = 'posts'


class PostDetailView(DetailView):
    model = Post
    template_name = 'index.html'
    context_object_name = 'post'

