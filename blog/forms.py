# # from django import forms
# #
# # from blog.models import Document
# #
# #
# # class DocumentForm(forms.ModelForm):
# #     class Meta:
# #         model = Document
# #         fields = ('description', 'document', )
#
# # forms.py
#
# from django import forms
#
# from .models import Readarticle
# from blog.widgets import MarkdownEditor
#
#
# class PostForm(forms.ModelForm):
#
#     class Meta:
#         model = Readarticle
#         fields = '__all__'
#         widgets = {
#             'content': MarkdownEditor,
#         }
