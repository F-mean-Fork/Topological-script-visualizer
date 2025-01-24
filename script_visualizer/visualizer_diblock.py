import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

# Добавление узлов
G.add_node('X1')
G.add_node('A2')
G.add_node('A3')
G.add_node('S4')
G.add_node('S5')
G.add_node('S6')
G.add_node('A7')
G.add_node('A8')
G.add_node('A9')
G.add_node('A10')
G.add_node('A11')
G.add_node('S12')
G.add_node('S13')
G.add_node('S14')
G.add_node('A15')
G.add_node('A16')
G.add_node('A17')
G.add_node('A18')
G.add_node('A19')
G.add_node('S20')
G.add_node('S21')
G.add_node('S22')
G.add_node('A23')
G.add_node('A24')
G.add_node('L25')
G.add_node('B26')
G.add_node('B27')
G.add_node('C28')
G.add_node('C29')
G.add_node('C30')
G.add_node('C31')
G.add_node('C32')
G.add_node('B33')
G.add_node('B34')
G.add_node('B35')
G.add_node('B36')
G.add_node('B37')
G.add_node('C38')
G.add_node('C39')
G.add_node('C40')
G.add_node('C41')
G.add_node('C42')
G.add_node('B43')
G.add_node('B44')
G.add_node('B45')
G.add_node('B46')
G.add_node('B47')
G.add_node('C48')
G.add_node('C49')
G.add_node('C50')
G.add_node('C51')
G.add_node('C52')
G.add_node('B53')
G.add_node('E54')


# Добавление связей
G.add_edge('X1', 'A2')
G.add_edge('A2', 'A3')
G.add_edge('A3', 'S4')
G.add_edge('S4', 'S5')
G.add_edge('S5', 'S6')
G.add_edge('A3', 'A7')
G.add_edge('A7', 'A8')
G.add_edge('A8', 'A9')
G.add_edge('A9', 'A10')
G.add_edge('A10', 'A11')
G.add_edge('A11', 'S12')
G.add_edge('S12', 'S13')
G.add_edge('S13', 'S14')
G.add_edge('A11', 'A15')
G.add_edge('A15', 'A16')
G.add_edge('A16', 'A17')
G.add_edge('A17', 'A18')
G.add_edge('A18', 'A19')
G.add_edge('A19', 'S20')
G.add_edge('S20', 'S21')
G.add_edge('S21', 'S22')
G.add_edge('A19', 'A23')
G.add_edge('A23', 'A24')
G.add_edge('A24', 'L25')
G.add_edge('L25', 'B26')
G.add_edge('B26', 'B27')
G.add_edge('B27', 'C28')
G.add_edge('C28', 'C29')
G.add_edge('C29', 'C30')
G.add_edge('C30', 'C31')
G.add_edge('C31', 'C32')
G.add_edge('B27', 'B33')
G.add_edge('B33', 'B34')
G.add_edge('B34', 'B35')
G.add_edge('B35', 'B36')
G.add_edge('B36', 'B37')
G.add_edge('B37', 'C38')
G.add_edge('C38', 'C39')
G.add_edge('C39', 'C40')
G.add_edge('C40', 'C41')
G.add_edge('C41', 'C42')
G.add_edge('B37', 'B43')
G.add_edge('B43', 'B44')
G.add_edge('B44', 'B45')
G.add_edge('B45', 'B46')
G.add_edge('B46', 'B47')
G.add_edge('B47', 'C48')
G.add_edge('C48', 'C49')
G.add_edge('C49', 'C50')
G.add_edge('C50', 'C51')
G.add_edge('C51', 'C52')
G.add_edge('B47', 'B53')
G.add_edge('B53', 'E54')


# Определение цветов для узлов
color_map = []
for node in G.nodes():
    if node == 'X1':
        color_map.append('red')
    elif node.startswith('A'):
        color_map.append('blue')
    elif node.startswith('B'):
        color_map.append('green')
    elif node.startswith('S'):
        color_map.append('orange')
    elif node.startswith('C'):
        color_map.append('violet')
    elif node.startswith('L'):
        color_map.append('black')
    else:
        color_map.append('yellow')

# Параметры узлов
node_size = 100
spacing = 0.5
side_spacing = spacing/4

# Задание позиций узлов
pos = {
'X1' :  (0, 1),
'A2' :  (0, 3),
'A3' :  (0, 5),
'S4' :  (4e-2, 5),
'S5' :  (8.5e-2, 5),
'S6' :  (13e-2, 5),
'A7' :  (0, 7),
'A8' :  (0, 9),

'A9' :  (0, 11),
'A10' : (0, 13),
'A11' : (0, 15),
'S12' : (-4.5e-2, 15),
'S13' : (-9e-2, 15),
'S14' : (-13.5e-2, 15),
'A15' : (0, 17),
'A16' : (0, 19),

'A17' : (0, 21),
'A18' : (0, 23),
'A19' : (0, 25),
'S20' : (4e-2, 25),
'S21' : (8.5e-2, 25),
'S22' :  (13e-2, 25),
'A23' :  (0, 27),
'A24' :  (0, 29),

'L25' : (0, 31),

'B26' : (0, 33),
'B27' : (0, 35),
'C28' : (-4.5e-2, 35),
'C29' : (-9e-2, 35),
'C30' : (-13.5e-2, 35),
'C31' : (-18e-2, 35),
'C32' : (-22.8e-2, 35),
'B33' : (0, 37),
'B34' : (0, 39),

'B35' : (0, 41),
'B36' : (0, 43),
'B37' : (0, 45),
'C38' : (4e-2, 45),
'C39' : (8.5e-2, 45),
'C40' :  (13e-2, 45),
'C41' :  (17.5e-2, 45),
'C42' :  (22e-2, 45),
'B43' : (0, 47),
'B44' : (0, 49),

'B45' : (0, 51),
'B46' : (0, 53),
'B47' : (0, 55),
'C48' : (-4.5e-2, 55),
'C49' : (-9e-2, 55),
'C50' : (-13.5e-2, 55),
'C51' : (-18e-2, 55),
'C52' : (-22.8e-2, 55),
'B53' : (0, 57),

'E54' : (0, 59),
}

# Визуализация графа
nx.draw(G, pos, with_labels=False, node_color=color_map,
        node_size=node_size, linewidths=1, edgecolors='black',
        width=1)

plt.xlim(-1, 1)
plt.savefig("diblock_model.png", dpi=300, bbox_inches='tight', format="png")