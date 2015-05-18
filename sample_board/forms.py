# -*- coding: utf-8 -*-
from django import forms
from sample_board.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
