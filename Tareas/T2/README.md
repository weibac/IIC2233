# Tarea 2: DCCruz vs Zombies :zombie::seedling::sunflower:


Un buen ```README.md``` puede marcar una gran diferencia en la facilidad con la que corregimos una tarea, y consecuentemente cómo funciona su programa, por lo en general, entre más ordenado y limpio sea éste, mejor será 

Para nuestra suerte, GitHub soporta el formato [MarkDown](https://es.wikipedia.org/wiki/Markdown), el cual permite utilizar una amplia variedad de estilos de texto, tanto para resaltar cosas importantes como para separar ideas o poner código de manera ordenada ([pueden ver casi todas las funcionalidades que incluye aquí](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet))

Un buen ```README.md``` no tiene por que ser muy extenso tampoco, hay que ser **concisos** (a menos que lo consideren necesario) pero **tampoco pueden** faltar cosas. Lo importante es que sea claro y limpio 

**Dejar claro lo que NO pudieron implementar y lo que no funciona a la perfección. Esto puede sonar innecesario pero permite que el ayudante se enfoque en lo que sí podría subir su puntaje.**

## Consideraciones generales :octocat:

- El frontend está ahí.
- Faltan la mayoría de las mecánicas del juego.
    - No se puede pasar de ronda
    - Ni plantas ni zombies mueren ni hacen daño
    - Las rondas solo pueden perderse
        - Perder no funciona muy bien

### Cosas implementadas y no implementadas :white_check_mark: :x:

Explicación: mantén el emoji correspondiente, de manera honesta, para cada item. Si quieres, también puedes agregarlos a los títulos:
- ❌ si **NO** completaste lo pedido
- ✅ si completaste **correctamente** lo pedido
- 🟠 si el item está **incompleto** o tiene algunos errores
#### Ventanas: 39 pts (40%)
##### ✅ Ventana de Inicio
##### ✅ Ventana de Ranking	
##### ✅ Ventana principal
##### 🟠 Ventana de juego
    algunos valores no se actualizan	
##### 🟠 Ventana post-ronda
    codigo incompleto y no aparece
#### Mecánicas de juego: 46 pts (47%)			
##### 🟠 Plantas
    se pueden poner
##### 🟠 Zombies
    no comen
##### 🟠 Escenarios		
##### 🟠 Fin de ronda	
    no aparece el sprite ni llama a ventana posronda
##### ❌ Fin de juego	
#### Interacción con el usuario: 22 pts (23%)
##### 🟠 Clicks	
     no se implementaron soles
##### 🟠 Animaciones
     solo de zombies y muy rapida
#### Cheatcodes: 8 pts (8%)
##### ✅ Pausa
##### ❌ S + U + N
##### ❌ K + I + L
#### Archivos: 4 pts (4%)
##### ✅ Sprites
##### ✅ Parametros.py
##### ❌ K + I + L
#### Bonus: 9 décimas máximo
##### ❌ Crazy Cruz Dinámico
##### ❌ Pala
##### ❌ Drag and Drop Tienda
##### ❌ Música juego

## Ejecución :computer:
El módulo principal de la tarea a ejecutar es  ```main.py```. Además se debe crear los siguientes archivos y directorios adicionales:
1. ```archivo.ext``` en ```ubicación```
2. ```directorio``` en ```ubicación```
3. ...


## Librerías :books:
### Librerías externas utilizadas
La lista de librerías externas que utilicé fue la siguiente:

1. ```time```: para esperar una vez que se pierde una ronda antes de cerrar ventana de juego
2. ```random```: para manejar los aspectos aleatorios de la creación de zombies
3. ```PyQt5```: para la interfaz gráfica y timers

### Librerías propias
Por otro lado, los módulos que fueron creados fueron los siguientes:

#### Backend
1. ```elementos_juego```: Contiene clases que modelan a zombies y plantas
2. ```logica_inicio```: Hecha para manejar la lógica del login (revisar nombre de usuario y manejar las señales correspondientes)
3. ```logica_juego```: Maneja la lógica del juego. Implementa pausar y despausar el juego, crear zombies con un timer, moverlos, y el sistema de comprar plantas. Envía señales a ```logica_juego``` para actualizar sprites cuando se necesite.

#### Frontend
1. ```ventana_inicio```: Dibuja ventana inicio, recibe input de nombre de usuario y lo manda a ```logica_inicio```
2. ```ventana_juego```: Dibuja la pantalla de juego. Recibe input de mouse para plantar plantas, y para pausar y despausar el juego. Actualiza los sprites de los zombies cuando se mueven.
3. ```ventana_posronda```: Está ahí pero nunca se ejecuta. Debería dibujar la ventana de posronda.
4. ```ventana_ranking```: Dibuja el ranking de los 5 mejores puntajes. Funciona al 100%.
5. ```ventana_seleccion_escenario```: Permite al usuario elegir el escenario donde quiere jugar. Una vez que lo hace, envía la señal para empezar el juego. Funciona al 100%.
6. ```ventana_test```: No se ejecuta. La tenía para hacer pruebas cuando empecé la tarea. Francamente se me quedó ahí.

#### Mainspace
1. ```dccruz_vs_zombies```: Contiene la la clase que representa al juego ```DCCruzVsZombies``` que hereda de ```QApplication```. Contiene como atributos a todas las clases dle frontend y del backend. Es llamada por ```main``` para iniciar el programa y conecta todas las señales entre sí.
2. ```parametros```: Contiene las constantes utilizadas en el programa. Esto incluye rutas de archivos como ui files y sprites.



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

Para realizar mi tarea saqué código de:
1. \<link de código>: este hace \<lo que hace> y está implementado en el archivo <nombre.py> en las líneas <número de líneas> y hace <explicación breve de que hace>



## Descuentos
La guía de descuentos se encuentra [link](https://github.com/IIC2233/Syllabus/blob/master/Tareas/Descuentos.md).
