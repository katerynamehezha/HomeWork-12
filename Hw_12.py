# Task 1 
def is_admin(fn):
    def wrapper(*args, **kwargs):
        user_type = kwargs.get('user_type')
        if user_type != 'admin':
            raise ValueError('Permission denied')
        return fn(*args, **kwargs)
    return wrapper


@is_admin
def show_customer_receipt(*args, **kwargs):
    print('Showing customer receipt...')


try:
    show_customer_receipt(user_type='user')
except ValueError as e:
    print(f'Error: {e}')

try:
    show_customer_receipt(user_type='admin')
    print('Correct!')
except ValueError as e:
    print(f'Error: {e}')

    

# Task 2
def catch_errors(fn):
    """
    Decorator `catch_errors` catches exceptions that occur inside the decorated function and prints information about the first error encountered.

    Usage examples:
    >>> @catch_errors
    >>> def some_function_with_risky_operation(data):
    >>>     print(data['key'])
    >>>
    >>> some_function_with_risky_operation({'foo': 'bar'})
    Found 1 error during execution of your function: KeyError 'key'
    >>> some_function_with_risky_operation({'key': 'bar'})
    bar
    """
    def wrapper(*args, **kwargs):
        try:
            return fn(*args, **kwargs)
        except Exception as e:
            print(f'Found 1 error during execution of your function: {type(e).__name__} {str(e)}')
    return wrapper


@catch_errors
def some_function_with_risky_operation(date):
    print(date['key'])

some_function_with_risky_operation({'foo': 'bar'})
some_function_with_risky_operation({'key': 'bar'})


