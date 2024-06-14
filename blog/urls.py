from django.urls import path
from blog.views import *
app_name = 'blog'
urlpatterns = [

    path('', blog_view, name= 'blog' ),
    path('<int:pid>', blog_data, name= 'blog-home' ),
    # path('test', blog_test, name= 'test' ),
    path('category/<str:cat_name>', blog_view, name= 'category' ),
    path('tag/<str:tag_name>', blog_view, name= 'tag' ),
    path('author/<str:author_username>', blog_view, name= 'author' ),
    path('search/', search_blog, name= 'search' )


]
