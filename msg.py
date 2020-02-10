def names(names):

    msg = 'У пользователя были следующие ники:\n\n'
    for i in names:
        f_name, l_name, usr_name = i
        if l_name == '':
            msg += f'  • {f_name} (@{usr_name})\n'
        else:
            msg += f'  • {f_name} {l_name} (@{usr_name})\n'
    return msg
            