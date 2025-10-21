from graphviz import Digraph

dot = Digraph()

dot.node('A', '8')
dot.node('B', '3')
dot.node('C', '10')
dot.node('D', '1')
dot.node('E', '6')

dot.edges(['AB', 'AC', 'BD', 'BE'])
dot.render('arbol_simple', view=True)