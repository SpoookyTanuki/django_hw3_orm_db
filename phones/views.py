from django.shortcuts import render

from phones.models import Phone


def show_catalog(request):
    template = 'catalog.html'
    phones = Phone.objects.all()

    sort_phones = request.GET.get("sort")
    if sort_phones == "name":
        phones = Phone.objects.all().order_by("name")
    if sort_phones == "min_price":
        phones = Phone.objects.all().order_by("price")
    if sort_phones == "max_price":
        phones = Phone.objects.all().order_by("-price")

    context = {
        "phones": phones
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'

    phones = Phone.objects.all()
    phone_slug = phones.get(slug)
    if phone_slug is not None:
        phones = Phone.objects.all().filter(slug=phone_slug)

    context = {
        "phones": phones
    }
    return render(request, template, context)
