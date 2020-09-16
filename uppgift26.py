'''
Nu ska vi leka med att skicka parametrar till en databas!

OMDB är en IMDB-liknande hemsida på nätet, som också tillhandahåller
ett API där man kan göra sökningar.

26.1 Jag har fixat en API-nyckel åt oss! Därför kan vi använda detta
     webb-API (som är ett REST-API) och leka. Testa att skriva följande
     i en browser:

      http://www.omdbapi.com/?t=Alien&apikey=9f6d550c

     Ändra på "Alien" till en annan film!

26.2 Använd requests.get() med ovanstående URL, fast ta bort ? och framåt.
     Använd istället params={"t": "Alien", "apikey": "9f6d550c"} så kommer
     requests att lägga på ? och & och sånt strunt själv. :)

     Pretty printa (pprint) JSON-resultatet med ett Pythonprogram!

26.3 Bygg ett Pythonprogram där användaren frågar efter en film, och skriv
     sedan ut en snygg infobox om filmen, typ så här:

*** Resultat från OMDB! ***
Alien (1979) regisserades av Ridley Scott.
      Skådisar: Tom Skerritt, Sigourney Weaver, Veronica Cartwright, Harry Dean Stanton
    IMDB betyg: 8.4
        Awards: Won 1 Oscar. Another 16 wins & 22 nominations.
         Längd: 117 min
'''

import json
import requests
from pprint import pprint


def main():
    movie = input("Ange film: ")
    r = requests.get("http://www.omdbapi.com/", params={"t": movie, "apikey": "9f6d550c"})
    text = r.text
    result = json.loads(text)

    if "Error" in result:
        print("Hittar inte filmen!")
        main()

    year = result['Year']
    title = result['Title']
    director = result['Director']
    actors = result['Actors']
    imdb = result['imdbRating']
    awards = result['Awards']
    runtime = result['Runtime']

    print("*** Resultat från OMDB! ***")
    print(f"{title} ({year}) regisserades av {director}.")
    print(f"Skådisar:   {actors}")
    print(f"IMDB betyg: {imdb}")
    print(f"Awards:     {awards}")
    print(f"Längd:      {runtime} min")


main()
