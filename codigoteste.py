import unittest

class TestCalcularFatura(unittest.TestCase):
    def teste_fatura_valida_sem_desconto_adicional(self):
        produtos = [{"nome": "Produto1", "preco": 100.00, "quantidade": 2}]
        self.assertEqual(calcularFatura(produtos, 10), 180.00)

    def teste_fatura_valida_com_desconto_adicional(self):
        produtos = [{"nome": "Produto1", "preco": 600.00, "quantidade": 2}]
        self.assertEqual(calcularFatura(produtos, 5), 1040.00)

    def teste_produto_com_preco_negativo(self):
        produtos = [{"nome": "Produto1", "preco": -100.00, "quantidade": 2}]
        with self.assertRaises(ProdutoInvalidoException):
            calcularFatura(produtos, 10)

    def teste_produto_com_quantidade_negativa(self):
        produtos = [{"nome": "Produto1", "preco": 100.00, "quantidade": -1}]
        with self.assertRaises(ProdutoInvalidoException):
            calcularFatura(produtos, 10)

    def teste_fatura_com_multiplos_produtos(self):
        produtos = [
            {"nome": "Produto1", "preco": 300.00, "quantidade": 2},
            {"nome": "Produto2", "preco": 200.00, "quantidade": 2}
        ]
        self.assertEqual(calcularFatura(produtos, 20), 960.00)

    def teste_fatura_sem_desconto_adicional(self):
        produtos = [{"nome": "Produto1", "preco": 500.00, "quantidade": 2}]
        self.assertEqual(calcularFatura(produtos, 10), 800.00)
