alien_0 = {'color': 'green',"points":5}

print(alien_0)

alien_0['color'] = 'yellow'

print(alien_0)

del alien_0['points']

print(alien_0)

languages = {
    'dinesh': 'python',
    'veda': 'youtube',
    'anu': 'nvivo'
}
language = languages.get('sarah','No language')
print(f"Veda's favorite language is {language.title()}")