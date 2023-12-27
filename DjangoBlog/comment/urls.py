# 引入path
from django.urls import path
# 引入views.py
from . import views

# 正在部署的应用的名称
app_name = 'comment'

urlpatterns = [
    # # path函数将url映射到视图
    # 发表评论
    path('post-comment/<int:article_id>/', views.post_comment, name='post_comment'),
]
