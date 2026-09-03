# 1️⃣ Ad-hoc / Code-First

## La idea

Escribes código directo, sin diseño previo ni pruebas. Vas ajustando sobre
la marcha, probando manualmente (corriendo el script y viendo qué sale).
Es la forma más natural en la que casi todos empezamos a programar.

- Cero (o casi cero) pruebas automatizadas
- Debug manual: `print()`, correr y ver
- Decisiones rápidas, guiadas por intuición
- Todo suele vivir en un solo archivo/función

**Bueno para:** scripts de un solo uso, prototipos, explorar una idea rápido.
**Riesgo:** conforme el archivo crece, le tienes miedo a tocarlo — no hay
red de seguridad (tests) que te avise si rompiste algo.

## El ejemplo

`pedidos.py` resuelve el sistema de pedidos completo: calcula el total de
una orden, aplica un cupón de descuento, valida que haya stock, y arma el
recibo. Todo en un solo archivo, funciones sueltas, sin clases, sin tests.
Nota cómo las reglas de negocio (el 10% si superas $500, el cupón fijo)
están mezcladas directamente con la lógica de armar el recibo — típico del
estilo ad-hoc.

Corre el ejemplo:

```bash
python3 lecciones/01_ad_hoc/pedidos.py
```

## Qué observar

- No hay ninguna prueba: para saber si funciona, lo corres y lees el
  `print()`.
- Si mañana quisiera agregar un cupón nuevo o cambiar el umbral del 10%,
  edito `calcular_total` directo y cruzo los dedos.
- Es rápido de escribir — para un script de una tarde, está perfecto.
