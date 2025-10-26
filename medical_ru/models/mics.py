from django.db import models


class ManufacturingOverview2(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to="manufacturing/")

    def __str__(self):
        return self.title


class ManufacturingStat2(models.Model):
    number = models.CharField(max_length=50)
    label = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.number} {self.label}"


class ProductionLine2(models.Model):
    icon = models.CharField(max_length=50, default="fas fa-industry")  # FontAwesome icon
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title


# Hamkorlar modeli
class Partner2(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    logo = models.ImageField(upload_to="partners/")
    website = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name


# Hamkorlik afzalliklari modeli
class PartnershipBenefit2(models.Model):
    icon = models.CharField(max_length=50, default="fas fa-check-circle")
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title


class GalleryCategory2(models.Model):
    name = models.CharField(max_length=100, unique=True)  # Masalan: "Binolar", "Mahsulotlar"

    class Meta:
        verbose_name = "Galereya Kategoriya"
        verbose_name_plural = "Galereya Kategoriyalar"

    def __str__(self):
        return self.name


class Gallery2(models.Model):
    category = models.ForeignKey(GalleryCategory2, on_delete=models.CASCADE, related_name="images")
    title = models.CharField(max_length=200)  # Masalan: "Asosiy bino"
    description = models.TextField(blank=True, null=True)  # Qo‘shimcha izoh
    image = models.ImageField(upload_to="gallery/")  # Rasm joylash
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Galereya"
        verbose_name_plural = "Galereyalar"

    def __str__(self):
        return self.title


class Category2(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class News2(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to="news/")
    date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category2, on_delete=models.CASCADE, related_name="news")

    def __str__(self):
        return self.title
