from browsers.Browser import Browser


class SpotifyPage:

    url = "https://www.spotify.com/pe/signup?forward_url=https%3A%2F%2Fopen.spotify.com%2F"
    title = "Registrarte - Spotify"

    def __init__(self):
        self.nav = Browser()
        print("Hola ingresaste a SpotifyPage")

    def goTo(self, navigator):
        self.nav.goTo(self.url, navigator)

    def isAt(self):
        print(self.nav.titulo())
        print(self.title)
        return self.nav.titulo() == self.title

# Un constructor crea