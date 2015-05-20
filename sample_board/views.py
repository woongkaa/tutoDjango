# -*- coding: utf-8 -*-
from django.views.generic import ListView, DetailView, CreateView
from sample_board.models import Post, Category


# FBV
# def home(request):
# template_name = 'home.html'
#     posts = Post.objects.all()
#     #print(posts)#테스트 코드였음
#     context_data = {'object_list': posts}
#     return render(request, template_name, context_data)
# def detail(request, pk):
#     template_name = 'detail.html'
#     post = get_object_or_404(Post, id=pk)
#     context_data = {'object':post}
#     return render(request, template_name, context_data)

class PostList(ListView):
    model = Post
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        #context를 super에서 받아와서, 다시 넘기는 것인디...super는 ListView의 그거인듯.
        context = super(PostList, self).get_context_data(**kwargs)
        categories = Category.objects.all()
        context['categories'] = categories
        return context

class PostDetail(DetailView):
    model = Post
    template_name = 'detail.html'


class PostCreate(CreateView):
    #CreateView에는 ModelFormMixin이 들어있다.
    model = Post
    template_name = 'create.html'
    #Django 1.8부터는 field값이 반드시 있어야 함.
    fields = '__all__'