import unittest
from scr.logica.Fecha import Fecha


class PruebaFecha(unittest.TestCase):
    def test_ValidarFecha_retonaTrueoFalse(self):
        # Arrange
        cases = [
            (20, 6, 2008, True),
            (21, 00, 3000, False),
            (21, 13, 3000, False),
            (0, 11, 2000, False),
            (32, 11, 2000, False),
            (31, 11, 2000, False),
            (31, 12, 2000, True),
            (30, 2, 2008, False),
            (29, 2, 2008, True),
            (29, 2, 2000, True),
            (29, 2, 2007, False),
            (29, 2, 1900, False),
        ]
        objFecha= Fecha()
        for i, (dia, mes, anio, resultadoEsperado) in enumerate(cases, 1):
            with self.subTest(case=i):
                # do
                resultadoActual = objFecha.validaFecha(dia, mes, anio)

                # Assert
                self.assertEqual(resultadoEsperado, resultadoActual,
                                 f"Fallo en el caso {i}: valida({dia}, {mes}, {anio}) = {resultadoActual},"
                                 f" esperado {resultadoEsperado}")
