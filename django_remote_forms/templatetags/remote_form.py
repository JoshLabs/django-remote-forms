import json
from django import template
from django.core.serializers.json import DjangoJSONEncoder

from django_remote_forms.forms import RemoteForm

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
    rf = RemoteForm(form)
    dct = rf.as_dict()
    return json.dumps(dct, cls=DjangoJSONEncoder)

