from django.http import QueryDict
from django.utils import six
from django.utils.functional import Promise

try:
    from django.utils.encoding import force_text
except ImportError:
    from django.utils.encoding import force_unicode as force_text


def resolve_promise(o):
    if isinstance(o, dict):
        return {k: resolve_promise(v) for k, v in o.items()}
    if isinstance(o, six.text_type):
        return force_text(o)
    elif isinstance(o, (list, tuple)):
        o = [resolve_promise(x) for x in o]
    elif isinstance(o, Promise):
        try:
            o = force_text(o)
        except:
            # Item could be a lazy tuple or list
            try:
                o = [resolve_promise(x) for x in o]
            except:
                raise Exception('Unable to resolve lazy object %s' % o)
    elif callable(o):
        o = o(o.im_self)

    return o
