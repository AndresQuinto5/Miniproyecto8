
# Traveling Salesman Problem using Genetic Algorithm

En la siguiente implementación, las ciudades se toman como genes, la cadena generada usando estos caracteres se denomina cromosoma, mientras que una puntuación de aptitud que es igual a la longitud de ruta de todas las ciudades mencionadas, se usa para apuntar a una población.
Fitness Score se define como la longitud del camino descrito por el gen. Cuanto menor sea el ajuste de la longitud del camino es el gen. 

El más apto de todos los genes del acervo genético sobrevive a la prueba de población y pasa a la siguiente iteración. El número de iteraciones depende del valor de una variable de enfriamiento. El valor de la variable de enfriamiento continúa disminuyendo con cada iteración y alcanza un umbral después de un cierto número de iteraciones.

## References
1. https://www.geeksforgeeks.org/traveling-salesman-problem-tsp-implementation/
2. https://www.geeksforgeeks.org/genetic-algorithms/
## Done with


```bash
Python 3.7.0
```

## Algorithm: 

```python
1. Initialize the population randomly.
2. Determine the fitness of the chromosome.
3. Until done repeat:
    1. Select parents.
    2. Perform crossover and mutation.
    3. Calculate the fitness of the new population.
    4. Append it to the gene pool.
```

## How the mutation works?
Supongamos que hay 5 ciudades: 0, 1, 2, 3, 4. El vendedor está en la ciudad 0 y tiene que encontrar la ruta más corta para viajar a través de todas las ciudades de regreso a la ciudad 0. Un cromosoma que representa la ruta elegida puede ser representado como: 

Imagen 1 xD

Este cromosoma sufre una mutación. Durante la mutación, la posición de dos ciudades en el cromosoma se intercambia para formar una nueva configuración, excepto la primera y la última celda, ya que representan el punto inicial y final.

Imagen 2 xD

El cromosoma original tenía una longitud de ruta igual a INT_MAX, según la entrada definida a continuación, ya que la ruta entre la ciudad 1 y la ciudad 4 no existía. Después de la mutación, el nuevo niño formado tiene una longitud de camino igual a 21, que es una respuesta mucho más optimizada que la suposición original. Así es como el algoritmo genético optimiza las soluciones a problemas difíciles.

## License
[MIT](https://choosealicense.com/licenses/mit/)

## Authors:
```
1. Andres Q
2. Mirka Nicolle M
3. Oscar de Leon
```