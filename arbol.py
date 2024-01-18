class Arbol:
    numero = 0
    
    def __init__(self, a):
        self.numero = a
        
    def generarArbol(self):
        if self.numero > 0:
            for num in range(1, self.numero + 1):
                print('*' * num)
                
def main():
    obj = Arbol(int(input("Numero: ")))
    
    obj.generarArbol()
    
if __name__ == "__main__":
    main()