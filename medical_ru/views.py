from django.shortcuts import render, get_object_or_404
from medical_ru.models import *


def home_page(request):
    services = Service2.objects.all()
    features = Feature2.objects.all()
    contact = Contact2.objects.first()
    internet = Internet2.objects.all()

    ctx = {
        "services": services,
        "features": features,
        "contact": contact,
        'internet': internet
    }
    return render(request, "medical/index.html", ctx)


def about(request):
    mission = Mission2.objects.first()
    points = MissionPoint2.objects.all()
    stats = Statistic2.objects.all()
    ctx = {
        "mission": mission,
        "points": points,
        "stats": stats,
        "values": Value2.objects.all(),
        "achievements": Achievement2.objects.all(),
        "members": Member2.objects.all(),
        "histories": History2.objects.all().order_by('year'),
        "contact": Contact2.objects.first(),
        "internet": Internet2.objects.all(),
    }
    return render(request, "medical/about.html", ctx)


def manufacturing_page(request):
    overview = ManufacturingOverview2.objects.first()
    lines = ProductionLine2.objects.all()
    stats = ManufacturingStat2.objects.all()
    contact = Contact2.objects.first()
    internet = Internet2.objects.all()
    return render(request, "medical/manufacturing.html", {
        "overview": overview,
        "stats": stats,
        "lines": lines,
        "contact": contact,
        'internet': internet
    })


def partners_page(request):
    partners = Partner2.objects.all()
    benefits = PartnershipBenefit2.objects.all()
    contact = Contact2.objects.first()
    internet = Internet2.objects.all()
    return render(request, "medical/partners.html", {
        "partners": partners,
        "benefits": benefits,
        "contact": contact,
        'internet': internet
    })


def gallery_page(request):
    categories = GalleryCategory2.objects.all()
    galleries = Gallery2.objects.all()
    contact = Contact2.objects.first()
    internet = Internet2.objects.all()
    ctx = {
        "categories": categories,
        "galleries": galleries,
        "contact": contact,
        'internet': internet
    }

    return render(request, "medical/gallery.html", ctx)


def product_list(request):
    categories = ProductCategory2.objects.all()
    products = Product2.objects.all()
    features = ProductFeature2.objects.all()
    contact = Contact2.objects.first()
    internet = Internet2.objects.all()

    return render(request, "medical/products.html", {
        "categories": categories,
        "products": products,
        "features": features,
        "contact": contact,
        'internet': internet
    })


def product_detail(request, pk):
    product = get_object_or_404(Product2, pk=pk)
    related_products = Product2.objects.filter(category=product.category).exclude(id=product.id)[:3]
    contact = Contact2.objects.first()
    internet = Internet2.objects.all()

    return render(request, "medical/product_detail.html", {
        "product": product,
        "related_products": related_products,
        "contact": contact,
        'internet': internet
    })


def news_page(request):
    educations = News2.objects.all()
    contact = Contact2.objects.first()
    internet = Internet2.objects.all()
    ctx = {
        "educations": educations,
        "contact": contact,
        'internet': internet
    }
    return render(request, 'medical/news.html', ctx)


def news_detail(request, id):
    education = get_object_or_404(News2, pk=id)
    contact = Contact2.objects.first()
    internet = Internet2.objects.all()
    ctx = {
        'education': education,
        "contact": contact,
        'internet': internet
    }
    return render(request, 'medical/news_detail.html', ctx)
