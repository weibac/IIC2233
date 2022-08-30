# Tarea 0: Star Advanced 🚀🌌


Un buen ```README.md``` puede marcar una gran diferencia en la facilidad con la que corregimos una tarea, y consecuentemente cómo funciona su programa, por lo en general, entre más ordenado y limpio sea éste, mejor será 

Para nuestra suerte, GitHub soporta el formato [MarkDown](https://es.wikipedia.org/wiki/Markdown), el cual permite utilizar una amplia variedad de estilos de texto, tanto para resaltar cosas importantes como para separar ideas o poner código de manera ordenada ([pueden ver casi todas las funcionalidades que incluye aquí](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet))

Un buen ```README.md``` no tiene por que ser muy extenso tampoco, hay que ser **concisos** (a menos que lo consideren necesario) pero **tampoco pueden** faltar cosas. Lo importante es que sea claro y limpio 

**Dejar claro lo que NO pudieron implementar y lo que no funciona a la perfección. Esto puede sonar innecesario pero permite que el ayudante se enfoque en lo que sí podría subir su puntaje.**

## Consideraciones generales :octocat:

<Descripción de lo que hace y que **_no_** hace la tarea que entregaron junto
con detalles de último minuto y consideraciones como por ejemplo cambiar algo
en cierta línea del código o comentar una función>

### Cosas implementadas y no implementadas :white_check_mark: :x:

Explicación: mantén el emoji correspondiente, de manera honesta, para cada item. Si quieres, también puedes agregarlos a los títulos:
- ❌ si **NO** completaste lo pedido
- ✅ si completaste **correctamente** lo pedido
- 🟠 si el item está **incompleto** o tiene algunos errores
#### Programación Orientada a Objetos (18pts) (22%%)
##### ✅ Menú de Inicio
##### ✅ Funcionalidades		
##### ✅ Puntajes
#### Flujo del Juego (30pts) (36%) 
##### ✅ Menú de Juego
##### ✅ Tablero		
##### ✅ Bestias	
##### ✅ Guardado de partida		
#### Término del Juego (14pts) (17%)
##### ✅🟠 Fin del juego	(no estoy 100% seguro de si funciona bien)
##### ✅ Puntajes	
#### Genera: (15 pts) (15%)
##### ✅ Menús
##### ✅ Parámetros
##### ✅ PEP-8
#### Bonus: 3 décimas
##### ✅ 
## Ejecución :computer:
El módulo principal de la tarea a ejecutar es  ```main.py```. Además se debe crear los siguientes archivos y directorios adicionales:
1. ```archivo.ext``` en ```ubicación```
2. ```directorio``` en ```ubicación```
3. ...


## Librerías :books:
### Librerías externas utilizadas
La lista de librerías externas (ordenadas según el archivo en el cual se importan) que utilicé fue la siguiente:

#### archivos.py
1. ```os```: ```path.join()``` para hacer rutas relativas compatibles con distintos sistemas operativos
2. ```os```: ```listdir()``` para obtener los archivos guardados en la carpeta partidas

#### archivos.py
1. ```math```: ```ceil()``` función techo usada al calcular la cantidad de bestias a poner
2. ```random```: ```randint()``` usada para obtener ubicaciones aleatorias para las bestias
3. ```string```: ```ascii_uppercase``` lista de ordenada letras usada para el procesamiento input de coordenadas por parte de usuario

#### main.py
1. ```sys```: ```exit``` para terminar la ejecución del programa cuando el usuario pide salir


### Librerías propias
Por otro lado, los módulos que fueron creados fueron los siguientes:

1. ```archivos.py```: Contiene funciones para leer y escribir información de la carpeta partidas y el archivo puntajes.txt
2. ```juego.py```: Contiene la clase Partida, que almacena los datos de cada partida y tiene métodos para crear el tablero, descurir casillas, y calcular el puntaje final.
3. ```menus.py```: Asiste en la interacción con el usuario. Almacena o crea strings multilinea que se muestran en cada menu, y contiene una función que revisa si el input entregado por el usuario es válido.



## Supuestos y consideraciones adicionales :thinking:
Los supuestos que realicé durante la tarea son los siguientes:

1. <Descripción/consideración 1 y justificación del por qué es válido/a> 
2. <Descripción/consideración 2 y justificación del por qué es válido/a>
3. ...

PD: <una última consideración (de ser necesaria) o comentario hecho anteriormente que se quiera **recalcar**>


-------



**EXTRA:** si van a explicar qué hace específicamente un método, no lo coloquen en el README mismo. Pueden hacerlo directamente comentando el método en su archivo. Por ejemplo:

```python
class Corrector:

    def __init__(self):
          pass

    # Este método coloca un 6 en las tareas que recibe
    def corregir(self, tarea):
        tarea.nota  = 6
        return tarea
```

Si quieren ser más formales, pueden usar alguna convención de documentación. Google tiene la suya, Python tiene otra y hay muchas más. La de Python es la [PEP287, conocida como reST](https://www.python.org/dev/peps/pep-0287/). Lo más básico es documentar así:

```python
def funcion(argumento):
    """
    Mi función hace X con el argumento
    """
    return argumento_modificado
```
Lo importante es que expliquen qué hace la función y que si saben que alguna parte puede quedar complicada de entender o tienen alguna función mágica usen los comentarios/documentación para que el ayudante entienda sus intenciones.

## Referencias de código externo :book:

Para realizar mi tarea me orienté con los siguientes materiales:
1. [AskPython: Create Minesweeper using Python from the Basic to Advanced](https://www.askpython.com/python/examples/create-minesweeper-using-python): Leí el principio de este tutorial para ayudarme a programar la creación del tablero. Me sirvió la idea, pero no copié código directamente.


## Descuentos
La guía de descuentos se encuentra [link](https://github.com/IIC2233/Syllabus/blob/master/Tareas/Descuentos.md).
