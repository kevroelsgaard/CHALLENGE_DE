import json
import re
from collections import Counter
from typing import List, Tuple

# expresion regular para usuarios, matchea los strings que comiencen en arroba y sean seguidos por alfanumericos
patron_menciones = re.compile(r'@(\w+)')

def contar_menciones(file_path: str) -> Counter:
    menciones = Counter()
    with open(file_path, 'r', encoding='utf-8') as archivo:
        for linea in archivo:
            tweet = json.loads(linea)
            # extrae todas las menciones en el tweet
            usuarios_mencionados = patron_menciones.findall(tweet['content'])
            menciones.update(usuarios_mencionados)
    return menciones

def q3_time(file_path: str) -> List[Tuple[str, int]]:
    menciones = contar_menciones(file_path)
    # return de los top 10 usuarios mas mencionados
    return menciones.most_common(10)