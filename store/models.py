from django.db import models
from django.utils.safestring import mark_safe
from django.utils.html import format_html


# Stores model
class Store(models.Model):
    image = models.ImageField(verbose_name="Логотип", upload_to='logo', null=True, blank=True)
    name = models.CharField(max_length=255, verbose_name="Название магазина")
    shortInfo = models.CharField(max_length=455, verbose_name="Краткое описание")
    owner = models.CharField(max_length=255, verbose_name="ФИО владельца")
    phone = models.CharField(max_length=255, verbose_name="Телефон номер")
    location = models.CharField(max_length=255, verbose_name="Адресс магазина")
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Магазин"
        verbose_name_plural = "Магазины"

    def __str__(self):
        return self.name

    def image_tag(self):
        return format_html('<img src="{}" style="width:70px; height:70px"/>'.format(self.image.url))
