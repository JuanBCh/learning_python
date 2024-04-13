import unittest

def es_numero_primo(num):
    if num <= 1:
        return False
    
    for i in range(2, num):
        if num % i == 0:
            return False
    
    return True

class Test(unittest.TestCase):

    def test_numero_menor_igual_1(self):
        numero = 1
        resultado = es_numero_primo(numero)
        self.assertFalse(resultado)

    def test_numero_no_primo(self):
        numero = 4
        resultado = es_numero_primo(numero)
        self.assertEqual(False, resultado)

    def test_numero_primo(self):
        numero = 7
        resultado = es_numero_primo(numero)
        self.assertTrue(resultado)


if __name__ == "__main__":
    unittest.main()