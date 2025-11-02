from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(max_length=100, unique=True, blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, related_name="products")
    title = models.CharField(max_length=200, blank=True)
    subtitle = models.TextField(blank=True)
    description = models.TextField(blank=True)
    usage = models.TextField(blank=True)  # Qo'llash yo'riqnomasi
    composition = models.TextField(blank=True)  # Tarkib
    image = models.ImageField(upload_to="products/")  # asosiy rasm
    badge = models.CharField(max_length=50, blank=True, null=True)  # "Yangi", "Mashhur"
    specs = models.JSONField(default=dict, blank=True)  # {"hajm": "1ml", "harorat": "2-8°C"}
    price = models.PositiveIntegerField(null=True, blank=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    certificates = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.title


class ProductFeature(models.Model):
    icon = models.CharField(max_length=50, default="fas fa-check-circle")
    title = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name = "Mahsulot afzalligi"
        verbose_name_plural = "Mahsulot afzalliklari"

    def __str__(self):
        return self.title


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="products/gallery/")

    def __str__(self):
        return f"{self.product.title} rasmi"
