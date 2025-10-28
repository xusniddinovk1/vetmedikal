from django.db import models


class ProductCategory2(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Product2(models.Model):
    category = models.ForeignKey(ProductCategory2, on_delete=models.CASCADE, related_name="products")
    title = models.CharField(max_length=200)
    subtitle = models.TextField()
    description = models.TextField()
    usage = models.TextField()  # Qo'llash yo'riqnomasi
    composition = models.TextField()  # Tarkib
    image = models.ImageField(upload_to="products/")  # asosiy rasm
    badge = models.CharField(max_length=50, blank=True, null=True)  # "Yangi", "Mashhur"
    specs = models.JSONField(default=dict, blank=True)  # {"hajm": "1ml", "harorat": "2-8°C"}
    price = models.PositiveIntegerField(null=True, blank=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    certificates = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.title


class ProductFeature2(models.Model):
    icon = models.CharField(max_length=50, default="fas fa-check-circle")
    title = models.CharField(max_length=200)
    description = models.TextField()

    class Meta:
        verbose_name = "Mahsulot afzalligi"
        verbose_name_plural = "Mahsulot afzalliklari"

    def __str__(self):
        return self.title


class ProductImage2(models.Model):
    product = models.ForeignKey(Product2, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="products/gallery/")

    def __str__(self):
        return f"{self.product.title} rasmi"
