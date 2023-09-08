Para empezar a probar la aplicacion hay que iniciarla como cualquier otra con "python manage.py runserver" y entrar a la url "app-entrega3/" alli se vera el inicio de la pagina web.

En el navbar se podran observar las views las cuales son:

-Producto
-Categoria
-Cliente
-Buscar
-Lista de Productos
-Lista de Categorias

Dentro de las views de Producto, Categoria y Cliente se podran añadir las respectivas clases:

-En "Producto" se podra añadir el nombre del mismo, su descripcion y el precio en ese orden respectivamente.

-En "Categoria" se podra añadir la Categoria de productos.

-En "Cliente" se podra añadir el nombre del cliente y su email.

Pasando a las siguientes views:

-En "Buscar" se podra observar una barra de busqueda que permitira buscar los productos almacenados en la base de datos.

-En "Lista de Productos" se mostrara la lista de los productos guardados con sus descripciones y precios incluidos.

-En "Lista de Categorias" se podran ver los titulos de las categorias guardadas.

Cada una de las views funciona gracias a la herencia desde "padre.html" y cada una tiene su propio html para su funcion.