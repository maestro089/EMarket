from django.shortcuts import render


from main.models import comment_book


def moderator_main(request):

    books = comment_book.objects.all()

    context = {
        'books':books,

        }

    return render(request,"moderator/moderator_main.html",context = context)
