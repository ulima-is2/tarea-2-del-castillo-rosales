### 1) Principio Single Responsibility o Responsabilidad Única:

  Se viola este principio debido a que las clases de cine definidas como "CinePlaneta" y "CineStark" llevan acabo los mismos métodos y operaciones por lo que se genera un aumento de líneas de código innecesario y hacen que las clases tengan más lineas de código que se redunda. Ya que se crean objetos a partir de las clases, pensamos que una solución sería usar una clase gestión de películas que haga las operaciones y métodos que se repiten, cumpliendo así con el principio.
  
---

### 2) Principio OPEN-CLOSE: 

Este principio es violado ya que la forma en que está estructurado el código lo obligaría en un futuro a modificarse si es que uno quiere agregar más cines o atributos a cada uno de estos. Por lo tanto, lo que se debe hacer es usar la abstracción y crear una clase padre que podría llamarse Cine en la que se van a definir métodos y propiedades generales(abstractas) para todos los cines. Finalmente, si en un futuro es necesario crear nuevos cines, solo extenderemos pero no será necesario modificar el código.

---

### 3) Principio Liskov Substitution:

Este principio es violado ya que no hay generalización de los cines. Es decir, se interactúa con ellos individualmente.
