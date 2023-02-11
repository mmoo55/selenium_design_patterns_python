from browsers.Browser import Browser


class FacebookSignInPage:

    url = "https://www.facebook.com/"
    title = "Facebook - Inicia sesión o regístrate"

    def __init__(self):
        self.nav = Browser()
        print("Ingresando a Facebook")

    def goTo(self, navigator):
        self.nav.goTo(self.url, navigator)

    def isAt(self):
        return self.nav.titulo() == self.title