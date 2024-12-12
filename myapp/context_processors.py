# miapp/context_processors.py
def carrito_context(request):
    carrito = request.session.get("carrito", [])
    cantidad_productos = sum(item["cantidad"] for item in carrito) if carrito else 0
    return {"cantidad_productos": cantidad_productos}