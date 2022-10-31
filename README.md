
# Traveling Salesman Problem using Genetic Algorithm

En la siguiente implementación, las ciudades se toman como genes, la cadena generada usando estos caracteres se denomina cromosoma, mientras que una puntuación de aptitud que es igual a la longitud de ruta de todas las ciudades mencionadas, se usa para apuntar a una población.
Fitness Score se define como la longitud del camino descrito por el gen. Cuanto menor sea el ajuste de la longitud del camino es el gen. 

El más apto de todos los genes del acervo genético sobrevive a la prueba de población y pasa a la siguiente iteración. El número de iteraciones depende del valor de una variable de enfriamiento. El valor de la variable de enfriamiento continúa disminuyendo con cada iteración y alcanza un umbral después de un cierto número de iteraciones.

