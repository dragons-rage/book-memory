# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model


def run(*args):
    # Example: Set password for a user with username 'john'
    # You can pass username and password as script arguments using --script-args if needed.
    if len(args) == 2:
        username = args[0]
        new_password = args[1]
    else:
        print(
            "Usage: python manage.py runscript set_user_password --script-args <username> <new_password>"
        )
        return

    User = get_user_model()
    try:
        user = User.objects.get(username=username)
        user.set_password(new_password)
        user.save()
        print(f"Password for user '{username}' successfully updated.")
    except User.DoesNotExist:
        print(f"User '{username}' not found.")
