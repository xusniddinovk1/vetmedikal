from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from medical_en.models import *
from .forms import *


def login_required_decorator(func):
    return login_required(func, login_url='en-admin:login_page')


def login_page1(request):
    if request.method == "POST":
        phone = request.POST.get("phone_number")
        password = request.POST.get("password")

        user = authenticate(request, phone_number=phone, password=password)
        if user:
            login(request, user)
            return redirect('en-admin:home_page')
        else:
            return render(request, "dashboard_en/login.html", {"error": "Incorrect credentials"})

    return render(request, "dashboard_en/login.html")


@login_required_decorator
def logout_page1(request):
    logout(request)
    return redirect('en-admin:login_page')


@login_required_decorator
def my_profile1(request):
    ctx = {
        'user': request.user,
    }
    return render(request, 'dashboard_en/profile/profile.html', ctx)


@login_required_decorator
def profile_edit1(request):
    user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('en-admin:my_profile')
    else:
        form = ProfileForm(instance=user)

    ctx = {
        'form': form
    }

    return render(request, 'dashboard_en/profile/profile_edit.html', ctx)


@method_decorator(login_required, name='dispatch')
class CustomPasswordChangeView(PasswordChangeView):
    template_name = 'dashboard_en/profile/password_change.html'
    success_url = reverse_lazy('password_change_done')


@login_required_decorator
def home_page1(request):
    products = Product1.objects.all()
    news = News1.objects.all()
    partners = Partner1.objects.all()
    members = Member1.objects.all()
    galleries = Gallery1.objects.all()
    product_categories = ProductCategory1.objects.all()
    statistics = Statistic1.objects.all()
    achievements = Achievement1.objects.all()

    items = [
        {
            "icon": "fa-users",
            "color": "#3b82f6",  # blue-500
            "count": products.count(),
            "label": "Mahsulotlar",
            "chart_data": [products.count(), products.count() // 2, products.count() // 3]
        },
        {
            "icon": "fa-book",
            "color": "#10b981",  # green-500
            "count": news.count(),
            "label": "Yangiliklar",
            "chart_data": [news.count(), news.count() // 2, news.count() // 3]
        },
        {
            "icon": "fa-bell",
            "color": "#ef4444",  # red-500
            "count": partners.count(),
            "label": "Hamkorlar",
            "chart_data": [partners.count(), partners.count() // 2, partners.count() // 3]
        },
        {
            "icon": "fa-star",
            "color": "#facc15",  # yellow-500
            "count": members.count(),
            "label": "Jamoa a'zolari",
            "chart_data": [members.count(), members.count() // 2, members.count() // 3]
        },
        {
            "icon": "fa-users",
            "color": "#3b82f6",  # blue-500
            "count": galleries.count(),
            "label": "Rasmlar",
            "chart_data": [galleries.count(), galleries.count() // 2, galleries.count() // 3]
        },
        {
            "icon": "fa-bell",
            "color": "#ef4444",  # red-500
            "count": product_categories.count(),
            "label": "Mahsulot kategoriyasi",
            "chart_data": [product_categories.count(), product_categories.count() // 2, product_categories.count() // 3]
        },
        {
            "icon": "fa-users",
            "color": "#3b82f6",  # blue-500
            "count": statistics.count(),
            "label": "Statistikalar",
            "chart_data": [statistics.count(), statistics.count() // 2, statistics.count() // 3]
        },
        {
            "icon": "fa-book",
            "color": "#10b981",  # green-500
            "count": achievements.count(),
            "label": "Yutuqlar",
            "chart_data": [achievements.count(), achievements.count() // 2, achievements.count() // 3]
        },
    ]
    return render(request, 'dashboard_en/index.html', {'items': items})


def service_list1(request):
    services = Service1.objects.all()
    return render(request, "dashboard_en/service/list.html", {"services": services})


def service_create1(request):
    form = ServiceForm(request.POST or None, request.FILES or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("en-admin:service_list")
    return render(request, "dashboard_en/service/form.html", {"form": form})


def service_edit1(request, id):
    service = get_object_or_404(Service1, id=id)
    form = ServiceForm(request.POST or None, request.FILES or None, instance=service)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("en-admin:service_list")
    return render(request, "dashboard_en/service/form.html", {"form": form, "service": service})


def service_delete1(request, id):
    service = get_object_or_404(Service1, id=id)
    service.delete()
    return redirect("en-admin:service_list")


# ==============================
# FEATURE VIEWS
# ==============================
def feature_list1(request):
    features = Feature1.objects.all()
    return render(request, "dashboard_en/feature/list.html", {"features": features})


def feature_create1(request):
    form = FeatureForm(request.POST or None, request.FILES or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("en-admin:feature_list")
    return render(request, "dashboard_en/feature/form.html", {"form": form})


def feature_edit1(request, id):
    feature = get_object_or_404(Feature1, id=id)
    form = FeatureForm(request.POST or None, request.FILES or None, instance=feature)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("en-admin:feature_list")
    return render(request, "dashboard_en/feature/form.html", {"form": form, "feature": feature})


def feature_delete1(request, id):
    feature = get_object_or_404(Feature1, id=id)
    feature.delete()
    return redirect("en-admin:feature_list")


# ==============================
# CONTACT VIEWS
# ==============================
def contact_list1(request):
    contacts = Contact1.objects.all()
    return render(request, "dashboard_en/contact/list.html", {"contacts": contacts})


def contact_create1(request):
    form = ContactForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("contact_listen-admin:")
    return render(request, "dashboard_en/contact/form.html", {"form": form})


def contact_edit1(request, id):
    contact = get_object_or_404(Contact1, id=id)
    form = ContactForm(request.POST or None, instance=contact)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("en-admin:contact_list")
    return render(request, "dashboard_en/contact/form.html", {"form": form, "contact": contact})


def contact_delete1(request, id):
    contact = get_object_or_404(Contact1, id=id)
    contact.delete()
    return redirect("en-admin:contact_list")


# ==============================
# INTERNET VIEWS
# ==============================
def internet_list1(request):
    items = Internet1.objects.all()
    return render(request, "dashboard_en/internet/list.html", {"items": items})


def internet_create1(request):
    form = InternetForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("en-admin:internet_list")
    return render(request, "dashboard_en/internet/form.html", {"form": form})


def internet_edit1(request, id):
    item = get_object_or_404(Internet1, id=id)
    form = InternetForm(request.POST or None, instance=item)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("en-admin:internet_list")
    return render(request, "dashboard_en/internet/form.html", {"form": form, "item": item})


def internet_delete1(request, id):
    item = get_object_or_404(Internet1, id=id)
    item.delete()
    return redirect("en-admin:internet_list")


# ==============================
# MISSION VIEWS
# ==============================
def mission_list1(request):
    missions = Mission1.objects.all()
    return render(request, "dashboard_en/mission/list.html", {"missions": missions})


def mission_create1(request):
    form = MissionForm(request.POST or None, request.FILES or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("en-admin:mission_list")
    return render(request, "dashboard_en/mission/form.html", {"form": form})


def mission_edit1(request, id):
    mission = get_object_or_404(Mission1, id=id)
    form = MissionForm(request.POST or None, request.FILES or None, instance=mission)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("en-admin:mission_list")
    return render(request, "dashboard_en/mission/form.html", {"form": form, "mission": mission})


def mission_delete1(request, id):
    mission = get_object_or_404(Mission1, id=id)
    mission.delete()
    return redirect("en-admin:mission_list")


# ==============================
# MISSION POINT VIEWS
# ==============================
def mission_point_list1(request):
    points = MissionPoint1.objects.all()
    return render(request, "dashboard_en/mission_point/list.html", {"points": points})


def mission_point_create1(request):
    form = MissionPointForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("en-admin:mission_point_list")
    return render(request, "dashboard_en/mission_point/form.html", {"form": form})


def mission_point_edit1(request, id):
    point = get_object_or_404(MissionPoint1, id=id)
    form = MissionPointForm(request.POST or None, instance=point)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("en-admin:mission_point_list")
    return render(request, "dashboard_en/mission_point/form.html", {"form": form, "point": point})


def mission_point_delete1(request, id):
    point = get_object_or_404(MissionPoint1, id=id)
    point.delete()
    return redirect("en-admin:mission_point_list")


# ==============================
# STATISTIC VIEWS
# ==============================
def statistic_list1(request):
    stats = Statistic1.objects.all()
    return render(request, "dashboard_en/statistic/list.html", {"stats": stats})


def statistic_create1(request):
    form = StatisticForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("en-admin:statistic_list")
    return render(request, "dashboard_en/statistic/form.html", {"form": form})


def statistic_edit1(request, id):
    stat = get_object_or_404(Statistic1, id=id)
    form = StatisticForm(request.POST or None, instance=stat)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("en-admin:statistic_list")
    return render(request, "dashboard_en/statistic/form.html", {"form": form, "stat": stat})


def statistic_delete1(request, id):
    stat = get_object_or_404(Statistic1, id=id)
    stat.delete()
    return redirect("en-admin:statistic_list")


# ==============================
# VALUE VIEWS
# ==============================
def value_list1(request):
    values = Value1.objects.all()
    return render(request, "dashboard_en/value/list.html", {"values": values})


def value_create1(request):
    form = ValueForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("en-admin:value_list")
    return render(request, "dashboard_en/value/form.html", {"form": form})


def value_edit1(request, id):
    value = get_object_or_404(Value1, id=id)
    form = ValueForm(request.POST or None, instance=value)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("en-admin:value_list")
    return render(request, "dashboard_en/value/form.html", {"form": form, "value": value})


def value_delete1(request, id):
    value = get_object_or_404(Value1, id=id)
    value.delete()
    return redirect("en-admin:value_list")


# ==============================
# ACHIEVEMENT VIEWS
# ==============================
def achievement_list1(request):
    achievements = Achievement1.objects.all()
    return render(request, "dashboard_en/achievement/list.html", {"achievements": achievements})


def achievement_create1(request):
    form = AchievementForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("en-admin:achievement_list")
    return render(request, "dashboard_en/achievement/form.html", {"form": form})


def achievement_edit1(request, id):
    achievement = get_object_or_404(Achievement1, id=id)
    form = AchievementForm(request.POST or None, instance=achievement)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("en-admin:achievement_list")
    return render(request, "dashboard_en/achievement/form.html", {"form": form, "achievement": achievement})


def achievement_delete1(request, id):
    achievement = get_object_or_404(Achievement1, id=id)
    achievement.delete()
    return redirect("en-admin:achievement_list")


# ==============================
# MEMBER VIEWS
# ==============================
def member_list1(request):
    members = Member1.objects.all()
    return render(request, "dashboard_en/member/list.html", {"members": members})


def member_create1(request):
    form = MemberForm(request.POST or None, request.FILES or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("en-admin:member_list")
    return render(request, "dashboard_en/member/form.html", {"form": form})


def member_edit1(request, id):
    member = get_object_or_404(Member1, id=id)
    form = MemberForm(request.POST or None, request.FILES or None, instance=member)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("en-admin:member_list")
    return render(request, "dashboard_en/member/form.html", {"form": form, "member": member})


def member_delete1(request, id):
    member = get_object_or_404(Member1, id=id)
    member.delete()
    return redirect("en-admin:member_list")


# ==============================
# HISTORY VIEWS
# ==============================
def history_list1(request):
    histories = History1.objects.all()
    return render(request, "dashboard_en/history/list.html", {"histories": histories})


def history_create1(request):
    form = HistoryForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("en-admin:history_list")
    return render(request, "dashboard_en/history/form.html", {"form": form})


def history_edit1(request, id):
    history = get_object_or_404(History1, id=id)
    form = HistoryForm(request.POST or None, instance=history)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("en-admin:history_list")
    return render(request, "dashboard_en/history/form.html", {"form": form, "history": history})


def history_delete1(request, id):
    history = get_object_or_404(History1, id=id)
    history.delete()
    return redirect("en-admin:history_list")


# ---------------- MANUFACTURING OVERVIEW ----------------
def manufacturing_overview_list1(request):
    items = ManufacturingOverview1.objects.all()
    return render(request, 'dashboard_en/overview/list.html', {'items': items})


def manufacturing_overview_create1(request):
    form = ManufacturingOverviewForm(request.POST or None, request.FILES or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect('en-admin:overview_list')
    return render(request, 'dashboard_en/overview/form.html', {'form': form})


def manufacturing_overview_edit1(request, id):
    obj = get_object_or_404(ManufacturingOverview1, id=id)
    form = ManufacturingOverviewForm(request.POST or None, request.FILES or None, instance=obj)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect('en-admin:overview_list')
    return render(request, 'dashboard_en/overview/form.html', {'form': form, 'object': obj})


def manufacturing_overview_delete1(request, id):
    obj = get_object_or_404(ManufacturingOverview1, id=id)
    obj.delete()
    return redirect('en-admin:overview_list')


# ---------------- MANUFACTURING STAT ----------------
def manufacturing_stat_list1(request):
    items = ManufacturingStat1.objects.all()
    return render(request, 'dashboard_en/stat/list.html', {'items': items})


def manufacturing_stat_create1(request):
    form = ManufacturingStatForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect('en-admin:stat_list')
    return render(request, 'dashboard_en/stat/form.html', {'form': form})


def manufacturing_stat_edit1(request, id):
    obj = get_object_or_404(ManufacturingStat1, id=id)
    form = ManufacturingStatForm(request.POST or None, instance=obj)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect('en-admin:stat_list')
    return render(request, 'dashboard_en/stat/form.html', {'form': form, 'object': obj})


def manufacturing_stat_delete1(request, id):
    obj = get_object_or_404(ManufacturingStat1, id=id)
    obj.delete()
    return redirect('en-admin:stat_list')


# ---------------- PRODUCTION LINE ----------------
def production_line_list1(request):
    items = ProductionLine1.objects.all()
    return render(request, 'dashboard_en/line/list.html', {'items': items})


def production_line_create1(request):
    form = ProductionLineForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect('en-admin:line_list')
    return render(request, 'dashboard_en/line/form.html', {'form': form})


def production_line_edit1(request, id):
    obj = get_object_or_404(ProductionLine1, id=id)
    form = ProductionLineForm(request.POST or None, instance=obj)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect('en-admin:line_list')
    return render(request, 'dashboard_en/line/form.html', {'form': form, 'object': obj})


def production_line_delete1(request, id):
    obj = get_object_or_404(ProductionLine1, id=id)
    obj.delete()
    return redirect('en-admin:line_list')


# ---------------- PARTNER ----------------
def partner_list1(request):
    items = Partner1.objects.all()
    return render(request, 'dashboard_en/partner/list.html', {'items': items})


def partner_create1(request):
    form = PartnerForm(request.POST or None, request.FILES or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect('en-admin:partner_list')
    return render(request, 'dashboard_en/partner/form.html', {'form': form})


def partner_edit1(request, id):
    obj = get_object_or_404(Partner1, id=id)
    form = PartnerForm(request.POST or None, request.FILES or None, instance=obj)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect('en-admin:partner_list')
    return render(request, 'dashboard_en/partner/form.html', {'form': form, 'object': obj})


def partner_delete1(request, id):
    obj = get_object_or_404(Partner1, id=id)
    obj.delete()
    return redirect('en-admin:partner_list')


# ---------------- PARTNERSHIP BENEFIT ----------------
def partnership_benefit_list1(request):
    items = PartnershipBenefit1.objects.all()
    return render(request, 'dashboard_en/benefit/list.html', {'items': items})


def partnership_benefit_create1(request):
    form = PartnershipBenefitForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect('en-admin:benefit_list')
    return render(request, 'dashboard_en/benefit/form.html', {'form': form})


def partnership_benefit_edit1(request, id):
    obj = get_object_or_404(PartnershipBenefit1, id=id)
    form = PartnershipBenefitForm(request.POST or None, instance=obj)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect('en-admin:benefit_list')
    return render(request, 'dashboard_en/benefit/form.html', {'form': form, 'object': obj})


def partnership_benefit_delete1(request, id):
    obj = get_object_or_404(PartnershipBenefit1, id=id)
    obj.delete()
    return redirect('en-admin:benefit_list')


# ---------------- GALLERY CATEGORY ----------------
def gallery_category_list1(request):
    items = GalleryCategory1.objects.all()
    return render(request, 'dashboard_en/gallery_category/list.html', {'items': items})


def gallery_category_create1(request):
    form = GalleryCategoryForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect('en-admin:gallery_category_list')
    return render(request, 'dashboard_en/gallery_category/form.html', {'form': form})


def gallery_category_edit1(request, id):
    obj = get_object_or_404(GalleryCategory1, id=id)
    form = GalleryCategoryForm(request.POST or None, instance=obj)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect('en-admin:gallery_category_list')
    return render(request, 'dashboard_en/gallery_category/form.html', {'form': form, 'object': obj})


def gallery_category_delete1(request, id):
    obj = get_object_or_404(GalleryCategory1, id=id)
    obj.delete()
    return redirect('en-admin:gallery_category_list')


# ---------------- GALLERY ----------------
def gallery_list1(request):
    items = Gallery1.objects.all()
    return render(request, 'dashboard_en/gallery/list.html', {'items': items})


def gallery_create1(request):
    form = GalleryForm(request.POST or None, request.FILES or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect('en-admin:gallery_list')
    return render(request, 'dashboard_en/gallery/form.html', {'form': form})


def gallery_edit1(request, id):
    obj = get_object_or_404(Gallery1, id=id)
    form = GalleryForm(request.POST or None, request.FILES or None, instance=obj)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect('en-admin:gallery_list')
    return render(request, 'dashboard_en/gallery/form.html', {'form': form, 'object': obj})


def gallery_delete1(request, id):
    obj = get_object_or_404(Gallery1, id=id)
    obj.delete()
    return redirect('en-admin:gallery_list')


# ---------------- CATEGORY ----------------
def category_list1(request):
    items = Category1.objects.all()
    return render(request, 'dashboard_en/category/list.html', {'items': items})


def category_create1(request):
    form = CategoryForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect('en-admin:category_list')
    return render(request, 'dashboard_en/category/form.html', {'form': form})


def category_edit1(request, id):
    obj = get_object_or_404(Category1, id=id)
    form = CategoryForm(request.POST or None, instance=obj)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect('en-admin:category_list')
    return render(request, 'dashboard_en/category/form.html', {'form': form, 'object': obj})


def category_delete1(request, id):
    obj = get_object_or_404(Category1, id=id)
    obj.delete()
    return redirect('en-admin:category_list')


# ---------------- NEWS ----------------
def news_list1(request):
    items = News1.objects.all()
    return render(request, 'dashboard_en/news/list.html', {'items': items})


def news_create1(request):
    form = NewsForm(request.POST or None, request.FILES or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect('en-admin:news_list')
    return render(request, 'dashboard_en/news/form.html', {'form': form})


def news_edit1(request, id):
    obj = get_object_or_404(News1, id=id)
    form = NewsForm(request.POST or None, request.FILES or None, instance=obj)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect('en-admin:news_list')
    return render(request, 'dashboard_en/news/form.html', {'form': form, 'object': obj})


def news_delete1(request, id):
    obj = get_object_or_404(News1, id=id)
    obj.delete()
    return redirect('en-admin:news_list')


def product_category_list1(request):
    categories = ProductCategory1.objects.all()
    return render(request, "dashboard_en/product_category/list.html", {"categories": categories})


def product_category_create1(request):
    form = ProductCategoryForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("en-admin:product_category_list")
    return render(request, "dashboard_en/category/form.html", {"form": form})


def product_category_edit1(request, id):
    category = get_object_or_404(ProductCategory1, id=id)
    form = ProductCategoryForm(request.POST or None, instance=category)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("en-admin:product_category_list")
    return render(request, "dashboard_en/category/form.html", {"form": form, "category": category})


def product_category_delete1(request, id):
    category = get_object_or_404(ProductCategory1, id=id)
    category.delete()
    return redirect("en-admin:product_category_list")


# ==============================
# PRODUCT CRUD
# ==============================
def product_list1(request):
    products = Product1.objects.all()
    return render(request, "dashboard_en/product/list.html", {"products": products})


def product_create1(request):
    form = ProductForm(request.POST or None, request.FILES or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("en-admin:product_list")
    return render(request, "dashboard_en/product/form.html", {"form": form})


def product_edit1(request, id):
    product = get_object_or_404(Product1, id=id)
    form = ProductForm(request.POST or None, request.FILES or None, instance=product)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("en-admin:product_list")
    return render(request, "dashboard_en/product/form.html", {"form": form, "product": product})


def product_delete1(request, id):
    product = get_object_or_404(Product1, id=id)
    product.delete()
    return redirect("en-admin:product_list")


# ==============================
# PRODUCT FEATURE CRUD
# ==============================
def product_feature_list1(request):
    features = ProductFeature1.objects.all()
    return render(request, "dashboard_en/product_feature/list.html", {"features": features})


def product_feature_create1(request):
    form = ProductFeatureForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("en-admin:product_feature_list")
    return render(request, "dashboard_en/product_feature/form.html", {"form": form})


def product_feature_edit1(request, id):
    feature = get_object_or_404(ProductFeature1, id=id)
    form = ProductFeatureForm(request.POST or None, instance=feature)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("en-admin:product_feature_list")
    return render(request, "dashboard_en/product_feature/form.html", {"form": form, "feature": feature})


def product_feature_delete1(request, id):
    feature = get_object_or_404(ProductFeature1, id=id)
    feature.delete()
    return redirect("en-admin:product_feature_list")


# ==============================
# PRODUCT IMAGE CRUD
# ==============================
def image_list1(request):
    images = ProductImage1.objects.all()
    return render(request, "dashboard_en/image/list.html", {"images": images})


def image_create1(request):
    form = ProductImageForm(request.POST or None, request.FILES or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("en-admin:image_list")
    return render(request, "dashboard_en/image/form.html", {"form": form})


def image_edit1(request, id):
    image = get_object_or_404(ProductImage1, id=id)
    form = ProductImageForm(request.POST or None, request.FILES or None, instance=image)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("en-admin:image_list")
    return render(request, "dashboard_en/image/form.html", {"form": form, "image": image})


def image_delete1(request, id):
    image = get_object_or_404(ProductImage1, id=id)
    image.delete()
    return redirect("en-admin:image_list")
