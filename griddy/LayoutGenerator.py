import json
from pprint import pprint
from collections import OrderedDict    
from random import randint
from functools import reduce

class LayoutGenerator:
    def __init__(self, args):
        self.layout = json.load(open(args.layout), object_pairs_hook=OrderedDict)
        self.html, self.css = "", "body{\n    width: 100vw;\n    height: 100vh;\n}\n\n"
        self.no_color = args.no_color
        self.walk(self.layout, 0)
    
    def getRandomColor(self):
        return 'rgb({}, {}, {})'.format(randint(0, 256), randint(0, 256), randint(0, 256))

    def parseKey(self, key):
        x = 'c' if 'c' in key else 'r'
        return tuple([key.split(x)[0], x])

    def generateCSS(self, key, className, isFlex):
        if key == "root":
            self.css += ".root\n{\n    width: 100%;\n    height: 100%;\n"
        else:
            percent, _ = self.parseKey(key)
            if 'c' in key:
                self.css += ".{}\n{{\n    width: {}%;\n    height: 100%;\n".format(className, percent)
            else:
                self.css += ".{}\n{{\n    width: 100%;\n    height: {}%;\n".format(className, percent)
        
        if isFlex:
            self.css += "    display: flex;\n"
        if not self.no_color:
            self.css += "    background-color: {};\n".format(self.getRandomColor())
        self.css += "}\n\n"

    def checkKey(self, key):
        return

    def checkLayer(self, node):
        node_type = []
        percents = []
        for key, item in node.items():
            if key == 'root':
                return
            p, x = self.parseKey(key)
            node_type.append(x)
            percents.append(p)
        total_percent = reduce(lambda x, y: int(x) + int(y), percents)
        all_same = all(x == node_type[0] for x in node_type)
        
    
    def isFlexNode(self, node):
        isFlex = False
        if not node is None:
            isFlex = 'c' in list(node)[0]
        return isFlex

    def walk(self, node, level):
        self.checkLayer(node)
        indent = "    " * (level + 1)
        for key, item in node.items():
            className = "root" if key == 'root' else 'level-{}-{}'.format(level, key)
            self.html += (indent + "<div class=\"{}\">\n".format(className))
            if not item is None:
                self.walk(item, level + 1)
            self.html += (indent + "</div>\n")
            self.generateCSS(key, className, self.isFlexNode(item))

    def write(self):
        with open('index.html', 'w') as file:
            file.write("<!DOCTYPE html>\n")
            file.write("<html>\n")
            file.write("<head>\n")
            file.write("    <link rel=\"stylesheet\" href=\"styles.css\">")
            file.write("</head>\n")
            file.write("<body>\n")
            file.write(self.html)
            file.write("</body>\n")
            file.write("</html>\n")
            
        with open('styles.css', 'w') as file:
            file.write(self.css)

    def print(self):
        print(self.html)
        print(self.css)