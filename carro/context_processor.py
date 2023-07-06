'''def importe_total_carro(request):
    total=0
    if request.user.is_authenticated:
        carro = request.session.get("carro", {})
        for key, value in request.session["carro"].items():
            total=total+(float(value["precio"]))
    return {"importe_total_carro": total}    '''
    
def importe_total_carro(request):
    total = 0
    if request.user.is_authenticated:
        carro = request.session.get("carro", {})
        for key, value in carro.items():
            precio = float(value.get("precio", 0))
            total += precio
    return {"importe_total_carro": total}
