# -*- coding: utf-8 -*-
from django.shortcuts import render
from sample_board.models import Post


# view method, called by urls, calling template 'base.html'
def home(request):
    template_name = 'home.html'
    posts = Post.objects.all()
    print(posts)
    context_data = {'object_list': posts}
    return render(request, template_name, context_data)
