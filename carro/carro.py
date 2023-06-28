class Carro:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        self.carro = {} 
        carro = self.session.get("carro")
        if not carro:
            carro = self.session["carro"] = {}
        
        self.carro = carro

    def agregar(self, producto):
        if str(producto.id) not in self.carro.keys():
            self.carro[producto.id] = {
                "id": producto.id,
                "nombre": producto.nombre,
                "precio": producto.precio,
                "cantidad": 1,
                "imagen": producto.imagen.url,
            }
        else:
            for key, value in self.carro.items():
                if key == str(producto.id):
                    value["cantidad"] += 1
                    value["precio"] += float(producto.precio)
                    break
        self.guardar()

    def guardar(self):
        self.session["carro"] = self.carro
        self.session.modified = True

    def eliminar(self, producto):
        producto_id = str(producto.id)
        if producto_id in self.carro:
            del self.carro[producto_id]
            self.guardar()

    def restar(self, producto):
        for key, value in self.carro.items():
            if key == str(producto.id):
                value["cantidad"] -= 1
                value["precio"] -= float(producto.precio)
                if value["cantidad"] <= 0:
                    self.eliminar(producto)
                break
        self.guardar()

    def vaciar(self):
        self.session["carro"] = {}
        self.session.modified = True
