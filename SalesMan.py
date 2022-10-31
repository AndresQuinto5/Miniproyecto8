from random import randint


'''

Problema del viajante de comercio (TSP): dado un conjunto de ciudades y distancias entre cada par de ciudades, 
el problema es encontrar la ruta más corta posible que visite cada ciudad exactamente una vez y regrese al punto de partida.
Tenga en cuenta la diferencia entre el ciclo hamiltoniano y TSP.


El problema del ciclo hamiltoniano es encontrar si existe un recorrido que visite cada ciudad exactamente una vez. 
Aquí sabemos que existe el recorrido hamiltoniano (porque el gráfico está completo) y, de hecho, existen muchos recorridos de este tipo, 
el problema es encontrar un ciclo hamiltoniano de peso mínimo.

'''
INT_MAX = 2147483647
# Number of cities in TSP
V = 5

# Names of the cities
GENES = "ABCDE"

# Starting Node Value
START = 0

# Initial population size for the algorithm
POP_SIZE = 10

# Structure of a GNOME
# defines the path traversed
# by the salesman while the fitness value
# of the path is stored in an integer


class individual:
	def __init__(self) -> None:
		self.gnome = ""
		self.fitness = 0

	def __lt__(self, other):
		return self.fitness < other.fitness

	def __gt__(self, other):
		return self.fitness > other.fitness


# Function to return a random number
# from start and end
def rand_num(start, end):
	return randint(start, end-1)


# Function to check if the character
# has already occurred in the string
def repeat(s, ch):
	for i in range(len(s)):
		if s[i] == ch:
			return True

	return False


