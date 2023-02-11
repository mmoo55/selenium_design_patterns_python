from paginas.FacebookSignInPage import FacebookSignInPage
from paginas.SpotifyPage import SpotifyPage


class Pagina:

    def __init__(self):
        print("Ingreso a Pagina")

    def spotify_page(self):
        spotify = SpotifyPage()
        return spotify

    def facebook_page(self):
        facebook = FacebookSignInPage()
        return facebook