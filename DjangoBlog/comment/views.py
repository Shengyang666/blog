from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from article.models import ArticlePost
from . import models


# 文章评论
@login_required(login_url='/userprofile/login/')
def post_comment(request, article_id):
    article = get_object_or_404(ArticlePost, id=article_id)
    if request.method == 'POST':
        new_comment_body = request.POST.get('body')
        new_article_user = request.user
        models.Comment.objects.create(article=article, body=new_comment_body,user=new_article_user)
        return redirect(article)
    else:
        return HttpResponse("发表评论仅接受POST请求。")