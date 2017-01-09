# django-remote-forms

## Installation

```bash
pip install git+git@github.com:valohai/django-remote-forms.git
```

A package that allows you to serialize django forms, including fields and widgets into Python
dictionary for easy conversion into JSON and expose over API.

## Testing

```bash
pip install -r requirements-dev.txt
pytest   # To run tests against your (virtual) environment
tox      # To run tests with various Python version defined in tox.ini
```

## Usage

### Minimal Example

```python
import json
from django.contrib.auth.forms import AuthenticationForm
from django_remote_forms.forms import RemoteForm

form = AuthenticationForm()
remote_form = RemoteForm(form)
remote_form_dict = remote_form.as_dict()
print(json.dumps(remote_form_dict))
```
```json
{
  "typed_errors": {},
  "errors": {},
  "title": "AuthenticationForm",
  "fieldsets": [],
  "label_suffix": ":",
  "name": "AuthenticationForm",
  "non_field_errors": [],
  "fields": {
    "username": {
      "widget": {
        "is_localized": false,
        "is_required": true,
        "needs_multipart_form": false,
        "input_type": "text",
        "title": "TextInput",
        "attrs": {
          "maxlength": "254",
          "autofocus": ""
        },
        "is_hidden": false
      },
      "min_length": null,
      "required": true,
      "label": "Username",
      "error_messages": {
        "required": "This field is required."
      },
      "max_length": 254,
      "title": "UsernameField",
      "initial": null,
      "help_text": ""
    },
    "password": {
      "widget": {
        "is_localized": false,
        "is_required": true,
        "needs_multipart_form": false,
        "input_type": "password",
        "title": "PasswordInput",
        "attrs": {},
        "is_hidden": false
      },
      "min_length": null,
      "required": true,
      "label": "Password",
      "error_messages": {
        "required": "This field is required."
      },
      "max_length": null,
      "title": "CharField",
      "initial": null,
      "help_text": ""
    }
  },
  "is_bound": false,
  "ordered_fields": [
    "username",
    "password"
  ],
  "data": {
    "username": null,
    "password": null
  },
  "prefix": null
}
```

### An API endpoint serving remote forms

```python
from django.core.serializers.json import simplejson as json, DjangoJSONEncoder
from django.http import HttpResponse
from django.middleware.csrf import CsrfViewMiddleware
from django.views.decorators.csrf import csrf_exempt

from django_remote_forms.forms import RemoteForm

from my_awesome_project.forms import MyAwesomeForm


@csrf_exempt
def my_ajax_view(request):
    csrf_middleware = CsrfViewMiddleware()

    response_data = {}
    if request.method == 'GET':
        # Get form definition
        form = MyAwesomeForm()
    elif request.raw_post_data:
        request.POST = json.loads(request.raw_post_data)
        # Process request for CSRF
        csrf_middleware.process_view(request, None, None, None)
        form_data = request.POST.get('data', {})
        form = MyAwesomeForm(form_data)
        if form.is_valid():
            form.save()

    remote_form = RemoteForm(form)
    # Errors in response_data['non_field_errors'] and response_data['errors']
    response_data.update(remote_form.as_dict())

    response = HttpResponse(
        json.dumps(response_data, cls=DjangoJSONEncoder),
        mimetype="application/json"
    )

    # Process response for CSRF
    csrf_middleware.process_response(request, response)
    return response
```

## Sample Implementation

If you don't mind digging around a little bit to learn about different the components that might be
necessary for an implementation of django-remote-forms, check out
Django Remote Admin [django-remote-admin](https://github.com/tarequeh/django-remote-admin)

## DjangoCon Proposal

Please go through the original [DjangoCon US 2012 talk](http://www.slideshare.net/tarequeh/django-forms-in-a-web-api-world)
to understand the problem sphere, motivations, challenges and implementation of Django Remote Forms.

This is a bit lengthy. But if you want to know more about my motivations behind developing django-remote-forms
then read on.


>In our quest to modularize the architecture of web applications, we create self-containing backend
>systems that provide web APIs for programmatic interactions. This gives us the flexibility to
>separate different system components. A system with multiple backend components e.g. user profile
>engine, content engine, community engine, analytics engine may have a single frontend application
>that fetches data from all of these components using respective web APIs.

>With the increased availability of powerful JavaScript frameworks, such frontend applications are
>often purely JS based to decrease application footprint, increase deployment flexibility and
>separate presentation from data. The separation is very rewarding from a software engineering
>standpoint but imposes several limitations on system design. Using django to construct the API for
>arbitrary consumers comes with the limitation of not being able to utilize the powerful django form
>subsystem to drive forms on these consumers. But is there a way to overcome this restriction?

>This is not a trivial problem to solve and there are only a few assumptions we can make about the
>web API consumer. It can be a native mobile or desktop - application or browser. We advocate that
>web APIs should provide sufficient information about 'forms' so that they can be faithfully
>reproduced at the consumer end.

>Even in a API backend built using django, forms are essential for accepting, filtering, processing
>and saving data. The django form subsystem provides many useful features to accomplish these tasks.
>At the same time it facilitates the process of rendering the form elements in a browser
>environment. The concepts of form fields combined with widgets can go a long way in streamlining
>the interface to interact with data.

>We propose an architecture to serialize information about django forms (to JSON) in a framework
>independent fashion so that it can be consumed by any frontend application that renders HTML. Such
>information includes but is not limited to basic form configurations, security tokens (if
>necessary), rendering metadata and error handling instructions. We lovingly name this architecture
>django-remote-forms.

>At WiserTogether, we are in the process of building a component based architecture that strictly
>provides data endpoints for frontend applications to consume. We are working towards developing
>our frontend application for web browsers using backbone.js as MVC and handlebars as the templating
>engine. django-remote-forms helps us streamline our data input interface with the django forms
>living at the API backend.
