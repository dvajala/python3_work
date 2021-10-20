def city_country(city,country):
    city_country_formatted = f"{city.title()}, {country.title()}"
    return city_country_formatted



def make_album(artist,album):
    album_dict = {'artist':artist,'album':album}
    return album_dict

album1 = make_album('santiago','chile')
album2 = make_album('Beatles','White Album')
album3 = make_album('Rolling stones','ruby tuesday')
print(album1,album2,album3)