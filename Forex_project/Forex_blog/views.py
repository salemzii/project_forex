from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from django.views.generic import DetailView, CreateView
from .forms import CommentForm
from django.urls import reverse_lazy

def show_welcome(request):
    content = Post.objects.all()
    context = {
        'content': content,
    }
    return render(request, 'forex_blog\welcom.html', context)



class TopicView(DetailView):
    model = Post
    template_name = 'Forex_blog/Course.html'
    context_object_name = 'post'

class AddCommentView(CreateView):
    model = Comment
    template_name = 'Forex_blog/addComment.html'
    form_class = CommentForm

    def form_valid(self, form):
        print(self.kwargs['pk'])
        print(type(self.kwargs['pk']))
        form.instance.comment_id = self.kwargs['pk']
        return super().form_valid(form)

    success_url = reverse_lazy('welcome_page')

