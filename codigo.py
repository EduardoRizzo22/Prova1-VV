class ProdutoInvalidoException(Exception):
    """quando um produto possui dados inválidos."""
    pass

def calcularFatura(products, discount):
   
    # verifica se há produtos com preço ou quantidade inválidos
    for product in products:
        if product["price"] < 0 or product["quantity"] < 0:
            raise ProdutoInvalidoException("Preço ou quantidade inválida para o produto.")

    # calcula o valor total bruto
    total_bruto = sum(product["price"] * product["quantity"] for product in products)

    # aplica o desconto percentual
    total_com_desconto = total_bruto * (1 - discount / 100)

    # aplica desconto adicional de R$ 100,00 para total bruto > R$ 1.000,00
    if total_bruto > 1000:
        total_com_desconto -= 100

    return round(total_com_desconto, 2)
