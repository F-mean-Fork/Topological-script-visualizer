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
G.add_node('B9')
G.add_node('B10')
G.add_node('B11')
G.add_node('C12')
G.add_node('C13')
G.add_node('C14')
G.add_node('C15')
G.add_node('C16')
G.add_node('B17')
G.add_node('B18')
G.add_node('A19')
G.add_node('A20')
G.add_node('A21')
G.add_node('S22')
G.add_node('S23')
G.add_node('S24')
G.add_node('A25')
G.add_node('A26')
G.add_node('B27')
G.add_node('B28')
G.add_node('B29')
G.add_node('C30')
G.add_node('C31')
G.add_node('C32')
G.add_node('C33')
G.add_node('C34')
G.add_node('B35')
G.add_node('B36')
G.add_node('A37')
G.add_node('A38')
G.add_node('A39')
G.add_node('S40')
G.add_node('S41')
G.add_node('S42')
G.add_node('A43')
G.add_node('A44')
G.add_node('B45')
G.add_node('B46')
G.add_node('B47')
G.add_node('C48')
G.add_node('C49')
G.add_node('C50')
G.add_node('C51')
G.add_node('C52')
G.add_node('B53')
G.add_node('B54')
G.add_node('L55')
G.add_node('A56')
G.add_node('A57')
G.add_node('S58')
G.add_node('S59')
G.add_node('S60')
G.add_node('A61')
G.add_node('A62')
G.add_node('B63')
G.add_node('B64')
G.add_node('B65')
G.add_node('C66')
G.add_node('C67')
G.add_node('C68')
G.add_node('C69')
G.add_node('C70')
G.add_node('B71')
G.add_node('B72')
G.add_node('A73')
G.add_node('A74')
G.add_node('A75')
G.add_node('S76')
G.add_node('S77')
G.add_node('S78')
G.add_node('A79')
G.add_node('A80')
G.add_node('B81')
G.add_node('B82')
G.add_node('B83')
G.add_node('C84')
G.add_node('C85')
G.add_node('C86')
G.add_node('C87')
G.add_node('C88')
G.add_node('B89')
G.add_node('B90')
G.add_node('A91')
G.add_node('A92')
G.add_node('A93')
G.add_node('S94')
G.add_node('S95')
G.add_node('S96')
G.add_node('A97')
G.add_node('A98')
G.add_node('B99')
G.add_node('B100')
G.add_node('B101')
G.add_node('C102')
G.add_node('C103')
G.add_node('C104')
G.add_node('C105')
G.add_node('C106')
G.add_node('B107')
G.add_node('E108')

# Добавление связей
G.add_edge('X1', 'A2')
G.add_edge('A2', 'A3')
G.add_edge('A3', 'S4')
G.add_edge('S4', 'S5')
G.add_edge('S5', 'S6')
G.add_edge('A3', 'A7')
G.add_edge('A7', 'A8')
G.add_edge('A8', 'B9')
G.add_edge('B9', 'B10')
G.add_edge('B10', 'B11')
G.add_edge('B11', 'C12')
G.add_edge('C12', 'C13')
G.add_edge('C13', 'C14')
G.add_edge('C14', 'C15')
G.add_edge('C15', 'C16')
G.add_edge('B11', 'B17')
G.add_edge('B17', 'B18')
G.add_edge('B18', 'A19')
G.add_edge('A19', 'A20')
G.add_edge('A20', 'A21')
G.add_edge('A21', 'S22')
G.add_edge('S22', 'S23')
G.add_edge('S23', 'S24')
G.add_edge('A21', 'A25')
G.add_edge('A25', 'A26')
G.add_edge('A26', 'B27')
G.add_edge('B27', 'B28')
G.add_edge('B28', 'B29')
G.add_edge('B29', 'C30')
G.add_edge('C30', 'C31')
G.add_edge('C31', 'C32')
G.add_edge('C32', 'C33')
G.add_edge('C33', 'C34')
G.add_edge('B29', 'B35')
G.add_edge('B35', 'B36')
G.add_edge('B36', 'A37')
G.add_edge('A37', 'A38')
G.add_edge('A38', 'A39')
G.add_edge('A39', 'S40')
G.add_edge('S40', 'S41')
G.add_edge('S41', 'S42')
G.add_edge('A39', 'A43')
G.add_edge('A43', 'A44')
G.add_edge('A44', 'B45')
G.add_edge('B45', 'B46')
G.add_edge('B46', 'B47')
G.add_edge('B47', 'C48')
G.add_edge('C48', 'C49')
G.add_edge('C49', 'C50')
G.add_edge('C50', 'C51')
G.add_edge('C51', 'C52')
G.add_edge('B47', 'B53')
G.add_edge('B53', 'B54')
G.add_edge('B54', 'L55')
G.add_edge('L55', 'A56')
G.add_edge('A56', 'A57')
G.add_edge('A57', 'S58')
G.add_edge('S58', 'S59')
G.add_edge('S59', 'S60')
G.add_edge('A57', 'A61')
G.add_edge('A61', 'A62')
G.add_edge('A62', 'B63')
G.add_edge('B63', 'B64')
G.add_edge('B64', 'B65')
G.add_edge('B65', 'C66')
G.add_edge('C66', 'C67')
G.add_edge('C67', 'C68')
G.add_edge('C68', 'C69')
G.add_edge('C69', 'C70')
G.add_edge('B65', 'B71')
G.add_edge('B71', 'B72')
G.add_edge('B72', 'A73')
G.add_edge('A73', 'A74')
G.add_edge('A74', 'A75')
G.add_edge('A75', 'S76')
G.add_edge('S76', 'S77')
G.add_edge('S77', 'S78')
G.add_edge('A75', 'A79')
G.add_edge('A79', 'A80')
G.add_edge('A80', 'B81')
G.add_edge('B81', 'B82')
G.add_edge('B82', 'B83')
G.add_edge('B83', 'C84')
G.add_edge('C84', 'C85')
G.add_edge('C85', 'C86')
G.add_edge('C86', 'C87')
G.add_edge('C87', 'C88')
G.add_edge('B83', 'B89')
G.add_edge('B89', 'B90')
G.add_edge('B90', 'A91')
G.add_edge('A91', 'A92')
G.add_edge('A92', 'A93')
G.add_edge('A93', 'S94')
G.add_edge('S94', 'S95')
G.add_edge('S95', 'S96')
G.add_edge('A93', 'A97')
G.add_edge('A97', 'A98')
G.add_edge('A98', 'B99')
G.add_edge('B99', 'B100')
G.add_edge('B100', 'B101')
G.add_edge('B101', 'C102')
G.add_edge('C102', 'C103')
G.add_edge('C103', 'C104')
G.add_edge('C104', 'C105')
G.add_edge('C105', 'C106')
G.add_edge('B101', 'B107')
G.add_edge('B107', 'E108')


# Определение цветов для узлов
color_map = []
for node in G.nodes():
    if node == 'X1':
        color_map.append('red')
    elif node.startswith('A'):
        color_map.append('steelblue')
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
node_size = 30

# Задание позиций узлов
pos = {
'X1' : (0, 4),
'A2' : (0, 7),
'A3' : (0, 10),
'S4' : (-0.08, 10),
'S5' : (-0.16, 10),
'S6' : (-0.24, 10),
'A7' : (0, 13),
'A8' : (0, 16),
'B9' : (0, 19),
'B10' : (0, 22),
'B11' : (0, 25),
'C12' : (0.08, 25),
'C13' : (0.16, 25),
'C14' : (0.24, 25),
'C15' : (0.32, 25),
'C16' : (0.4, 25),
'B17' : (0, 28),
'B18' : (0, 31),
'A19' : (0, 34),
'A20' : (0, 37),
'A21' : (0, 40),
'S22' : (-0.08, 40),
'S23' : (-0.16, 40),
'S24' : (-0.24, 40),
'A25' : (0, 43),
'A26' : (0, 46),
'B27' : (0, 49),
'B28' : (0, 52),
'B29' : (0, 55),
'C30' : (0.08, 55),
'C31' : (0.16, 55),
'C32' : (0.24, 55),
'C33' : (0.32, 55),
'C34' : (0.4, 55),
'B35' : (0, 58),
'B36' : (0, 61),
'A37' : (0, 64),
'A38' : (0, 67),
'A39' : (0, 70),
'S40' : (-0.08, 70),
'S41' : (-0.16, 70),
'S42' : (-0.24, 70),
'A43' : (0, 73),
'A44' : (0, 76),
'B45' : (0, 79),
'B46' : (0, 82),
'B47' : (0, 85),
'C48' : (0.08, 85),
'C49' : (0.16, 85),
'C50' : (0.24, 85),
'C51' : (0.32, 85),
'C52' : (0.4, 85),
'B53' : (0, 88),
'B54' : (0, 91),
'L55' : (0, 94),
'A56' : (0, 97),
'A57' : (0, 100),
'S58' : (-0.08, 100),
'S59' : (-0.16, 100),
'S60' : (-0.24, 100),
'A61' : (0, 103),
'A62' : (0, 106),
'B63' : (0, 109),
'B64' : (0, 112),
'B65' : (0, 115),
'C66' : (0.08, 115),
'C67' : (0.16, 115),
'C68' : (0.24, 115),
'C69' : (0.32, 115),
'C70' : (0.4, 115),
'B71' : (0, 118),
'B72' : (0, 121),
'A73' : (0, 124),
'A74' : (0, 127),
'A75' : (0, 130),
'S76' : (-0.08, 130),
'S77' : (-0.16, 130),
'S78' : (-0.24, 130),
'A79' : (0, 133),
'A80' : (0, 136),
'B81' : (0, 139),
'B82' : (0, 142),
'B83' : (0, 145),
'C84' : (0.08, 145),
'C85' : (0.16, 145),
'C86' : (0.24, 145),
'C87' : (0.32, 145),
'C88' : (0.4, 145),
'B89' : (0, 148),
'B90' : (0, 151),
'A91' : (0, 154),
'A92' : (0, 157),
'A93' : (0, 160),
'S94' : (-0.08, 160),
'S95' : (-0.16, 160),
'S96' : (-0.24, 160),
'A97' : (0, 163),
'A98' : (0, 166),
'B99' : (0, 169),
'B100' : (0, 172),
'B101' : (0, 175),
'C102' : (0.08, 175),
'C103' : (0.16, 175),
'C104' : (0.24, 175),
'C105' : (0.32, 175),
'C106' : (0.4, 175),
'B107' : (0, 178),
'E108' : (0, 181),

}

# Визуализация графа
nx.draw(G, pos, with_labels=False, node_color=color_map,
        node_size=node_size, linewidths=1, edgecolors='black',
        width=1)

plt.xlim(-3, 3)
plt.ylim(1, 190)
plt.savefig("alter_model_v2.png", dpi=300, bbox_inches='tight', format="png")