class ListaNumeros:
    numero = 0
    
    def __init__(self, a):
        self.numero = a
    
    def generarLista(self):
        if self.numero > 0:
            lista = []
            pares = []
            impares = []
            repetidos = []
            
            for num in range(self.numero):
                newnum = int(input("Pos {}: ".format(num)))
                
                if newnum % 2 == 0:
                    pares.append(newnum)
                else:
                    impares.append(newnum)
                    
                lista.append(newnum)
                
            lista.sort()
            
            print("orden: ", lista)
            print("par: ", pares)
            print("impar: ", impares)
            
            for item in set(lista):
                if lista.count(item) > 1:
                    repetidos.append(item)
                else:
                    print("No hay numeros repetidos")
            
            print("Repetidos: ", repetidos)
            
def main():
    obj = ListaNumeros(int(input("Numeros a ingresar: ")))
    
    obj.generarLista()
    
if __name__ == "__main__":
    main()