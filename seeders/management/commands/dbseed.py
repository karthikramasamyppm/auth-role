from __future__ import print_function
from django.core.management.base import BaseCommand

from users.models import User as UserModel, Role
from seeders.tables.users import set_users


class Command(BaseCommand):
    help = 'Generate sample data to database'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def add_arguments(self, parser):
        parser.add_argument('-u', '--users', action='store_true', help='Generate users table')

    def handle(self, *args, **options):
        if options['users'] is not None:
            users = set_users()

            for user in users:
                role_id = user['role']

                if Role.objects.filter(pk=user['role']).exists():
                    role = Role.objects.filter(pk=role_id).get()
                else:
                    role = Role.objects.create(id=role_id)
                    print('add new role: {}'.format(user['role']))

                del user['role']
                new_user = UserModel.objects.create_user(**user)
                print('add new user: {}'.format(user['username']))
                new_user.roles.add(role)
                new_user.save()
        else:
            exit(1)
        exit(0)
