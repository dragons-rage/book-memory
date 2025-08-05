# my_app/scripts/create_user.py
from django.contrib.auth import get_user_model
import argparse


def run(*args):
    parser = argparse.ArgumentParser()
    parser.add_argument("user", type=str)
    parser.add_argument("email", type=str)
    parser.add_argument("password", type=str)
    arglist = parser.parse_args(args)

    User = get_user_model()

    if not User.objects.filter(username=arglist.user).exists():
        user = User.objects.create_user(
            username=arglist.user, email=arglist.email, password=arglist.password
        )
        print(f"User '{user.username}' created successfully.")
    else:
        print(f"User '{arglist.user}' already exists.")
