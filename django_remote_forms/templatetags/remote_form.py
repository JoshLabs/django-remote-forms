import json
from django import template
from django import forms
from django.core.serializers.json import DjangoJSONEncoder
from django_remote_forms.forms import RemoteForm, RemoteFormSet

register = template.Library()


@register.filter
def form_as_json(form):
    """
    Usage:

        {% load remote_form %}

        <script type='text/javascript'>
            var formData = {{ form|form_as_json }}
        </script>
    """
    if isinstance(form, forms.BaseFormSet):
        rf = RemoteFormSet(form)
    else:
        rf = RemoteForm(form)
    dct = rf.as_dict()
    return json.dumps(dct, cls=DjangoJSONEncoder)
