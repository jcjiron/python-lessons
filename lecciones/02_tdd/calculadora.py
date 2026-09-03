def calcular_total(pedido, cupon=None):
    total = sum(producto.precio * cantidad for producto, cantidad in pedido.items)

    if cupon == "DESCUENTO10":
        total *= 0.9
    if total > 500:
        total *= 0.9

    return round(total, 2)
