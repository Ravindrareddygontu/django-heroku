import pytest
from django.contrib.auth import get_user_model


@pytest.fixture
def signup_data():
    return {'username': 'ravindra',
        'email': 'reddy@gmail.com', 'first_name': 'ravindra', 'password1':
        'pass@1234', 'password2': 'pass@1234'}


@pytest.fixture
def signup_for_login():
    return {'username': 'ravindra',
        'email': 'reddy@gmail.com', 'first_name': 'ravindra', 'password': 'pass@1234'}


@pytest.fixture
def login_data(signup_for_login):
    user_model = get_user_model()
    test_user = user_model.objects.create_user(**signup_for_login)
    test_user.set_password(signup_for_login.get('password'))
    return test_user


@pytest.fixture
def logout_data(client, signup_for_login):
    user_model = get_user_model()
    test_user = user_model.objects.create_user(**signup_for_login)
    test_user.set_password(signup_for_login.get('password'))
    test_user.save()
    client.login(**signup_for_login)
    return test_user









