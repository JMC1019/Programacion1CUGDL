from graphviz import Digraph

dot = Digraph()

dot.node('A', 'Raíz')
dot.node('B', 'Izquierda')
dot.node('C', 'Derecha')

dot.edges(['AB', 'AC'])
dot.render('arbol_simple', view=True)