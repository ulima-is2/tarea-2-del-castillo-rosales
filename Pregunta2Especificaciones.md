# Sustento de Patrones de Diseño Elegidos

### 1. Factory

Utilizamos este patrón pues al comienzo teniamos dos cines que repetian operaciones y métodos. El detalle ocurre si queremos modificar el caso de negocio y nos piden agregar muchos más cines. Es ahí cuando usamos este patrón y creamos una clase factory llamada Cine que tendrá los métodos compartidos por todos los cines a instanciarse. De esa forma se modulariza el código, se restan lineas de código redundante e innecesarias y se hace más eficiente el programa.

<table>
<tr>
<td>
  <b>Código Original</b>
</td>
<td>
  <b>Código Modificado</b>
</td>
</tr>
<tr>
<td>
   <pre lang="python">
    class CinePlaneta:
      def __init__(self):...
      
      def listar_peliculas(self):...

      def listar_funciones(self, ...):...

      def guardar_entrada(self, ...):...

    class CineStark:
      def __init__(self):...

      def listar_peliculas(self):...

      def listar_funciones(self, ...):...

      def guardar_entrada(self, ...):...     
   </pre>
</td>
<td>
  <pre lang="python">
 class Cine:
    def __init__(self,  ...):...
    
    def addPelicula(self, ...):...    

    def listar_peliculas(self, ...):...

    def getpelicula(self, ...):...
        
    def listar_funciones(self, ...):...
    
    def guardar_entrada(self, ...):...
    
  </pre>
</td>
</tr>
</table>

### 2. Composite

Usamos este patrón para definir métodos que realicen la función de imprimir la información solicitada de acuerdo al caso específico. En la definición de adapter se habla de trabajar con librerias; sin embargo, ya que el código es pequeño y es un programa pequeño los "adaptadores" son métodos que se encargan de realizar la impresión comportandose de manera dinámica en respuesta al input ingresado por el usuario.

<table>
<tr>
<td>
  <b>Código Original</b>
</td>
<td>
  <b>Código Modificado</b>
</td>
</tr>
<tr>
<td>
   <pre lang="python">
    class CineStark:
      def __init__(self):
        peliculaD = Pelicula(1, 'Desparecido')
        peliculaDeep = Pelicula(2, 'Deep El Pulpo')

        peliculaD.funciones = ['21:00', '23:00']
        peliculaDeep.funciones = ['16:00', '20:00']

        self.lista_peliculas = [peliculaD, peliculaDeep]
        self.entradas = []
        ...
   </pre>
</td>
<td>
  <pre lang="python">
  def mainLocal():
    terminado = False
    while not terminado:
        
        # CineStark
        cineStark = Cine("CineStark")
        cineStark.addPelicula(Pelicula('Desaparecido'))
        cineStark.addPelicula(Pelicula('Deep El Pulpo'))

  </pre>
</td>
</tr>
</table>

### 3. Adapter

Este patrón lo usamos para diseñar la estructura jerárquica que el programa sigue. Dicho patrón nos permite agregar dinámicamente, por ejemplo, nuevas películas a un determinado cine o nuevos cines a la lista de cine. Todo esto siguiendo un modelo con estructura de forma de árbol y haciendolo recursivamente.

<table>
<tr>
<td>
  <b>Código Original</b>
</td>
<td>
  <b>Código Modificado</b>
</td>
</tr>
<tr>
<td>
   <pre lang="python">
   def Main():
   ...
     elif opcion == '2':
        print('********************')
        print('Lista de cines')
        print('1: CinePlaneta')
        print('2: CineStark')
        print('********************')
   </pre>
</td>
<td>
  <pre lang="python">  
  class GrupoCines:
  ...
      def listarCines(self, esInput):
        print('********************')
        print('Lista de cines')
        if esInput is True:
            for cine in self.Cines:
                print("{}: {}".format(cine.id, cine.nombre))
            return input('Primero elija un cine:')
        elif esInput is False:
            for cine in self.Cines:
                print("{}: {}".format(cine.id, cine.nombre))
        print('********************')
    def Main():
    ...
        elif opcion == '2':
          cine = Cines.listarCines(...)
  </pre>
</td>
</tr>
</table>
