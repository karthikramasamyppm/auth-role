from users.models import Role

users = [
    {
        'username': 'superadmin',
        'password': 'Admin12345^',
        'email': 'superadmin@example.com',
        'first_name': '',
        'last_name': '',
        'is_superuser': True,
        'is_active': True,
        'role': Role.ADMIN
    },
]


def create_data_sample(role, order):
    username = '{}{}'.format(role[1].lower(), order)
    return {
        'username': username,
        'password': 'Admin12345^',
        'email': '{}@example.com'.format(username),
        'first_name': '',
        'last_name': '',
        'is_superuser': False,
        'is_active': True,
        'role': role[0]
    }


def set_users():
    # set admin role
    for i in range(1, 5):
        users.append(create_data_sample(role=Role.ROLE_CHOICES[4], order=i))

    # set supervisor role
    for i in range(1, 11):
        users.append(create_data_sample(role=Role.ROLE_CHOICES[3], order=i))

    # set secretary role
    for i in range(1, 11):
        users.append(create_data_sample(role=Role.ROLE_CHOICES[2], order=i))

    # set teacher role
    for i in range(1, 11):
        users.append(create_data_sample(role=Role.ROLE_CHOICES[1], order=i))

    # set student role
    for i in range(1, 21):
        users.append(create_data_sample(role=Role.ROLE_CHOICES[0], order=i))

    return users
