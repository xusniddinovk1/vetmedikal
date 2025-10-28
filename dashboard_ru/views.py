from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from medical_ru.models import *
from .forms import *


def login_required_decorator(func):
    return login_required(func, login_url='ru-admin:vhod_stranitsa')


def login_page(request):
    if request.method == "POST":
        phone = request.POST.get("phone_number")
        password = request.POST.get("password")

        user = authenticate(request, phone_number=phone, password=password)
        if user:
            login(request, user)
            return redirect('ru-admin:vhod_stranitsa')
        else:
            return render(request, "dashboard_ru/login.html", {"error": "Incorrect credentials"})

    return render(request, "dashboard_ru/login.html")


@login_required_decorator
def logout_page(request):
    logout(request)
    return redirect('ru-admin:vhod_stranitsa')


@login_required_decorator
def my_profile(request):
    ctx = {
        'user': request.user,
    }
    return render(request, 'dashboard_ru/profile/profile.html', ctx)


@login_required_decorator
def profile_edit(request):
    user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('ru-admin:moy_profil')
    else:
        form = ProfileForm(instance=user)

    ctx = {
        'form': form
    }

    return render(request, 'dashboard_ru/profile/profile_edit.html', ctx)


@method_decorator(login_required, name='dispatch')
class CustomPasswordChangeView(PasswordChangeView):
    template_name = 'dashboard_ru/profile/password_change.html'
    success_url = reverse_lazy('password_change_done')


@login_required_decorator
def home_page(request):
    products = Product2.objects.all()
    news = News2.objects.all()
    partners = Partner2.objects.all()
    members = Member2.objects.all()
    galleries = Gallery2.objects.all()
    product_categories = ProductCategory2.objects.all()
    statistics = Statistic2.objects.all()
    achievements = Achievement2.objects.all()

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
    return render(request, 'dashboard_ru/index.html', {'items': items})


def service_list(request):
    services = Service2.objects.all()
    return render(request, "dashboard_ru/service/list.html", {"services": services})


def service_create(request):
    form = ServiceForm(request.POST or None, request.FILES or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("ru-admin:uslugi_spisok")
    return render(request, "dashboard_ru/service/form.html", {"form": form})


def service_edit(request, id):
    service = get_object_or_404(Service2, id=id)
    form = ServiceForm(request.POST or None, request.FILES or None, instance=service)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("ru-admin:uslugi_spisok")
    return render(request, "dashboard_ru/service/form.html", {"form": form, "service": service})


def service_delete(request, id):
    service = get_object_or_404(Service2, id=id)
    service.delete()
    return redirect("ru-admin:uslugi_spisok")


# ==============================
# FEATURE VIEWS
# ==============================
def feature_list(request):
    features = Feature2.objects.all()
    return render(request, "dashboard_ru/feature/list.html", {"features": features})


def feature_create(request):
    form = FeatureForm(request.POST or None, request.FILES or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("ru-admin:osobennosti_spisok")
    return render(request, "dashboard_ru/feature/form.html", {"form": form})


def feature_edit(request, id):
    feature = get_object_or_404(Feature2, id=id)
    form = FeatureForm(request.POST or None, request.FILES or None, instance=feature)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("ru-admin:osobennosti_spisok")
    return render(request, "dashboard_ru/feature/form.html", {"form": form, "feature": feature})


def feature_delete(request, id):
    feature = get_object_or_404(Feature2, id=id)
    feature.delete()
    return redirect("ru-admin:osobennosti_spisok")


# ==============================
# CONTACT VIEWS
# ==============================
def contact_list(request):
    contacts = Contact2.objects.all()
    return render(request, "dashboard_ru/contact/list.html", {"contacts": contacts})


def contact_create(request):
    form = ContactForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("ru-admin:kontakty_spisok")
    return render(request, "dashboard_ru/contact/form.html", {"form": form})


def contact_edit(request, id):
    contact = get_object_or_404(Contact2, id=id)
    form = ContactForm(request.POST or None, instance=contact)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("ru-admin:kontakty_spisok")
    return render(request, "dashboard_ru/contact/form.html", {"form": form, "contact": contact})


def contact_delete(request, id):
    contact = get_object_or_404(Contact2, id=id)
    contact.delete()
    return redirect("ru-admin:kontakty_spisok")


# ==============================
# INTERNET VIEWS
# ==============================
def internet_list(request):
    items = Internet2.objects.all()
    return render(request, "dashboard_ru/internet/list.html", {"items": items})


def internet_create(request):
    form = InternetForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("ru-admin:internet_spisok")
    return render(request, "dashboard_ru/internet/form.html", {"form": form})


def internet_edit(request, id):
    item = get_object_or_404(Internet2, id=id)
    form = InternetForm(request.POST or None, instance=item)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("ru-admin:internet_spisok")
    return render(request, "dashboard_ru/internet/form.html", {"form": form, "item": item})


def internet_delete(request, id):
    item = get_object_or_404(Internet2, id=id)
    item.delete()
    return redirect("ru-admin:internet_spisok")


# ==============================
# MISSION VIEWS
# ==============================
def mission_list(request):
    missions = Mission2.objects.all()
    return render(request, "dashboard_ru/mission/list.html", {"missions": missions})


def mission_create(request):
    form = MissionForm(request.POST or None, request.FILES or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("ru-admin:missiya_spisok")
    return render(request, "dashboard_ru/mission/form.html", {"form": form})


def mission_edit(request, id):
    mission = get_object_or_404(Mission2, id=id)
    form = MissionForm(request.POST or None, request.FILES or None, instance=mission)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("ru-admin:missiya_spisok")
    return render(request, "dashboard_ru/mission/form.html", {"form": form, "mission": mission})


def mission_delete(request, id):
    mission = get_object_or_404(Mission2, id=id)
    mission.delete()
    return redirect("ru-admin:missiya_spisok")


# ==============================
# MISSION POINT VIEWS
# ==============================
def mission_point_list(request):
    points = MissionPoint2.objects.all()
    return render(request, "dashboard_ru/mission_point/list.html", {"points": points})


def mission_point_create(request):
    form = MissionPointForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("ru-admin:punkty_missii_spisok")
    return render(request, "dashboard_ru/mission_point/form.html", {"form": form})


def mission_point_edit(request, id):
    point = get_object_or_404(MissionPoint2, id=id)
    form = MissionPointForm(request.POST or None, instance=point)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("ru-admin:punkty_missii_spisok")
    return render(request, "dashboard_ru/mission_point/form.html", {"form": form, "point": point})


def mission_point_delete(request, id):
    point = get_object_or_404(MissionPoint2, id=id)
    point.delete()
    return redirect("ru-admin:punkty_missii_spisok")


# ==============================
# STATISTIC VIEWS
# ==============================
def statistic_list(request):
    stats = Statistic2.objects.all()
    return render(request, "dashboard_ru/statistic/list.html", {"stats": stats})


def statistic_create(request):
    form = StatisticForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("ru-admin:statistika_spisok")
    return render(request, "dashboard_ru/statistic/form.html", {"form": form})


def statistic_edit(request, id):
    stat = get_object_or_404(Statistic2, id=id)
    form = StatisticForm(request.POST or None, instance=stat)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("ru-admin:statistika_spisok")
    return render(request, "dashboard_ru/statistic/form.html", {"form": form, "stat": stat})


def statistic_delete(request, id):
    stat = get_object_or_404(Statistic2, id=id)
    stat.delete()
    return redirect("ru-admin:statistika_spisok")


# ==============================
# VALUE VIEWS
# ==============================
def value_list(request):
    values = Value2.objects.all()
    return render(request, "dashboard_ru/value/list.html", {"values": values})


def value_create(request):
    form = ValueForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("ru-admin:tsennosti_spisok")
    return render(request, "dashboard_ru/value/form.html", {"form": form})


def value_edit(request, id):
    value = get_object_or_404(Value2, id=id)
    form = ValueForm(request.POST or None, instance=value)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("ru-admin:tsennosti_spisok")
    return render(request, "dashboard_ru/value/form.html", {"form": form, "value": value})


def value_delete(request, id):
    value = get_object_or_404(Value2, id=id)
    value.delete()
    return redirect("ru-admin:tsennosti_spisok")


# ==============================
# ACHIEVEMENT VIEWS
# ==============================
def achievement_list(request):
    achievements = Achievement2.objects.all()
    return render(request, "dashboard_ru/achievement/list.html", {"achievements": achievements})


def achievement_create(request):
    form = AchievementForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("ru-admin:dostizheniya_spisok")
    return render(request, "dashboard_ru/achievement/form.html", {"form": form})


def achievement_edit(request, id):
    achievement = get_object_or_404(Achievement2, id=id)
    form = AchievementForm(request.POST or None, instance=achievement)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("ru-admin:dostizheniya_spisok")
    return render(request, "dashboard_ru/achievement/form.html", {"form": form, "achievement": achievement})


def achievement_delete(request, id):
    achievement = get_object_or_404(Achievement2, id=id)
    achievement.delete()
    return redirect("ru-admin:dostizheniya_spisok")


# ==============================
# MEMBER VIEWS
# ==============================
def member_list(request):
    members = Member2.objects.all()
    return render(request, "dashboard_ru/member/list.html", {"members": members})


def member_create(request):
    form = MemberForm(request.POST or None, request.FILES or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("ru-admin:chleny_komandy_spisok")
    return render(request, "dashboard_ru/member/form.html", {"form": form})


def member_edit(request, id):
    member = get_object_or_404(Member2, id=id)
    form = MemberForm(request.POST or None, request.FILES or None, instance=member)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("ru-admin:chleny_komandy_spisok")
    return render(request, "dashboard_ru/member/form.html", {"form": form, "member": member})


def member_delete(request, id):
    member = get_object_or_404(Member2, id=id)
    member.delete()
    return redirect("ru-admin:chleny_komandy_spisok")


# ==============================
# HISTORY VIEWS
# ==============================
def history_list(request):
    histories = History2.objects.all()
    return render(request, "dashboard_ru/history/list.html", {"histories": histories})


def history_create(request):
    form = HistoryForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("ru-admin:istoriya_spisok")
    return render(request, "dashboard_ru/history/form.html", {"form": form})


def history_edit(request, id):
    history = get_object_or_404(History2, id=id)
    form = HistoryForm(request.POST or None, instance=history)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("ru-admin:istoriya_spisok")
    return render(request, "dashboard_ru/history/form.html", {"form": form, "history": history})


def history_delete(request, id):
    history = get_object_or_404(History2, id=id)
    history.delete()
    return redirect("ru-admin:istoriya_spisok")


# ---------------- MANUFACTURING OVERVIEW ----------------
def manufacturing_overview_list(request):
    items = ManufacturingOverview2.objects.all()
    return render(request, 'dashboard_ru/overview/list.html', {'items': items})


def manufacturing_overview_create(request):
    form = ManufacturingOverviewForm(request.POST or None, request.FILES or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect('ru-admin:obzor_spisok')
    return render(request, 'dashboard_ru/overview/form.html', {'form': form})


def manufacturing_overview_edit(request, id):
    obj = get_object_or_404(ManufacturingOverview2, id=id)
    form = ManufacturingOverviewForm(request.POST or None, request.FILES or None, instance=obj)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect('ru-admin:obzor_spisok')
    return render(request, 'dashboard_ru/overview/form.html', {'form': form, 'object': obj})


def manufacturing_overview_delete(request, id):
    obj = get_object_or_404(ManufacturingOverview2, id=id)
    obj.delete()
    return redirect('ru-admin:obzor_spisok')


# ---------------- MANUFACTURING STAT ----------------
def manufacturing_stat_list(request):
    items = ManufacturingStat2.objects.all()
    return render(request, 'dashboard_ru/stat/list.html', {'items': items})


def manufacturing_stat_create(request):
    form = ManufacturingStatForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect('ru-admin:statistika_proizvodstva_spisok')
    return render(request, 'dashboard_ru/stat/form.html', {'form': form})


def manufacturing_stat_edit(request, id):
    obj = get_object_or_404(ManufacturingStat2, id=id)
    form = ManufacturingStatForm(request.POST or None, instance=obj)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect('ru-admin:statistika_proizvodstva_spisok')
    return render(request, 'dashboard_ru/stat/form.html', {'form': form, 'object': obj})


def manufacturing_stat_delete(request, id):
    obj = get_object_or_404(ManufacturingStat2, id=id)
    obj.delete()
    return redirect('ru-admin:statistika_proizvodstva_spisok')


# ---------------- PRODUCTION LINE ----------------
def production_line_list(request):
    items = ProductionLine2.objects.all()
    return render(request, 'dashboard_ru/line/list.html', {'items': items})


def production_line_create(request):
    form = ProductionLineForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect('ru-admin:proizvodstvennaya_liniya_spisok')
    return render(request, 'dashboard_ru/line/form.html', {'form': form})


def production_line_edit(request, id):
    obj = get_object_or_404(ProductionLine2, id=id)
    form = ProductionLineForm(request.POST or None, instance=obj)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect('ru-admin:proizvodstvennaya_liniya_spisok')
    return render(request, 'dashboard_ru/line/form.html', {'form': form, 'object': obj})


def production_line_delete(request, id):
    obj = get_object_or_404(ProductionLine2, id=id)
    obj.delete()
    return redirect('ru-admin:proizvodstvennaya_liniya_spisok')


# ---------------- PARTNER ----------------
def partner_list(request):
    items = Partner2.objects.all()
    return render(request, 'dashboard_ru/partner/list.html', {'items': items})


def partner_create(request):
    form = PartnerForm(request.POST or None, request.FILES or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect('ru-admin:partnery_spisok')
    return render(request, 'dashboard_ru/partner/form.html', {'form': form})


def partner_edit(request, id):
    obj = get_object_or_404(Partner2, id=id)
    form = PartnerForm(request.POST or None, request.FILES or None, instance=obj)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect('ru-admin:partnery_spisok')
    return render(request, 'dashboard_ru/partner/form.html', {'form': form, 'object': obj})


def partner_delete(request, id):
    obj = get_object_or_404(Partner2, id=id)
    obj.delete()
    return redirect('ru-admin:partnery_spisok')


# ---------------- PARTNERSHIP BENEFIT ----------------
def partnership_benefit_list(request):
    items = PartnershipBenefit2.objects.all()
    return render(request, 'dashboard_ru/benefit/list.html', {'items': items})


def partnership_benefit_create(request):
    form = PartnershipBenefitForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect('ru-admin:preimushchestva_partnyorstva_spisok')
    return render(request, 'dashboard_ru/benefit/form.html', {'form': form})


def partnership_benefit_edit(request, id):
    obj = get_object_or_404(PartnershipBenefit2, id=id)
    form = PartnershipBenefitForm(request.POST or None, instance=obj)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect('ru-admin:preimushchestva_partnyorstva_spisok')
    return render(request, 'dashboard_ru/benefit/form.html', {'form': form, 'object': obj})


def partnership_benefit_delete(request, id):
    obj = get_object_or_404(PartnershipBenefit2, id=id)
    obj.delete()
    return redirect('ru-admin:preimushchestva_partnyorstva_spisok')


# ---------------- GALLERY CATEGORY ----------------
def gallery_category_list(request):
    items = GalleryCategory2.objects.all()
    return render(request, 'dashboard_ru/gallery_category/list.html', {'items': items})


def gallery_category_create(request):
    form = GalleryCategoryForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect('ru-admin:kategoriya_galerei_spisok')
    return render(request, 'dashboard_ru/gallery_category/form.html', {'form': form})


def gallery_category_edit(request, id):
    obj = get_object_or_404(GalleryCategory2, id=id)
    form = GalleryCategoryForm(request.POST or None, instance=obj)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect('ru-admin:kategoriya_galerei_spisok')
    return render(request, 'dashboard_ru/gallery_category/form.html', {'form': form, 'object': obj})


def gallery_category_delete(request, id):
    obj = get_object_or_404(GalleryCategory2, id=id)
    obj.delete()
    return redirect('ru-admin:kategoriya_galerei_spisok')


# ---------------- GALLERY ----------------
def gallery_list(request):
    items = Gallery2.objects.all()
    return render(request, 'dashboard_ru/gallery/list.html', {'items': items})


def gallery_create(request):
    form = GalleryForm(request.POST or None, request.FILES or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect('ru-admin:galereya_spisok')
    return render(request, 'dashboard_ru/gallery/form.html', {'form': form})


def gallery_edit(request, id):
    obj = get_object_or_404(Gallery2, id=id)
    form = GalleryForm(request.POST or None, request.FILES or None, instance=obj)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect('ru-admin:galereya_spisok')
    return render(request, 'dashboard_ru/gallery/form.html', {'form': form, 'object': obj})


def gallery_delete(request, id):
    obj = get_object_or_404(Gallery2, id=id)
    obj.delete()
    return redirect('ru-admin:galereya_spisok')


# ---------------- CATEGORY ----------------
def category_list(request):
    items = Category2.objects.all()
    return render(request, 'dashboard_ru/category/list.html', {'items': items})


def category_create(request):
    form = CategoryForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect('ru-admin:kategoriya_spisok')
    return render(request, 'dashboard_ru/category/form.html', {'form': form})


def category_edit(request, id):
    obj = get_object_or_404(Category2, id=id)
    form = CategoryForm(request.POST or None, instance=obj)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect('ru-admin:kategoriya_spisok')
    return render(request, 'dashboard_ru/category/form.html', {'form': form, 'object': obj})


def category_delete(request, id):
    obj = get_object_or_404(Category2, id=id)
    obj.delete()
    return redirect('ru-admin:kategoriya_spisok')


# ---------------- NEWS ----------------
def news_list(request):
    items = News2.objects.all()
    return render(request, 'dashboard_ru/news/list.html', {'items': items})


def news_create(request):
    form = NewsForm(request.POST or None, request.FILES or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect('ru-admin:novosti_spisok')
    return render(request, 'dashboard_ru/news/form.html', {'form': form})


def news_edit(request, id):
    obj = get_object_or_404(News2, id=id)
    form = NewsForm(request.POST or None, request.FILES or None, instance=obj)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect('ru-admin:novosti_spisok')
    return render(request, 'dashboard_ru/news/form.html', {'form': form, 'object': obj})


def news_delete(request, id):
    obj = get_object_or_404(News2, id=id)
    obj.delete()
    return redirect('ru-admin:novosti_spisok')


def product_category_list(request):
    categories = ProductCategory2.objects.all()
    return render(request, "dashboard_ru/product_category/list.html", {"categories": categories})


def product_category_create(request):
    form = ProductCategoryForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("ru-admin:kategoriya_produktov_spisok")
    return render(request, "dashboard_ru/category/form.html", {"form": form})


def product_category_edit(request, id):
    category = get_object_or_404(ProductCategory2, id=id)
    form = ProductCategoryForm(request.POST or None, instance=category)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("ru-admin:kategoriya_produktov_spisok")
    return render(request, "dashboard_ru/category/form.html", {"form": form, "category": category})


def product_category_delete(request, id):
    category = get_object_or_404(ProductCategory2, id=id)
    category.delete()
    return redirect("ru-admin:kategoriya_produktov_spisok")


# ==============================
# PRODUCT CRUD
# ==============================
def product_list(request):
    products = Product2.objects.all()
    return render(request, "dashboard_ru/product/list.html", {"products": products})


def product_create(request):
    form = ProductForm(request.POST or None, request.FILES or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("ru-admin:produkty_spisok")
    return render(request, "dashboard_ru/product/form.html", {"form": form})


def product_edit(request, id):
    product = get_object_or_404(Product2, id=id)
    form = ProductForm(request.POST or None, request.FILES or None, instance=product)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("ru-admin:produkty_spisok")
    return render(request, "dashboard_ru/product/form.html", {"form": form, "product": product})


def product_delete(request, id):
    product = get_object_or_404(Product2, id=id)
    product.delete()
    return redirect("ru-admin:produkty_spisok")


# ==============================
# PRODUCT FEATURE CRUD
# ==============================
def product_feature_list(request):
    features = ProductFeature2.objects.all()
    return render(request, "dashboard_ru/product_feature/list.html", {"features": features})


def product_feature_create(request):
    form = ProductFeatureForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("ru-admin:harakteristiki_produktov_spisok")
    return render(request, "dashboard_ru/product_feature/form.html", {"form": form})


def product_feature_edit(request, id):
    feature = get_object_or_404(ProductFeature2, id=id)
    form = ProductFeatureForm(request.POST or None, instance=feature)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("ru-admin:harakteristiki_produktov_spisok")
    return render(request, "dashboard_ru/product_feature/form.html", {"form": form, "feature": feature})


def product_feature_delete(request, id):
    feature = get_object_or_404(ProductFeature2, id=id)
    feature.delete()
    return redirect("ru-admin:harakteristiki_produktov_spisok")


# ==============================
# PRODUCT IMAGE CRUD
# ==============================
def image_list(request):
    images = ProductImage2.objects.all()
    return render(request, "dashboard_ru/image/list.html", {"images": images})


def image_create(request):
    form = ProductImageForm(request.POST or None, request.FILES or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("ru-admin:izobrazheniya_spisok")
    return render(request, "dashboard_ru/image/form.html", {"form": form})


def image_edit(request, id):
    image = get_object_or_404(ProductImage2, id=id)
    form = ProductImageForm(request.POST or None, request.FILES or None, instance=image)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("ru-admin:izobrazheniya_spisok")
    return render(request, "dashboard_ru/image/form.html", {"form": form, "image": image})


def image_delete(request, id):
    image = get_object_or_404(ProductImage2, id=id)
    image.delete()
    return redirect("ru-admin:izobrazheniya_spisok")
