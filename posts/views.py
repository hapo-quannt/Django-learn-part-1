from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from .models import Post

from django.shortcuts import render
from django.views.generic import ListView
from .models import Post

class ListPostView(ListView):
    model = Post
    template_name = 'posts/list-post.html'  # Đặt template_name ở cấp class, không trong phương thức get()

    def get_queryset(self):
        return Post.objects.all()  # Sử dụng phương thức get_queryset() thay vì ghi đè phương thức get()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = self.get_queryset()  # Thêm danh sách bài viết vào context
        return context


# posts/views.py


...
from django.views.generic import ListView, CreateView
from django.contrib.messages.views import SuccessMessageMixin
from .form import CreatePostForm
...
...
class CreatePostView(SuccessMessageMixin, CreateView):
  template_name = 'posts/create-post.html'
  form_class = CreatePostForm
  success_message = 'Crate Post successfully!'


from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse

class UpdatePostView(SuccessMessageMixin, UpdateView):
  template_name = 'posts/edit-post.html'
  model = Post
  fields = ['name', 'content',]
  success_message = 'Update Post successfully!'

  def get_success_url(self):
    return reverse('posts:list-posts', kwargs={})