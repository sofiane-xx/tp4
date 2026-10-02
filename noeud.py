import matplotlib.pyplot as plt

class Noeud : 
    def __init__(self, node_value, child_nodes = None):
        if not child_nodes : 
            child_nodes=[] 
        
        for node in child_nodes:
            if not isinstance(node, Noeud): 
                raise TypeError("the second param should be of type Noed !!")

        self.child_nodes = child_nodes
        self.node_value = node_value

    def add_child_node(self, new_child):
        self.child_nodes.append(new_child)

    def display_expression(self): 
        expression = str(self.node_value)
        for child in self.child_nodes: 
            expression += " " +child.display_expression()

        return(expression)

    def evaluer(self, valeurs):
        # 1. Constant
        if isinstance(self.node_value, (int, float)):
            return float(self.node_value)

        # 2. Variable (leaf that is a string)
        if len(self.child_nodes) == 0:
            if self.node_value not in valeurs:
                raise ValueError(f"No value given for variable '{self.node_value}'")
            return float(valeurs[self.node_value])

        # 3. Operator: evaluate the children first
        args = [child.evaluer(valeurs) for child in self.child_nodes]

        # Binary operators
        if self.node_value == "*":
            return args[0] * args[1]
        if self.node_value == "+":
            return args[0] + args[1]
        if self.node_value == "-":
            return args[0] - args[1]
        if self.node_value == "/":
            if args[1] == 0:
                raise ValueError("Division by zero")
            return args[0] / args[1]

        # Unary operators (optional part)
        unaires = {"exp": math.exp, "log": math.log, "sin": math.sin, "cos": math.cos}
        if self.node_value in unaires:
            return unaires[self.node_value](args[0])

        raise ValueError(f"Unknown operator '{self.node_value}'")

    def tracer(self, variable, valeurs_x):
        valeurs_y = []
        for x in valeurs_x:
            valeurs_y.append(self.evaluer({variable: x}))
        plt.plot(valeurs_x, valeurs_y)
        plt.xlabel(variable)
        plt.ylabel("f(" + variable + ")")
        plt.title(self.display_expression())
        plt.show()

