import json

from django_remote_forms.forms import RemoteForm


def test_empty_form():
    from tests.data.empty_form import EmptyForm, EXPECT
    form = EmptyForm()
    remote_form = RemoteForm(form)
    remote_form_dict = remote_form.as_dict()
    assert remote_form_dict == EXPECT


def test_my_form():
    from tests.data.my_form import MyForm, EXPECT
    form = MyForm()
    remote_form = RemoteForm(form)
    remote_form_dict = remote_form.as_dict()
    assert remote_form_dict == EXPECT


def test_login_form():
    from tests.data.authentication_form import AuthenticationForm, EXPECT
    form = AuthenticationForm()
    remote_form = RemoteForm(form)
    remote_form_dict = remote_form.as_dict()
    assert remote_form_dict == EXPECT
