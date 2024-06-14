from django.shortcuts import render ,get_object_or_404 , redirect
from blog.models import post , comment
from django.db.models import Q
from datetime import datetime
from django.core.paginator import Paginator, PageNotAnInteger , EmptyPage
from blog.forms import commentForm
from django.http import HttpResponse , HttpResponseRedirect
from django.urls import reverse
# from django.contrib.auth.decorators import login_required
# from timezone import utc

# from django.http import HttpResponse
# def sample(request):
#     return HttpResponse('Hello')
# @login_required(login_url="/accounts/login")
def blog_view(request,cat_name=None , author_username = None , tag_name = None):
    posts = post.objects.filter(status=True)
    if cat_name:
            posts = posts.filter( categories__name = cat_name )
    if author_username:
         posts = posts.filter( author__username = author_username )
         
    if tag_name :
   
          posts = posts.filter(tags__name__in=[tag_name])
    
    try:
         paginator = Paginator(posts,2)
         page_number = request.GET.get("page")
         posts = paginator.get_page(page_number)
    except PageNotAnInteger:
         # If page is not an integer, deliver first page.
         posts = paginator.page(1)
         
    except EmptyPage:
         # If page is out of range (e.g. 9999), deliver last page of results.
         posts = paginator.page(paginator.num_pages)


    context = {'posts': posts}

    return render(request,"blog/blog-home.html" , context)


def blog_data(request, pid):
    if request.method == 'POST':
        form = commentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("/thanks/")
        else:
            return HttpResponse("/kir/")
    
    post_instance = post.objects.get(id=pid, status=True)
    
    if post_instance.login_require and not request.user.is_authenticated:
        return redirect('accounts:login')

    comments = comment.objects.filter(post_id=post_instance.id, approved=True)
    form = commentForm()
    context = {'post': post_instance, "comments": comments, "form": form}
    return render(request, "blog/blog-single.html", context)



def blog_category(request,cat_name,author_username = None):
    posts = post.objects.filter(status=True)
    posts = posts.filter( categories__name = cat_name )
    context = {'posts': posts}
    return render(request,"blog/blog-home.html" , context)

def search_blog(request):
        posts = post.objects.filter(status=True)
        if request.method == "GET" :
        
             if request.GET.get('s'):
                print(request.GET.get('s'))
                
                  
                posts= posts.filter(content__contains=request.GET.get('s'))
        context = {'posts': posts}
        return render(request,"blog/blog-home.html" , context)
     






# def post_list_view(request):
#     published_date_field = 'publish_date'  
#     # دریافت زمان فعلی
#     now = datetime.now()

#     # فیلتر کردن پست ها بر اساس زمان انتشار
#     # فقط پست هایی که تاریخ انتشارشان قبل از زمان فعلی است نمایش داده می شوند
#     posts = post.objects.filter(Q(**{published_date_field: now}))

#     # ...

#     return render(request, 'blog-home.html', {'posts': posts})


def blog_test(request):
    # posts = post.objects.get(id=pid)
    # context = {'posts': posts}
    return render(request,"test.html")


# def post_detail(request, pk):
#     post = post.objects.get(pk=pk)

#     posts = post.objects.all()
#     current_post_index = posts.index(post)

#     has_previous_post = current_post_index > 0
#     has_next_post = current_post_index < len(posts) - 1

#     if has_previous_post:
#         previous_post = posts[current_post_index - 1]

#     if has_next_post:
#         next_post = posts[current_post_index + 1]

#     context = {
#         "post": post,
#         "has_previous_post": has_previous_post,
#         "previous_post": previous_post,
#         "has_next_post": has_next_post,
#         "next_post": next_post,
#     }

#     return render(request, "blog-home.html", context)

