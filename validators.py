import re

def validate_email(email):
    regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(regex, email) is not None


def validate_positive_integer(value):
    return isinstance(value, int) and value > 0


def validate_input(data):
    if not validate_email(data.get('email', '')):
        raise ValueError('Invalid email format')
    if not validate_positive_integer(data.get('age', 0)):
        raise ValueError('Age must be a positive integer')

    return True


if __name__ == '__main__':
    sample_data = {'email': 'user@example.com', 'age': 30}
    try:
        validate_input(sample_data)
        print('Input is valid')
    except ValueError as e:
        print(f'Input validation error: {e}')