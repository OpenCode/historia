from django.contrib import admin
from .models import SiteInfo, Donor, Category, Document


class SiteInfoAdmin(admin.ModelAdmin):
    list_display = ('key', 'value')
    search_fields = ['key', 'value']


class DonorAdmin(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ['name', ]


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ['name', ]


class DocumentAdmin(admin.ModelAdmin):
    list_display = ('name', 'typology', 'year')
    list_filter = ('typology', 'category')
    search_fields = ['name', ]
    readonly_fields=('date', 'uuid')


admin.site.register(SiteInfo, SiteInfoAdmin)
admin.site.register(Donor, DonorAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Document, DocumentAdmin)
