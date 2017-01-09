from django_remote_forms.forms import RemoteForm


def test_empty_form():
    from tests.data.empty_form import EmptyForm, EXPECTED_FORM
    form = EmptyForm()
    remote_form = RemoteForm(form)
    remote_form_dict = remote_form.as_dict()
    assert remote_form_dict == EXPECTED_FORM


def test_my_form():
    from tests.data.my_form import MyForm, EXPECTED_FORM
    form = MyForm()
    remote_form = RemoteForm(form)
    remote_form_dict = remote_form.as_dict()
    assert remote_form_dict == EXPECTED_FORM


def test_login_form():
    from tests.data.authentication_form import AuthenticationForm, EXPECTED_FORM
    form = AuthenticationForm()
    remote_form = RemoteForm(form)
    remote_form_dict = remote_form.as_dict()
    assert remote_form_dict == EXPECTED_FORM
