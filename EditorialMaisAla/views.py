from django.http import HttpResponse
from django.template import Template, Context


def home(request):

    res = open("EditorialMaisAla/Templates/home.html")
    template = Template(res.read())
    res.close()

    cont = Context()
    response = template.render(cont)

    return HttpResponse(response)


def books(request):
    res = open("EditorialMaisAla/Templates/books.html")
    template = Template(res.read())
    res.close()

    cont = Context()
    response = template.render(cont)

    return HttpResponse(response)


def about(request):
    res = open("EditorialMaisAla/Templates/about.html")
    template = Template(res.read())
    res.close()

    cont = Context()
    response = template.render(cont)

    return HttpResponse(response)


def contact(request):
    res = open("EditorialMaisAla/Templates/contact.html")
    template = Template(res.read())
    res.close()

    cont = Context()
    response = template.render(cont)

    return HttpResponse(response)
