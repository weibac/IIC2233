# Tarea 3: DCCard-Jitsu 🐧🥋



**Dejar claro lo que NO pudieron implementar y lo que no funciona a la perfección. Esto puede sonar innecesario pero permite que el ayudante se enfoque en lo que sí podría subir su puntaje.**

## Consideraciones generales :octocat:

La parte networking funciona bien. Hay servidor y cliente, y se hablan entre sí encriptado, con el protocolo pedido, y sin caerse. Implementé la desconeción repentina tanto por parte de cliente como de servidor y el bonus chat.

Lo único que falta es el juego en sí. No hay cartas. Estando en la ventana de juego, solo se puede chatear con el rival.
Si tu rival se desconecta antes que tú, ganas. Supongo que el juego se trata de convencer por chat al otro de desconectarse primero.

### Cosas implementadas y no implementadas :white_check_mark: :x:

Explicación: mantén el emoji correspondiente, de manera honesta, para cada item. Si quieres, también puedes agregarlos a los títulos:
- ❌ si **NO** completaste lo pedido
- ✅ si completaste **correctamente** lo pedido
- 🟠 si el item está **incompleto** o tiene algunos errores
#### Networking: 26 pts (19%)
##### ✅ Protocolo	
##### ✅ Correcto uso de sockets		
##### ✅ Conexión	
##### ✅ Manejo de Clientes	
##### ✅ Desconexión Repentina
#### Arquitectura Cliente - Servidor: 31 pts (23%)			
##### ✅ Roles			
##### ✅ Consistencia		
##### 🟠 Logs: no están implementados los logs de las funcionalidades no implementadas
#### Manejo de Bytes: 27 pts (20%)
##### ✅ Codificación			
##### ✅ Decodificación			
##### ✅ Encriptación		
##### ✅ Desencriptación	
##### ❌✅🟠 Integración: no sé qué es esto, sorry. Si es volver a usar lo enviado en el programa entonces ✅.
#### Interfaz Gráfica: 27 pts (20%)	
##### ✅ Ventana inicio		
##### ✅ Sala de Espera			
##### 🟠 Ventana de juego: está ahí, pero no permite jugar. Solo chat.						
##### ✅ Ventana final
#### Reglas de DCCard-Jitsu: 17 pts (13%)
##### 🟠 Inicio del juego: muestra la ventana cuando se cumplen condiciones	
##### ❌ Ronda				
##### 🟠 Termino del juego: solo para desconexión repentina
#### Archivos: 8 pts (6%)
##### ✅ Parámetros (JSON)		
##### 🟠 Cartas.py:	no se usa
##### ✅ Cripto.py
#### Bonus: 8 décimas máximo
##### ❌ Cheatcodes	
##### ❌ Bienestar	
##### ✅ Chat

## Ejecución :computer:
Los módulos principales de la tarea a ejecutar son dos: ```servidor/main.py``` y ```cliente/main.py```


Además se debe crear los siguientes archivos y directorios adicionales:
1. ```sprites/``` en ```cliente/front```, junto a su contenido (subdirectorios e imágenes correspondientes a los sprites utilizados en el juego).



## Librerías :books:
### Librerías externas utilizadas
La lista de librerías externas que utilicé fue la siguiente:

1. ```PyQt5``` para la interfaz gráfica del cliente
1. ```threading``` para las threads del cliente y el servidor encargadas de escuchar mensajes constantemente o (en caso del servidor) de aceptar nuevas conexiones
1. ```socket``` para poder enviar mensajes mediante networking entre cliente y servidor
1. ```json``` por dos motivos:
    - para importar los parámetros de ```parametros.json```
    - para pasar los diccionarios enviados entre cliente y servidor a representación ```json``` antes de codificarlos, encriptarlos, y enviarlos. También para hacer el proceso inverso al recibirlos del otro lado.
1. ```os```: ```path``` para unir rutas de archivo OS-agnostic con ```join``` y ```dirname``` para obtener el nombre de archivo de ```aux_json.py``` en el proceso ```join``` que se ejecuta ahí dentro. (el de los parámetros.)
1. ```collections```: ```deque``` para poder hacerle ```popleft``` a las listas a, b y c de bytes en ```cripto.py```.
1. ```time```: ```sleep``` para poder esperar un rato antes de cerrar el programa tras la desconexión repentina en ```dccardjitsu.py```.
1. ```sys```: ```exit``` en los ```main.py``` para salir del programa.
1. ```random```: ```randint``` en ```cartas.py```

### Librerías propias
Por otro lado, los módulos que fueron creados fueron los siguientes:

#### cliente/

1. ```aux_json.py```: Contiene las funciones que se encargan de pasar a y sacar de formato ```json``` los mensajes y también de encriptarlos y desencriptarlos, y la que carga los parámetros desde ```parametros.json```como un diccionario.
1. ```cripto.py```: Contiene las funciones que encriptan y desencriptan los bytearrays a enviar.
1. ```dccardjitsu.py```: Contiene la clase ```DccCardjitsu```, clase que instancia al frontend y al backend del cliente y conecta sus señales.

##### back/

1. ```cliente.py```: Contiene la clase ```Cliente```, encargada de comunicarse con el servidor. Implementa los protocolos de codificación definidos en el enunciado. Importa desde ```aux_json.py``` las funciones que se encargan de pasar a y sacar de formato ```json``` los mensajes y también de encriptarlos y desencriptarlos.
1. ```logica_ventanas.py```: Su principal funcionalida está en el método ```ejecutar_respuesta_servidor```. Éste es llamado cuando llega la respuesta del servidor, y según el comando contenido en ella emite la señal correspondiente a la ventana.

##### front/

1. ```ventana_inicio.py```: Se encarga de mostrar y de manejar las señales de la ventana de inicio.
1. ```ventana_espera.py```: Se encarga de mostrar y de manejar las señales de la ventana de espera.
1. ```ventana_juego.py```: Se encarga de mostrar y de manejar las señales de la ventana de juego.
1. ```ventana_chat.py```: Se encarga de mostrar y de manejar las señales de la ventana de chat.
1. ```ventana_final.py```: Se encarga de mostrar y de manejar las señales de la ventana final.

#### servidor/

1. ```aux_json.py```: Es la misma librería que la del mismo nombre del cliente.
1. ```cripto.py```: Es la misma librería que la del mismo nombre del cliente.
1. ```cartas.py```: No la usé, pero por lo que veo tiene un método que retorna un diccionario con información de las cartas del juego.
1. ```logica_juego.py```: Contiene la clase ```LogicaJuego```, encargada de cumplir todas las funciones del servidor que tengan que ver con el juego. No implementé el juego en sí, pero sí hace cosas como verificar los nombres de los usuarios. El método clave es ```ejecutar_comando```, que elabora la respuesta que entrega el servidor a cada request de un cliente.
1. ```servidor.py```: Contiene la clase ```Servidor```, encargada de comunicarse con el cliente mediante networking.  Importa desde ```aux_json.py``` las funciones que se encargan de pasar a y sacar de formato ```json``` los mensajes y también de encriptarlos y desencriptarlos. Puede tanto responder a requests de un cliente (toda request tiene una respuesta (mensaje que va de vuelta al cliente), aunque el cliente no haga nada con ella), y también mandar mensajes a un cliente por "iniciativa propia". Podría usarse para mandar mensajes a un cliente arbitrariamente, pero en esta implementación esto ocurre solo tras una desconexión repentina o paralelamente a una respuesta a una request. Por ejemplo, para enviarle información al otro jugador (no el que envió la request).


## Supuestos y consideraciones adicionales :thinking:
Los supuestos que realicé durante la tarea son los siguientes:

1. <Descripción/consideración 1 y justificación del por qué es válido/a> 
2. <Descripción/consideración 2 y justificación del por qué es válido/a>
3. ...

PD: <una última consideración (de ser necesaria) o comentario hecho anteriormente que se quiera **recalcar**>
- Usé un puerto (47105) distinto al que deben haber usado la mayoría de las tareas (el de la AF3) para que se pueda correr al mismo tiempo que otras tareas (aunque por supuesto no lo he probado y no estoy seguro de qué serviría. Supongo que solo quise ser original.).
- Cada vez que veas una variable de nombre ```p```, esta es un diccionario con los parámetros importados del JSON.
- Debido al uso de encriptación para toda la comunicación entre cliente y servidor, la desconexión repentina no produce un ```ConnectionError```, sino un ```IndexError``` originado en ```cripto.py```. Por eso el manejo de la desconexion repentina está implementado a partir de ```IndexError```.

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

1. https://stackoverflow.com/questions/2753254/how-to-open-a-file-in-the-parent-directory-in-python-in-appengine para abrir parametros.json desde el parent directory en el archivo ```aux_json.py```.



## Descuentos
La guía de descuentos se encuentra [link](https://github.com/IIC2233/Syllabus/blob/master/Tareas/Descuentos.md).
