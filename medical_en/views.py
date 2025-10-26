from django.shortcuts import render, get_object_or_404
from medical_en.models import *



def home_page(request):
    services = Service1.objects.all()
    features = Feature1.objects.all()
    contact = Contact1.objects.first()
    internet = Internet1.objects.all()

    ctx = {
        "services": services,
        "features": features,
        "contact": contact,
        'internet': internet
    }
    return render(request, "medical_en/index.html", ctx)


def about(request):
    mission = Mission1.objects.first()
    points = MissionPoint1.objects.all()
    stats = Statistic1.objects.all()
    ctx = {
        "mission": mission,
        "points": points,
        "stats": stats,
        "values": Value1.objects.all(),
        "achievements": Achievement1.objects.all(),
        "members": Member1.objects.all(),
        "histories": History1.objects.all().order_by('year'),
        "contact": Contact1.objects.first(),
        "internet": Internet1.objects.all(),
    }
    return render(request, "medical_en/about.html", ctx)


def manufacturing_page(request):
    overview = ManufacturingOverview1.objects.first()
    lines = ProductionLine1.objects.all()
    stats = ManufacturingStat1.objects.all()
    contact = Contact1.objects.first()
    internet = Internet1.objects.all()
    return render(request, "medical_en/manufacturing.html", {
        "overview": overview,
        "stats": stats,
        "lines": lines,
        "contact": contact,
        'internet': internet
    })


def partners_page(request):
    partners = Partner1.objects.all()
    benefits = PartnershipBenefit1.objects.all()
    contact = Contact1.objects.first()
    internet = Internet1.objects.all()
    return render(request, "medical_en/partners.html", {
        "partners": partners,
        "benefits": benefits,
        "contact": contact,
        'internet': internet
    })


def gallery_page(request):
    categories = GalleryCategory1.objects.all()
    galleries = Gallery1.objects.all()
    contact = Contact1.objects.first()
    internet = Internet1.objects.all()
    ctx = {
        "categories": categories,
        "galleries": galleries,
        "contact": contact,
        'internet': internet
    }

    return render(request, "medical_en/gallery.html", ctx)


def product_list(request):
    categories = ProductCategory1.objects.all()
    products = Product1.objects.all()
    features = ProductFeature1.objects.all()
    contact = Contact1.objects.first()
    internet = Internet1.objects.all()

    return render(request, "medical_en/products.html", {
        "categories": categories,
        "products": products,
        "features": features,
        "contact": contact,
        'internet': internet
    })


def product_detail(request, pk):
    product = get_object_or_404(Product1, pk=pk)
    related_products = Product1.objects.filter(category=product.category).exclude(id=product.id)[:3]
    contact = Contact1.objects.first()
    internet = Internet1.objects.all()

    return render(request, "medical_en/product_detail.html", {
        "product": product,
        "related_products": related_products,
        "contact": contact,
        'internet': internet
    })


def news_page(request):
    educations = News1.objects.all()
    contact = Contact1.objects.first()
    internet = Internet1.objects.all()
    ctx = {
        "educations": educations,
        "contact": contact,
        'internet': internet
    }
    return render(request, 'medical_en/news.html', ctx)


def news_detail(request, id):
    education = get_object_or_404(News1, pk=id)
    contact = Contact1.objects.first()
    internet = Internet1.objects.all()
    ctx = {
        'education': education,
        "contact": contact,
        'internet': internet
    }
    return render(request, 'medical_en/news_detail.html', ctx)
