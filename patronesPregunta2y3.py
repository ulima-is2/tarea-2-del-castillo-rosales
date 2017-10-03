import sqlite3

conn = sqlite3.connect('Cines.db')
c = conn.cursor()

class TipoConexion:
    def __init__(self):
        self.bd = '1'
        self.local = '2'

tipoConn = TipoConexion()

class Entrada:
    def __init__(self, pelicula_id, funcion, cantidad):
        self.pelicula_id = pelicula_id
        self.funcion = funcion
        self.cantidad = cantidad


class Pelicula:
    def __init__(self,  nombre):
        self.nombre = nombre


class Cine:
    def __init__(self,  nombre):
        self.id = None
        self.idP = 1
        self.nombre = nombre
        self.lista_peliculas = []
        self.entradas = []

    def addPelicula(self, pelicula):
        if self.nombre=='CineStark':
            if pelicula.nombre=='Desaparecido':
                pelicula.funciones =['21:00', '23:00']
            elif pelicula.nombre=='Deep El Pulpo':
                pelicula.funciones = ['16:00', '20:00']
            pelicula.id=self.idP
            self.lista_peliculas.append(pelicula)
            self.idP += 1
        elif self.nombre=='CinePlaneta':
            if pelicula.nombre=='Desaparecido':
                pelicula.funciones = ['20:00', '23:00']
            elif pelicula.nombre=='Deep El Pulpo':
                pelicula.funciones = ['16:00']
            elif pelicula.nombre == 'IT':
                pelicula.funciones = ['19:00', '20:30', '22:00']
            elif pelicula.nombre == 'La Hora Final':
                pelicula.funciones = ['21:00']
            pelicula.id = self.idP
            self.lista_peliculas.append(pelicula)
            self.idP += 1

    def listar_peliculas(self, esInput):
        print('********************')
        if esInput is True:
            for pelicula in self.lista_peliculas:
                print("{}. {}".format(pelicula.id, pelicula.nombre))
            return input('Elija pelicula:')
        elif esInput is False:
            for pelicula in self.lista_peliculas:
                print("{}. {}".format(pelicula.id, pelicula.nombre))
        print('********************')

    def getpelicula(self, ideleccion):
        peliculaeleccion = ""
        for pelicula in self.lista_peliculas:
            if str(pelicula.id) == ideleccion:
                peliculaeleccion = pelicula.nombre
        return peliculaeleccion

    def listar_funciones(self, pelicula_id):
        print('Ahora elija la función (debe ingresar el formato hh:mm): ')
        for funcion in self.lista_peliculas[int(pelicula_id) - 1].funciones:
            print('Función: {}'.format(funcion))

        rsltdo1 = input('Funcion:')
        rsltdo2 = input('Ingrese cantidad de entradas: ')

        return [rsltdo1,rsltdo2]

    def guardar_entrada(self, id_pelicula_elegida, funcion_elegida, cantidad):
        self.entradas.append(Entrada(id_pelicula_elegida, funcion_elegida, cantidad))
        return len(self.entradas)


class GrupoCines:
    def __init__(self):
        self.idCine=1
        self.Cines = []

    def getCine(self, idC):
        return self.Cines[idC]

    def addCine(self,cine):
        cine.id = self.idCine
        self.Cines.append(cine)
        self.idCine+=1

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


def printInicial(tipo):
    if tipo == '1':
        print('Ingrese la opción que desea realizar')
        print('(1) Listar cines')
        print('(2) Listar cartelera')
        print('(3) Comprar entrada')
        print('(4) Ver entradas')
        print('(0) Salir')
    elif tipo == '2':
        print('Ingrese la opción que desea realizar')
        print('(1) Listar cines')
        print('(2) Listar cartelera')
        print('(3) Comprar entrada')
        print('(0) Salir')
    return input('Opción: ')


def sqlInit():
    c.execute('''CREATE TABLE IF NOT EXISTS Cines
           (idCine integer, NombreCine text)''')

    c.execute('''CREATE TABLE IF NOT EXISTS PeliculasCine
           (idCine integer, NombreCine text, idPelicula integer, NombrePelicula text)''')

    c.execute('''CREATE TABLE IF NOT EXISTS FuncionesEntradas
         (NombrePelicula text, Funcion text, Entradas text)''')
    conn.commit()

def limpiarBD():
    c.execute('''DROP TABLE IF EXISTS Cines''')
    c.execute('''DROP TABLE IF EXISTS PeliculasCine''')

def listarCinesBD(esInput):
    if esInput is True:
        c.execute('SELECT * FROM Cines')
        print(c.fetchall())
        return input('Primero elija un cine:')
    elif esInput is False:
        c.execute('SELECT * FROM Cines')
        print(c.fetchall())

def listarPeliculasBD(cine, esInput):
    if esInput is True:
        c.execute('SELECT * FROM PeliculasCine where idCine=?', (cine.id,))
        print(c.fetchall())
        return input('Elija pelicula:')
    elif esInput is False:
        c.execute('SELECT * FROM PeliculasCine where idCine=?', (cine.id,))
        print(c.fetchall())


def listarEntradas():
    c.execute('SELECT * FROM FuncionesEntradas')
    print(c.fetchall())

def insertarCine(cine):

    c.execute("INSERT INTO Cines (idCine, NombreCine) VALUES (?,?)", (cine.id, cine.nombre ))

    conn.commit()

    # Insertar Peliculas

    for pelicula in cine.lista_peliculas:
        c.execute("INSERT INTO PeliculasCine (idCine , NombreCine , idPelicula , NombrePelicula )"
                  " VALUES (?,?,?,?)", (cine.id, cine.nombre, pelicula.id , pelicula.nombre))

    conn.commit()

def insertarFuncionEntrada(idPelicula, horarioFuncion, cantidadEntradas):
    c.execute("INSERT INTO FuncionesEntradas (NombrePelicula , Funcion , Entradas )"
              " VALUES (?,?,?)", (idPelicula, horarioFuncion, cantidadEntradas))

    conn.commit()

def main():
    terminado = False
    while not terminado:
        print('********************')
        print('Utilizar:')
        print('(1) Sqlite')
        print('(2) Memoria')
        print('(0) Salir')

        eleccion = input("Elegir opcion: ")

        if eleccion == '1':
            mainBD()
        elif eleccion == '2':
            mainLocal()
        elif eleccion == '0':
            break
        else:
            print("Se ingreso un valor no valido")
            break

def mainLocal():
    terminado = False
    while not terminado:
        # limpiarBD()
        # CineStark
        cineStark = Cine("CineStark")
        cineStark.addPelicula(Pelicula('Desaparecido'))
        cineStark.addPelicula(Pelicula('Deep El Pulpo'))

        # CinePlaneta
        cinePlaneta = Cine("CinePlaneta")
        cinePlaneta.addPelicula(Pelicula('IT'))
        cinePlaneta.addPelicula(Pelicula('La Hora Final'))
        cinePlaneta.addPelicula(Pelicula('Desaparecido'))
        cinePlaneta.addPelicula(Pelicula('Deep El Pulpo'))

        Cines = GrupoCines()
        Cines.addCine(cineStark)
        Cines.addCine(cinePlaneta)

        opcion = printInicial(tipoConn.local)

        if opcion == '1':
            Cines.listarCines(False)
        elif opcion == '2':
            cine = Cines.listarCines(True)
            if cine == '1':
                cine = Cines.getCine(0)
            elif cine == '2':
                cine = Cines.getCine(1)
            else:
                print("Se ingreso un valor no valido")
                break

            cine.listar_peliculas(False)

        elif opcion == '3':
            print('********************')
            print('COMPRAR ENTRADA')

            cine = Cines.listarCines(True)
            if cine == '1':
                cine = Cines.getCine(0)
            elif cine == '2':
                cine = Cines.getCine(1)
            else:
                print("Se ingreso un valor no valido")
                break

            pelicula_id = cine.listar_peliculas(True)

            pelicula_elegida = cine.getpelicula(pelicula_id)

            resultadosFuncion = cine.listar_funciones(pelicula_id)

            codigo_entrada = cine.guardar_entrada(pelicula_elegida, resultadosFuncion[0], resultadosFuncion[1])

            print('Se realizó la compra de la entrada. Código es {}'.format(codigo_entrada))

        elif opcion == '0':

            terminado = True
        else:
            print(opcion)


def mainBD():
    sqlInit()
    terminado = False
    while not terminado:

        # CineStark
        cineStark = Cine("CineStark")
        cineStark.addPelicula(Pelicula('Desaparecido'))
        cineStark.addPelicula(Pelicula('Deep El Pulpo'))

        # CinePlaneta
        cinePlaneta = Cine("CinePlaneta")
        cinePlaneta.addPelicula(Pelicula('IT'))
        cinePlaneta.addPelicula(Pelicula('La Hora Final'))
        cinePlaneta.addPelicula( Pelicula('Desaparecido'))
        cinePlaneta.addPelicula(Pelicula('Deep El Pulpo'))

        Cines = GrupoCines()
        Cines.addCine(cineStark)
        Cines.addCine(cinePlaneta)

        c.execute('SELECT * FROM Cines where NombreCine=?',("CineStark",))
        if c.fetchone() is None:
            insertarCine(cineStark)

        c.execute('SELECT * FROM Cines where NombreCine=?', ("CinePlaneta",))
        if c.fetchone() is None:
            insertarCine(cinePlaneta)

        opcion = printInicial(tipoConn.bd)

        if opcion == '1':
            listarCinesBD(False)
        elif opcion == '2':
            cine = listarCinesBD(True)
            if cine == '1':
                cine = Cines.getCine(0)
            elif cine == '2':
                cine = Cines.getCine(1)
            else:
                print("Se ingreso un valor no valido")
                break

            listarPeliculasBD(cine,False)

        elif opcion == '3':
            print('********************')
            print('COMPRAR ENTRADA')

            cine = listarCinesBD(True)
            if cine == '1':
                cine = Cines.getCine(0)
            elif cine == '2':
                cine = Cines.getCine(1)
            else:
                print("Se ingreso un valor no valido")
                break

            pelicula_id = listarPeliculasBD(cine, True)

            pelicula_elegida = cine.getpelicula(pelicula_id)

            resultadosFuncion = cine.listar_funciones(pelicula_id)

            codigo_entrada = cine.guardar_entrada(pelicula_elegida, resultadosFuncion[0], resultadosFuncion[1])
            insertarFuncionEntrada(pelicula_elegida,resultadosFuncion[0], resultadosFuncion[1])
            print('Se realizó la compra de la entrada. Código es {}'.format(codigo_entrada))
        elif opcion == '4':
            listarEntradas()
        elif opcion == '0':
            terminado = True
        else:
            print(opcion)


if __name__ == '__main__':
    main()
