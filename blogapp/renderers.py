from django.forms.renderers import DjangoTemplates


class FormRenderer(DjangoTemplates):
    form_template_name = 'blogapp/form_snippet.html'
