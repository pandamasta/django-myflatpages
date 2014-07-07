from django.contrib import admin
#from django.contrib.flatpages.models import FlatPage
from myflatpages.models import FlatPage
from django.utils.translation import ugettext_lazy as _
#from django.contrib.flatpages.forms import FlatpageForm

from django_summernote.admin import SummernoteModelAdmin
#modif 2014 04 14
#class FlatPageAdmin(admin.ModelAdmin):
class FlatPageAdmin(SummernoteModelAdmin):
    #form = FlatpageForm
    fieldsets = (
        (None, {'fields': ('url', 'title', 'content', 'sites', 'order')}),
        (_('Advanced options'), {'classes': ('collapse',), 'fields': ('enable_comments', 'registration_required', 'template_name')}),
    )
    list_display = ('url', 'title', 'order')
    list_filter = ('sites', 'enable_comments', 'registration_required')
    search_fields = ('url', 'title')

admin.site.register(FlatPage, FlatPageAdmin)
