from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.urls import reverse_lazy

from posts.models import Post


def hello(request):
    # my_list = [1, 2, 3, 4]
    body = "<h1>Hello</h1>"
    # body = """
    # <!DOCTYPE html>
    #     <html>
    #         <head>
    #             <title>Geek TEST</title>
    #         </head>
    #         <body>
    #
    #             <h1>Заголовок первого уровня</h1>
    #             <p>Параграф</p>
    #
    #         </body>
    #     </html>
    # """
    headers = {
        "name": "Alex",
    }
    # "Content-Type": "application/vnd.ms-excel",
    # "Content-Disposition": "attachment; filename=file.xls"}
    return HttpResponse(body, headers=headers, status=500)


# def get_index(request):
#     posts = Post.objects.filter(status=True)
#     context = {
#         "title": "Main page",
#         "posts": posts,
#     }
#     return render(request, "posts/index.html", context=context)

class IndexView(generic.ListView):
    queryset = Post.objects.filter(status=True)
    context_object_name = "posts"
    # model = Post
    template_name = "posts/index.html"


class PostDetailView(generic.DetailView):
    model = Post
    context_object_name = "post"
    template_name = "posts/post_detail.html"


class PostCreateView(generic.CreateView):
    model = Post
    template_name = "posts/post_create.html"
    fields = ["title", "content"]
    success_url = reverse_lazy("index-page")


class PostUpdateView(generic.UpdateView):
    model = Post
    template_name = "posts/post_update.html"
    fields = ["title", "content"]
    success_url = reverse_lazy("index-page")


class PostDeleteView(generic.DeleteView):
    model = Post
    success_url = reverse_lazy("index-page")


class AboutView(generic.TemplateView):
    template_name = "posts/about.html"
    extra_context = {
        "title": "Страница о нас",
    }


# CRUD - Create, Retrieve, Update, Delete

# def get_about(request):
#     context = {
#         "title": "Страница о нас",
#     }
#     return render(request, "posts/about.html", context=context)


def get_contacts(request):
    return render(request, "posts/contacts.html", {"title": "Контакты"})


def post_create(request):
    return render(request, "posts/post_create.html")


def post_delete(request):
    return render(request, "posts/post_delete.html")


def post_update(request):
    return render(request, "posts/post_update.html")