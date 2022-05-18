from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post

# Renders and returns the Home page, including getting all posts from the database.
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'projectunit/home.html', context)


# Manages and sorts all posts according to the date posted, to be able to list them in the home page.
class PostListView(ListView):
    model = Post
    template_name = 'projectunit/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']

# Enables viewing post details.
class PostDetailView(DetailView):
    model = Post

# Handles the creation of posts. 
# Django crispy forms handles the form and inputs required for the fields from the PostCreateView and display them to the user.
# Corresponding template: post_form.
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

# Handles editing and updating of posts. 
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

# Handles the deletion of posts.
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

# Renders About page.
def about(request):
    return render(request, 'projectunit/about.html', {'title': 'About'})
