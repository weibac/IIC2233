# --- EJEMPLO --- #
# [Plato1, Plato2, Plato2, Plato4]
# pasa a ser
# {"Categoria1": [Plato3, Plato2], "Categoria2": [Plato1, Plato4]}
def platos_por_categoria(lista_platos: list) -> dict:
    cat_platos_dict = {}
    for plato in lista_platos:
        cat_platos_dict[plato.categoria] = plato
    return cat_platos_dict



# Debe devolver los platos que no tengan ninguno de los ingredientes descartados
def descartar_platos(ingredientes_descartados: set, lista_platos: list) -> list:
    platos_filtrados = [plato for plato in lista_platos if set(plato.ingredientes) & ingredientes_descartados == set()]
    return platos_filtrados
    # & es interseccion y set() es ocnjunto vacio


# --- EXPLICACION --- #
# Si el plato necesita un ingrediente que no tiene cantidad suficiente,
# entonces retorna False
#
# En caso que tenga todo lo necesario, resta uno a cada cantidad y retorna True
# NO MODIFICAR
def preparar_plato(plato, ingredientes: dict) -> bool:
    for ingrediente_plato in plato.ingredientes:
        if ingredientes[ingrediente_plato] <= 0:
            return False

    for ingrediente_plato in plato.ingredientes:
        ingredientes[ingrediente_plato] -= 1

    return True


# --- EXPLICACION --- #
# Debe retornar un diccionario que agregue toda la información ...
#  de la lista de platos.
# precio total, tiempo total, cantidad de platos, platos
def resumen_orden(lista_platos: list) -> dict:
    precio_total = 0
    tiempo_total = 0
    cantidad_platos = 0
    nombres_platos = []
    for plato in lista_platos:
        precio_total += plato.precio
        tiempo_total += plato.tiempo
        cantidad_platos += 1
        nombres_platos.append(plato.nombre)
    
    orden_dict = {
        'precio total': precio_total,
        'tiempo total': tiempo_total,
        'cantidad platos': cantidad_platos,
        'platos': nombres_platos
    }

    return orden_dict

