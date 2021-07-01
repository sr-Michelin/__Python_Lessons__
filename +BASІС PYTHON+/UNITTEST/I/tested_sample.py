def get_fd_nm(first, last='', middle=''):
    if middle:
        return f'{first} {middle} {last}'.title()
    if last:
        return f'{first} {last}'.title()
    else:
        return f'{first}'.title()
