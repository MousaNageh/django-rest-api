from django.urls import path
# from apiapp.views import allArticles, article_detail
from apiapp.views import ArticleView, ArticleDetail
from rest_framework.urlpatterns import format_suffix_patterns
app_name = "myapp"
urlpatterns = [
    # path("all/", allArticles, name='all'),
    # path("article/<int:pk>", article_detail, name="detail")
    path("all/", ArticleView.as_view(), name='all'),
    path("art/<int:pk>", ArticleDetail.as_view(), name='art'),
]
urlpatterns = format_suffix_patterns(urlpatterns)
