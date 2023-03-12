from django.shortcuts import render
from django.http import HttpResponse

def hello(request):
    # mylist  = [1,2,3,4]
    body = "<h1>Hello<h1>"
    # body = """
    # <!DOCTYPE html>
    #     <html>
    #     <head>
    #         <title>Geek Test</title>
    #     </head>
    #     <body>

    #         <h1>Зaголовок первого уровня</h1>
    #         <p>Параграф</p>

    #     </body>
    #     </html>
    #  """
    headers = {"names": "Alex"}

# "Content-Type":"applivcation/vnd.ms-excel",
# "Content-Dispasition": "attachment"}
    return HttpResponse(body, headers=headers, status=300)

def get_index(request):

    # print (request.__dict__)
    # if request.method == "GET":
    #     return HttpResponse("Главная страница")
    # else:
    #     return HttpResponse("Не тот метод запроса")
    return render(request, "posts/index.html", context=None)

def get_contacts(request):
    return render(request, "posts/contacts.html", context=None)

def get_about(request):
    return render(request, "posts/about.html", context=None)