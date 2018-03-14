from django.contrib import admin
from blog.models import Article , Readarticle, Author , Mythought
from django.utils.html import mark_safe
from markdown import markdown
from martor.widgets import AdminMartorWidget

from blog.models import Readarticle

# Registering Tutorial editor in admin
# Define the admin class
class Admin_Article(admin.ModelAdmin):
    list_display = ('title', 'subject','created_at','user' , 'document','views')
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()

class Admin_Readarticle(admin.ModelAdmin):

    list_display = ('title', 'get_subject','written_by','written_at','get_document','get_views')
    def get_subject(self , obj):
        return obj.subject_other
    def get_document(self , obj):
        return obj.document_other
    def get_views(self , obj):
        return obj.view_other

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()

# Register admin class with the associated model
class Admin_Author(admin.ModelAdmin):
    list_display = ('blogger', 'strong','about_author', 'document')
    description = 'Description'
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()

class Admin_Commentblog(admin.ModelAdmin):
    list_display = ('topic', 'message','commented_at')
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()

class Admin_Mythought(admin.ModelAdmin):
    list_display = ('header','image')
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()
# Register the admin class with the associated model
admin.site.register(Article, Admin_Article)
admin.site.register(Author , Admin_Author)
admin.site.register(Readarticle , Admin_Readarticle)
admin.site.register(Mythought , Admin_Mythought)
