

class Productos:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def info (self):
        print("Producto: {}".format(self.nombre))
        print("Precio: ${}".format(self.precio))
        print("Stock disponible: {}".format(self.stock))

    def stock_actualizar(self, cantidad):
        self.stock += cantidad

class Bebidas(Productos):
    def __init__(self, nombre, precio, stock, tamano, marca, sabor):
        super().__init__(nombre, precio, stock)
        self.tamano = tamano
        self.marca = marca
        self.sabor = sabor
    
    def info (self):
        print("Producto: {}".format(self.nombre))
        print("Marca: {}".format(self.marca))
        print("Sabor: {}".format(self.sabor))
        print("Tamaño: {} Cc.".format(self.tamano))
        print("Precio: ${}".format(self.precio))
        print("Stock disponible: {}".format(self.stock))
        
       

class Tabaco(Productos):
    def __init__(self, nombre, marca,cantidad_por_paquete, precio, stock):
        super().__init__(nombre, precio, stock)
        self.marca = marca
        self.cantidad_por_paquete = cantidad_por_paquete
        
    def info (self):
        print("Producto: {}".format(self.nombre))
        print("Marca: {}".format(self.marca))
        print("cantidad por paquete: {} unidades.".format(self.cantidad_por_paquete))       
        print("Precio: ${}".format(self.precio))
        print("Stock disponible: {}".format(self.stock))
        
        

class Dulces(Productos):
    def __init__(self, nombre, marca, sabor, precio, stock):
        super().__init__(nombre, precio, stock)
        self.sabor = sabor
        self.marca = marca
    
    def info (self):
        print("Producto: {}".format(self.nombre))
        print("Marca: {}".format(self.marca))
        print("Sabor: {}".format(self.sabor))
        print("Precio: ${}".format(self.precio))
        print("Stock disponible: {}".format(self.stock))
        