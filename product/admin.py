from django.contrib import admin
import admin_thumbnails
from mptt.admin import DraggableMPTTAdmin
from .models import *


# Color Admin Fields
class ColorAdmin(admin.ModelAdmin):
    list_display = ['name', 'code', 'color_tag']


# Category Admin Fields
@admin_thumbnails.thumbnail('image')
class CategoryAdmin(DraggableMPTTAdmin):
    mptt_indent_field = "name"
    list_display = ('tree_actions', 'indented_title', 'color', 'image_tag')
    list_display_links = ('indented_title',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)

        # Add cumulative product count
        qs = Category.objects.add_related_count(
            qs,
            Product,
            'category',
            'products_cumulative_count',
            cumulative=True)

        # Add non cumulative product count
        qs = Category.objects.add_related_count(
            qs,
            Product,
            'category',
            'products_count',
            cumulative=False)
        return qs

    def related_products_count(self, instance):
        return instance.products_count

    related_products_count.short_description = 'Related products (for this specific category)'

    def related_products_cumulative_count(self, instance):
        return instance.products_cumulative_count

    related_products_cumulative_count.short_description = 'Related products (in tree)'


# Brand Admin Fields
class BrandAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


class ProductImages(admin.ModelAdmin):
    list_display = ['product', 'id', 'image_tag']
    readonly_fields = ('id',)


# ProductImage Admin Field
class ProductsImageAdmin(admin.TabularInline):
    model = ProductsImage
    readonly_fields = ('id', 'image_tag')
    list_display = ('id', 'image_tag')
    extra = 1

    def image_tag(self, instance):
        return format_html('<img src="{}" width="90" height="90" />'.format(instance.image.url))
    image_tag.short_description = 'Image'
    image_tag.allow_tags = True


# class ProductVariants(admin.TabularInline):
#     model = ProductVariant
#     readonly_fields = ('image_tag',)
#     extra = 1
#     show_change_link = True
#
#     def image_tag(self, instance):
#         return format_html('<img src="{}" width="90" height="90" />'.format(instance.image.url))
#     image_tag.short_description = 'Image'
#     image_tag.allow_tags = True


# class ProductVariantAdmin(admin.ModelAdmin):
#     list_display = ['product', 'color', 'option', 'price']


# Product Admin Field
@admin_thumbnails.thumbnail('image')
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'brand', 'sell_price', 'is_available', 'image_tag']
    search_fields = ['name', 'category__name', 'brand__name']
    list_filter = ['category__name', 'brand', 'is_available']
    list_editable = ['is_available']
    inlines = [ProductsImageAdmin]


# Registration models
admin.site.register(Color, ColorAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Currency)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductsImage, ProductImages)
# admin.site.register(Option)
# admin.site.register(OptionValue)
# admin.site.register(ProductVariant, ProductVariantAdmin)
