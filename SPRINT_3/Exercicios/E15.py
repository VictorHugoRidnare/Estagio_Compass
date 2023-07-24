class Lampada:
    def __init__(lamp, esta_ligada = False):
        lamp.esta_ligada = esta_ligada


    def ligada(lamp):
        lamp.esta_ligada = True
    

    def desliga(lamp):
        lamp.esta_ligada = False
    
    
    def esta_ligada(lamp):
        return lamp.esta_ligada
    
lampada = Lampada()
lampada.ligada()
print("A lâmpada está ligada?", lampada.esta_ligada)
lampada.desliga()
print("A lâmpada ainda está ligada?", lampada.esta_ligada)