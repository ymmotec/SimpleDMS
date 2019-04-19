from django.contrib import admin

from .models import Department, Category, Document, Formular

class DocumentAdmin(admin.ModelAdmin):
    fields = (
        ('title', 'document_number'),
        'document_file',
        'category',
        'product',
        'department'
    )

    filter_horizontal = ['product', 'department']

admin.site.register(Department)
admin.site.register(Category)
admin.site.register(Document, DocumentAdmin)
admin.site.register(Formular)
#admin.site.register(Document)
