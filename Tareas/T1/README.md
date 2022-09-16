# Tarea 1: DCCampeonato 🏃‍♂️🏆


**Dejar claro lo que NO pudieron implementar y lo que no funciona a la perfección. Esto puede sonar innecesario pero permite que el ayudante se enfoque en lo que sí podría subir su puntaje.**

## Consideraciones generales :octocat:

<Descripción de lo que hace y que **_no_** hace la tarea que entregaron junto
con detalles de último minuto y consideraciones como por ejemplo cambiar algo
en cierta línea del código o comentar una función>

### Consideraciones de formato:
- Uso las comillas simples `'` como comillas principales y las dobles `"` como secundarias
- Uso los nombres de variable `a`, `b`, `c`, ... para los iteradores de los `for in range()`


### Cosas implementadas y no implementadas :white_check_mark: :x:

Explicación: mantén el emoji correspondiente, de manera honesta, para cada item. Si quieres, también puedes agregarlos a los títulos:
- ❌ si **NO** completaste lo pedido
- ✅ si completaste **correctamente** lo pedido
- 🟠 si el item está **incompleto** o tiene algunos errores
#### Programación Orientada a Objetos (18pts) (22%%)
##### ✅ Diagrama
##### ✅ Definición de clases, atributos, métodos y properties		
##### ✅ Relaciones entre clases
#### Preparación programa: 11 pts (7%)			
##### ✅ Creación de partidas
#### Entidades: 28 pts (19%)
##### ✅ Programón
##### ✅ Entrenador		
##### 🟠 Liga: no se reinicia al terminar una partida
##### ✅ Objetos		
#### Interacción Usuario-Programa 57 pts (38%)
##### ✅ General	
##### ✅ Menú de Inicio
##### ✅ Menú Entrenador
##### ✅ Menu Entrenamiento
##### 🟠 Simulación ronda campeonato: no verifica si el jugador ha ganado
##### ✅ Ver estado del campeonato
##### ✅ Menú crear objeto
##### ✅ Menú utilizar objeto
##### ✅ Ver estado del entrenador
##### ✅ Robustez
#### Manejo de archivos: 12 pts (8%)
##### ✅ Archivos CSV
##### ✅ Parámetros
#### Bonus: 5 décimas
##### ✅ Mega Evolución (pero no la probé)
##### ✅ CSV dinámico

## Ejecución :computer:
El módulo principal de la tarea a ejecutar es  ```main.py```. Contiene funciones que manejan el flujo de cada menú.


## Librerías :books:
### Librerías externas utilizadas
La lista de librerías externas que utilicé fue la siguiente:

#### archivos.py
1. ```os```: ```path.join()```
2. ```typing```: ```List, Dict```
#### entrenadores.py
1. ```random```: ```random, choice```
2. ```typing```: ```List```
3. ```beautifultable```: ```BeautifulTable``` (debe instalarse)
#### liga.py
1. ```random```: ```randint, shuffle```
#### main.py
1. ```collections```: ```namedtuple```
2. ```sys```: ```exit```
#### menus.py
1. ```typing```: ```List```
#### objetos.py
1. ```random```: ```randint```
2. ```abc```: ```ABC, abstractmethod```
#### programones.py
1. ```random```: ```randint, choice```
2. ```abc```: ```ABC, abstractmethod```

### Librerías propias
Por otro lado, los módulos que fueron creados fueron los siguientes:

1. ```librería_1```: Contiene a ```ClaseA```, ```ClaseB```, (ser general, tampoco es necesario especificar cada una)...
2. ```librería_2```: Hecha para <insertar descripción **breve** de lo que hace o qué contiene>

1. ```parametros.py```: Contiene las constantes usadas por otros módulos
2. ```archivos.py```: Contiene a la función ```cargar_archivo()```, que abre un archivo y carga sus datos en una representación ```Dict[str, Dict[str, str or list]]```. Implementa lectura dinámica de CSV.
3. ```menus.py```: Contiene a la clase ```Menu```, hecha para generar la string a imprimir para cada menú multilínea de selección múltiple numérica con el que interactúe el usuario y entregar robustez al input del usuario al seleccionar una opción en ellos.
4. ```liga.py```: Contiene a la clase ```LigaProgramon```
5. ```entrenadores.py```: Contiene a la clase ```Entrenador```
6. ```programones.py```: Contiene a la clase abstracta ```Programon``` y sus subclases ```ProgramonFuego```, ```ProgramonPlanta``` y ```ProgramonAgua```, que hacen overriding al método abstracto ```accion_victoria()```. Heredan también muchas properties.
7. ```objetos.py```: Contiene a la clase abstracta ```Objeto``` y sus subclases ```Baya```, ```Pocion``` y ```Caramelo```. Esta última implementa la multiherencia desde ```Baya``` y ```Pocion```.



PD: Quedaron repartidos por ahí varios ```# TODO```. Marcan cosas que me habría gustado implementar o arreglar, pero que no tuve el tiempo de hacer.


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

Para realizar mi tarea saqué código de:

ninguna parte



## Descuentos
La guía de descuentos se encuentra [link](https://github.com/IIC2233/Syllabus/blob/master/Tareas/Descuentos.md).
