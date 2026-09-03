"""Sistema de pedidos, estilo ad-hoc: todo suelto, sin tests, sin clases."""

STOCK = {
    "playera": 10,
    "gorra": 2,
    "sudadera": 0,
}

PRECIOS = {
    "playera": 250,
    "gorra": 150,
    "sudadera": 600,
}


def calcular_total(items, cupon=None):
    total = 0
    for producto, cantidad in items.items():
        total += PRECIOS[producto] * cantidad

    # regla de negocio mezclada aquí mismo, sin separar
    if cupon == "DESCUENTO10":
        total *= 0.9
    if total > 500:
        total *= 0.9  # otro 10% si la orden es grande

    return round(total, 2)


def validar_stock(items):
    faltantes = []
    for producto, cantidad in items.items():
        if STOCK.get(producto, 0) < cantidad:
            faltantes.append(producto)
    return faltantes


def procesar_pedido(items, cupon=None):
    faltantes = validar_stock(items)
    if faltantes:
        print(f"No se puede procesar: sin stock de {faltantes}")
        return None

    total = calcular_total(items, cupon)
    print("--- Recibo ---")
    for producto, cantidad in items.items():
        print(f"{producto} x{cantidad} = ${PRECIOS[producto] * cantidad}")
    print(f"TOTAL: ${total}")
    return total


if __name__ == "__main__":
    procesar_pedido({"playera": 2, "gorra": 1}, cupon="DESCUENTO10")
    print()
    procesar_pedido({"sudadera": 1})
