
### Listado de relaciones
- Herencia
    - Las 3 clases de programon elementales heredan de clase abstracta `Programon`.
    - `Bayas` y `Pociones` heredan de la clase abstracta `Objeto`.
    - `Caramelo` hereda de `Bayas` y `Pociones`.
- Agregación
    - `LigaProgramon` agrega a instancias de `Entrenador`.
    - Las instancias de `Entrenador` agregan a instancias de `Programon` y pueden agregar a instancias de `Objeto`.


### Otras características
- Clases Abstractas
    - Clase abstracta `Programon`
    - Clase abstracta `Objeto`
- Polimorfismo
    - El método `luchar()` es distinto para cada subclase programon elemental debido a que produce un distinto efecto al ganar un combate. Cada subclase hace overriding del método presente en la clase abstracta `Programon`.
    - El método `aplicar_objeto()` es distinto para cada subclase de `Objeto`. `Baya` y Pocion hacen overriding del método presente en `Objeto`, y `Caramelo` hereda ambos overrides.
- Properties
    - `experiencia` es una property que se resetea y hace subir nivel en 1 cuando llega a 100
    - `vida` es una property que nunca debe superar los 255
    - `ataque` es una property que nunca debe superar los 190
    - `defensa` es una property que nunca debe superar los 250
    - `velocidad` es una property que nunca debe superar los 200


### Diagrama de herencia
- `abc` (abstract base class)
    - `Programon`
        - `ProgramonAgua`
        - `ProgramonFuego`
        - `ProgramonTierra`
    - `Objeto`
        - `Baya`
        - `Caramelo`
        - `Pocion`
            - `Caramelo`