from .models import Books
from django import forms
from django.contrib import admin


class BooksAdminForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(BooksAdminForm, self).__init__(*args, **kwargs)


class BooksAdmin(admin.ModelAdmin):
    form = BooksAdminForm
    list_display = ('book_title', 'book_author')
    list_filter = ('book_title', 'book_author')
    search_fields = ('book_title', 'book_author')

    fieldsets = (
        ('General', {
            'fields': ('book_title', 'book_author')
        }),
    )

    def save_model(self, request, obj, form, change):
        result = super(BooksAdmin, self).save_model(request, obj, form,
                                                       change)

        return result


admin.site.register(Books, BooksAdmin)
