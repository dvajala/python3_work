def get_formatted_name(first_name,last_name,middle_name=''):
    """Return a full name, neatly formatted"""
    if middle_name:    
        full_name = f"{first_name} {middle_name} {last_name}"
        return full_name.title()
    else:
        full_name = f"{first_name} {last_name}"
        return full_name.title()

musician = get_formatted_name(first_name='jimi',middle_name='lee',last_name='hendricks')

print(musician)