import json
from datetime import datetime
from collections import Counter, defaultdict
from typing import List, Tuple

def q1_memory(ruta_json: str) -> List[Tuple[datetime.date, str]]:
    conteo_fechas = Counter()
    usuarios_por_fecha = defaultdict(Counter)
#recorro cada linea del json ya que cada linea es un tweet y luego le extraigo su fecha e incremento en 1 su cantidad de apariciones
#por cada fecha tengo la lista de usuarios que hicieron tweets en ese día y cuantas veces lo hicieron
    with open(ruta_json, 'r', encoding='utf-8') as archivo_entrada:
        for linea in archivo_entrada:
            tweet = json.loads(linea)
            fecha = datetime.strptime(tweet['date'][:10], '%Y-%m-%d').date() 
            usuario = tweet['user']['username']
            conteo_fechas[fecha] += 1
            usuarios_por_fecha[fecha][usuario] += 1
#utilizo modulo collections para sacar del array las 10 fechas con mas tweets y sus respectivos usuarios
    top_fechas = conteo_fechas.most_common(10)

    resultado = []
    for fecha, _ in top_fechas:
        top_usuario = usuarios_por_fecha[fecha].most_common(1)[0][0]
        resultado.append((fecha, top_usuario))

    return resultado