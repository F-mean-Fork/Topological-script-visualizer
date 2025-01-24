from .bonds_parser import bonds_parser
from .check_script import check_script
from .constructor import MolGraph
from .types_parser import types_parser


class Mol(MolGraph):
    def __init__(self, script: str) -> None:
        if check_script(script) != "No errors":
            raise ValueError(f"{script}: is not correct")
        
        self.types = types_parser(script)
        self.bonds = bonds_parser(script)
        
        with open("script_names.txt", "w") as file:
            for i, type_item in enumerate(self.types): 
                file.write(f"G.add_node('{type_item}{i+1}')\n")

        with open("script_bonds.txt", "w") as file:
            for i, type_item in enumerate(self.types):
                if i > 0:
                    if self.types[i - 1] != type_item:
                        file.write(f"G.add_edge('{self.types[i - 1]}{i}', '{type_item}{i + 1}')\n")
                    else:
                        file.write(f"G.add_edge('{type_item}{i}', '{type_item}{i + 1}')\n")
                        
        with open("script_pos.txt", "w") as file:
            last_letter = None
            second_number = 1
            for i, type_item in enumerate(self.types):   
                if type_item not in ['C', 'S']:
                    first_number = 0
                    second_number += 3
                else:
                    if type_item == 'S':
                        if last_letter != type_item:
                            first_number = -0.08
                        else:
                            first_number -= 0.08
                        second_number = second_number
                    elif type_item == 'C':
                        if last_letter != type_item:
                            first_number = 0.08
                        else:
                            first_number += 0.08
                        second_number = second_number
                
                last_letter = type_item
                file.write(f"'{type_item}{i + 1}' : ({first_number}, {second_number}),\n")                
        super().__init__(self.bonds)