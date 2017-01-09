from django.forms import formset_factory
from django_remote_forms.forms import RemoteFormSet


def test_empty_formset():
    from tests.data.empty_form import EmptyForm, EXPECTED_EMPTY_FORMSET
    EmptyFormSet = formset_factory(EmptyForm, extra=0)
    formset = EmptyFormSet()
    remote_formset = RemoteFormSet(formset)
    remote_formset_dict = remote_formset.as_dict()
    assert remote_formset_dict == EXPECTED_EMPTY_FORMSET


def test_empty_form_formset():
    from tests.data.empty_form import EmptyForm, EXPECTED_FORMSET
    EmptyFormSet = formset_factory(EmptyForm)
    formset = EmptyFormSet()
    remote_formset = RemoteFormSet(formset)
    remote_formset_dict = remote_formset.as_dict()
    assert remote_formset_dict == EXPECTED_FORMSET


def test_empty_form_formset_of_three():
    from tests.data.empty_form import EmptyForm, EXPECTED_FORMSET_THREE
    EmptyFormSet = formset_factory(EmptyForm, extra=3)
    formset = EmptyFormSet()
    remote_formset = RemoteFormSet(formset)
    remote_formset_dict = remote_formset.as_dict()
    assert remote_formset_dict == EXPECTED_FORMSET_THREE
