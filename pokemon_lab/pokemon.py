def makeImgTag(link):
    openTag = '<img src=https://img.pokemondb.net/sprites/x-y/normal/'
    closeTag = '.png>'
    return openTag + link + closeTag

def makeDivTag(content):
    return "<div>" + content + "</div>"

def generateBody():
    data = open("pokemon.csv", "r")
    pokemons = data.readlines()
    body = ""
    for pokemon in pokemons[1:]:
        pokemon = pokemon.split(",")[1].lower()
        body += makeDivTag("<b>" + pokemon + "</b>") + makeImgTag(pokemon)

    return body

def makeWebPage():
    webpage = open("pokemon.html", "w")
    header = '''<html>
    <body> <h1>Pokemon</h1>'''

    foot = '''
        </body>
    </html>'''

    webpage.write(header + generateBody() + foot)
    webpage.close()

makeWebPage()
