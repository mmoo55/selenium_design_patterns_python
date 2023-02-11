import unittest

from datos.ClienteEntity import ClienteEntity
from datos.ClienteRepository import ClienteRepository
from paginas.Pagina import Pagina


class TestPaginas(unittest.TestCase):

    def test_spotify(self):

        pagina = Pagina()
        #pagina.spotify_page().goTo("Chrome")

        facebook = pagina.facebook_page()
        facebook.goTo("Chrome")

        message = "Valore de la prueba no es verdadero"
        print(facebook.isAt())
        self.assertTrue(facebook.isAt(), message)

        cliente = ClienteEntity()
        cliente.set_nombres("Lizet")
        cliente.set_apellidos("Canazas")

        repository = ClienteRepository()
        repository.guardarCliente(cliente)