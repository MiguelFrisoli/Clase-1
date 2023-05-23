from Productos import Bebidas
from Productos import Tabaco
from Productos import Dulces

# instancio y creo el objeto
caramelo_1 = Dulces ("caramelos", "mogul", "acidos", 12, 55)
caramelo_1.info()
caramelo_1.stock_actualizar(55)

# # ver la info de la golosina
caramelo_1.info()

# # actualizar el invantario, y ver info del producto
caramelo_1.stock_actualizar(-10)
caramelo_1.info()

# instancio y creo el objeto
gaseosa_1 = Bebidas ("Gaseosa", 400, 36, 1500, "Talca", "Pomelo")
gaseosa_1.info()
gaseosa_1.stock_actualizar(12)

# ver la info de la golosina
gaseosa_1.info()

# actualizar el invantario, y ver info del producto
gaseosa_1.stock_actualizar(-6)
gaseosa_1.info()

# # instancio y creo el objeto
cigarrillo_1 = Tabaco ("Cigarrillo", "Malboro", 20, 750, 20)
cigarrillo_1.info()
cigarrillo_1.stock_actualizar(12)

# # ver la info de la golosina
cigarrillo_1.info()

# # actualizar el invantario, y ver info del producto
cigarrillo_1.stock_actualizar(-6)
cigarrillo_1.info()