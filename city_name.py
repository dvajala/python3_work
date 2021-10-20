def city_country(city,country):
    city_country_formatted = f"{city.title()}, {country.title()}"
    return city_country_formatted



def make_album(artist,album,songs=None):
    album_dict = {'artist':artist,'album':album}
    if songs:
        album_dict['songs'] = songs
    return album_dict

while True:
    print("Tell me the artist and album name\nEnter 'q' to quit at any time")
    artist = input("Enter artist name: ")
    if artist == 'q':
        break
    album = input("Enter album name: ")
    if album == 'q':
        break

    my_dict = make_album(artist,album)
    print(my_dict)