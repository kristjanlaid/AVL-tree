from tkinter import *
from tkinter import messagebox
from projekt import *
from text_recognitionV3 import *
from random import *
###############################
#   Global variables for GUI
###############################
x_gap_per_layer = [300, 150, 75, 45, 20, 10, 5]
y_gap_per_layer = 100
starting_coordinates = [700, 20]
added_nodes_stack = []

myTree = AVLTree()
root_node = None

###############################
#   Function definitions
###############################
def get_from_stack():
    if len(added_nodes_stack) == 0:
       return False, 0

    return True, added_nodes_stack.pop()


def draw_text(canvas, x, y, text):
    font_size = 12
    if len(text) == 4:
        font_size = 8
    elif len(text) >= 5:
        font_size = 7

    inserted_text = canvas.create_text(x,y, font="Times " + str(font_size) + " bold", text=text)
    canvas.tag_raise(inserted_text)
    canvas.pack(fill=BOTH)


def draw_circle(canvas, x, y, text):
    canvas.create_oval(x - 15, y - 15, x + 15, y + 15, outline="black",
                       fill="lightblue", width=2)
    draw_text(canvas, x, y, text)
    canvas.pack(fill=BOTH)


def draw_line(canvas, x_start, y_start, x_end, y_end):
    line = canvas.create_line(x_start, y_start,x_end, y_end, width=2)
    canvas.tag_lower(line)
    canvas.pack(fill=BOTH)


def canvas_clear_all(canvas):
    global root_node
    global added_nodes_stack
    root_node = None
    canvas.delete('all')
    added_nodes_stack = []


def get_existing_numbers_in_range(added_nodes_stack, min_value, max_value):
    list_of_values = []
    for index in range(len(added_nodes_stack)):
        value = added_nodes_stack[index]
        if value >= min_value and value <= max_value:
            list_of_values.append(value)
    return list_of_values
def get_random_number_in_a_list(list_):
    random_index = randint(0,len(list_)-1)
    return list_[random_index]

def read_instruction(canvas):
    global added_nodes_stack
    sentence = number_input.get()
    #sentence = 'Add 5 nodes superior to 5 and inferior to 10'
    print(sentence)
    #sentence = number_input.get()
#def read_instruction(sentence):
    list_of_instructions = get_list_of_instructions(sentence)
    print_list_of_instructions(list_of_instructions)
    #I put the instruction about the root at the begining
    for index_instruction in range(len(list_of_instructions)):
        instruction = list_of_instructions[index_instruction]
        print(type(instruction))
        if instruction.action == 'start':
            list_of_instructions.insert(0,list_of_instructions.pop(index_instruction))

    #Now I read the instructions
    for index_instruction in range(len(list_of_instructions)):
        print(added_nodes_stack)
        instruction = list_of_instructions[index_instruction]
        action_type = instruction.action
        if instruction.number_of_times:
            number_of_times = instruction.number_of_times
        else:
            number_of_times = 1
        print("Number_of_times:",number_of_times)
        list_of_specifications = []
        for specification in instruction.list_of_specifications:
            list_of_specifications.append(specification.specification_type)
        #key_word = instruction.key_word.name
        list_of_nodes = instruction.list_of_nodes

        if action_type == 'start':
            added_nodes_stack = []#reinitialize the stack
            number = list_of_nodes[0]
            insert_new_node(canvas,number)
                    
        elif action_type == 'create':   
            min_value = 0
            max_value = 999#Max value
            if [] == list_of_specifications:#The default case
                if len(list_of_nodes)>1:#There are nodes in list_of_nodes
                    for number in list_of_nodes:
                        insert_new_node(canvas,number)
                elif len(list_of_nodes)==1:#There is only on node in list_of_nodes
                    number = list_of_nodes[0]
                    for k in range(number_of_times):
                        insert_new_node(canvas,number)
                else:#list_of_nodes is emply, I choose a random value
                    for k in range(number_of_times):
                        number = randint(min_value,max_value)
                        insert_new_node(canvas,number)
            #Upper
            elif ['upper'] == list_of_specifications:
                min_value = list_of_nodes[0]
                for k in range(number_of_times):
                    number = randint(min_value,max_value)
                    insert_new_node(canvas,number)
            #Lower
            elif ['lower'] == list_of_specifications:
                max_value = list_of_nodes[0]
                for k in range(number_of_times):
                    number = randint(min_value,max_value)
                    insert_new_node(canvas,number)
            #Uppest
            elif ['uppest'] == list_of_specifications:
                max_value = max(added_nodes_stack)
                for k in range(number_of_times):
                    number = randint(min_value,max_value)
                    insert_new_node(canvas,number)
            #Lowest
            elif ['lowest'] == list_of_specifications:
                min_value = min(added_nodes_stack)   
                for k in range(number_of_times):
                    number = randint(min_value,max_value)
                    insert_new_node(canvas,number)
            #Range
            elif (['range'] == list_of_specifications):
                min_value = list_of_nodes[0]
                max_value = list_of_nodes[1]
                for k in range(number_of_times):
                    number = randint(min_value,max_value)
                    insert_new_node(canvas,number)
            elif 'lower' in list_of_specifications and 'upper' in list_of_specifications:
                for index_specification in range(len(list_of_specifications)):
                    specification = list_of_specifications[index_specification]
                    if specification == 'lower':
                        index_max_value = index_specification
                    elif specification == 'upper':
                        index_min_value = index_specification
                min_value = list_of_nodes[index_min_value]
                max_value = list_of_nodes[index_max_value]
                for k in range(number_of_times):
                    number = randint(min_value,max_value)
                    insert_new_node(canvas,number)
            #Max upper
            elif 'upper' in list_of_specifications and 'uppest' in list_of_specifications:#above the uppest value
                min_value = max(added_nodes_stack)
                for k in range(number_of_times):
                    number = randint(min_value,max_value)
                    insert_new_node(canvas,number)
            #Min upper
            elif 'upper' in list_of_specifications and 'lowest' in list_of_specifications:#above the lowest value
                min_value = min(added_nodes_stack)
                for k in range(number_of_times):
                    number = randint(min_value,max_value)
                    insert_new_node(canvas,number)
            #Max lower
            elif 'lower' in list_of_specifications and 'uppest' in list_of_specifications:#below the uppest value
                max_value = max(added_nodes_stack)
                for k in range(number_of_times):
                    number = randint(min_value,max_value)
                    insert_new_node(canvas,number)
            #Min lower
            elif 'lower' in list_of_specifications and 'lowest' in list_of_specifications:#below the lowest value
                max_value = min(added_nodes_stack)
                for k in range(number_of_times):
                    number = randint(min_value,max_value)
                    insert_new_node(canvas,number) 

        elif action_type == 'delete':
            min_value = 0
            max_value = 999#Max value
            list_of_numbers = get_existing_numbers_in_range(added_nodes_stack,min_value,max_value)
            if [] == list_of_specifications:
                if len(list_of_nodes) > 1:#There are nodes in list_of_nodes
                    for number in list_of_nodes:
                        delete_node(canvas, number, True)
                elif len(list_of_nodes) == 1:#There is only on node in list_of_nodes
                    number = list_of_nodes[0]
                    for k in range(number_of_times):
                        delete_node(canvas, number, True)
                else:#list_of_nodes is emply, I choose a random value to delete
                    for k in range(number_of_times):
                        number = get_random_number_in_a_list(list_of_numbers)
                        delete_node(canvas, number, True)
            #Upper
            elif ['upper'] == list_of_specifications:
                min_value = list_of_nodes[0]
                if instruction.key_word and instruction.key_word.name == 'nodes' and instruction.number_of_times==1:#Delete all the nodes superior
                    for number in list_of_numbers:
                        delete_node(canvas, number, True)
                else:
                    for k in range(number_of_times):
                        number = get_random_number_in_a_list(list_of_numbers)
                        delete_node(canvas, number, True)
            #Lower  
            elif ['lower'] == list_of_specifications:
                max_value = list_of_nodes[0]
                if instruction.key_word and instruction.key_word.name == 'nodes' and instruction.number_of_times==1:#Delete all the nodes inferior: Delete all nodes inferior to 10.
                    for number in list_of_numbers:
                        delete_node(canvas, number, True)
                else:
                    for k in range(number_of_times):
                        number = get_random_number_in_a_list(list_of_numbers)
                        delete_node(canvas, number, True)
            #Uppest   
            elif ['uppest'] == list_of_specifications:
                for k in range(number_of_times):
                    number = max(added_nodes_stack)
                    delete_node(canvas, number, True)
            #Lowest     
            elif ['lowest'] == list_of_specifications:
                for k in range(number_of_times):
                    number = min(added_nodes_stack)
                    delete_node(canvas, number, True)
            #Range
            elif (['range'] == list_of_specifications):
                min_value = list_of_nodes[0]
                max_value = list_of_nodes[1]

                if instruction.key_word and instruction.key_word.name == 'nodes' and instruction.number_of_times==1:
                    for number in list_of_numbers:
                        delete_node(canvas, number, True)
                else:
                    for k in range(number_of_times):
                        number = get_random_number_in_a_list(list_of_numbers)
                        delete_node(canvas, number, True)
            elif 'lower' in list_of_specifications and 'upper' in list_of_specifications:
                for index_specification in range(len(list_of_specifications)):
                    specification = list_of_specifications[index_specification]
                    if specification == 'lower':
                        index_max_value = index_specification
                    elif specification == 'upper':
                        index_min_value = index_specification
                min_value = list_of_nodes[index_min_value]
                max_value = list_of_nodes[index_max_value]
                if instruction.key_word and instruction.key_word.name == 'nodes' and instruction.number_of_times==1:
                    for number in list_of_numbers:
                        delete_node(canvas, number, True)
                else:
                    for k in range(number_of_times):
                        number = get_random_number_in_a_list(list_of_numbers)
                        delete_node(canvas, number, True)
            #Min upper
            elif 'upper' in list_of_specifications and 'lowest' in list_of_specifications:#above the lowest value
                min_value = min(added_nodes_stack)
                if instruction.key_word and instruction.key_word.name == 'nodes' and instruction.number_of_times==1:
                    for number in list_of_numbers:
                        delete_node(canvas, number, True)
                else:
                    for k in range(number_of_times):
                        number = get_random_number_in_a_list(list_of_numbers)
                        delete_node(canvas, number, True)
            #Max lower
            elif 'lower' in list_of_specifications and 'uppest' in list_of_specifications:#below the uppest value
                max_value = max(added_nodes_stack)
                if instruction.key_word and instruction.key_word.name == 'nodes' and instruction.number_of_times==1:
                    for number in list_of_numbers:
                        delete_node(canvas, number, True)
                else:
                    for k in range(number_of_times):
                        number = get_random_number_in_a_list(list_of_numbers)
                        delete_node(canvas, number, True)
                
def insert_new_node(canvas,i):
    global root_node
    global added_nodes_stack

    added_nodes_stack.append(i)
    root_node = myTree.insert(root_node, i) # Adds the number to AVL-tree
    canvas.delete('all') # Clear canvas to start drawing again
    draw_tree_recursion(canvas, root_node, starting_coordinates[0], starting_coordinates[1], 0)  # Start drawing
    number_textbox.delete(0, 'end')


def find_node():
    global root_node
    i = int(number_input.get())
    if myTree.search(root_node, i):
       messagebox.showinfo("Find {}".format(i), "Yes!")
    else:
       messagebox.showinfo("Find {}".format(i), "No!")
    number_textbox.delete(0, 'end')


def delete_node(canvas, i, delete_from_stack):
    global added_nodes_stack
    global root_node

    # Cannot delete anything
    if (len(added_nodes_stack) == 0) or (i not in added_nodes_stack and delete_from_stack):
        return

    # If undo button is used, the element is already deleted from the stack
    if delete_from_stack:
        added_nodes_stack.remove(i)

    root_node = myTree.delete(root_node, i)  # Adds the number to AVL-tree
    canvas.delete('all')  # Clear canvas to start drawing again
    draw_tree_recursion(canvas, root_node, starting_coordinates[0], starting_coordinates[1], 0)  # Start drawing
    number_textbox.delete(0, 'end')
    return


def undo_change(canvas):
    tuple = get_from_stack()
    if tuple[0]:
        delete_node(canvas, tuple[1], False)


def draw_tree_recursion(canvas, node, start_x, start_y, layer_nr):
    # draw circle
    draw_circle(canvas, start_x, start_y, str(node.value))

    # draw left child and line
    if node.left != None:
         draw_line(canvas, start_x, start_y, start_x-x_gap_per_layer[min(layer_nr, len(x_gap_per_layer)-1)], start_y+y_gap_per_layer)
         draw_tree_recursion(canvas, node.left, start_x-x_gap_per_layer[min(layer_nr, len(x_gap_per_layer)-1)], start_y+y_gap_per_layer, layer_nr+1)

    # draw right child and line
    if node.right != None:
         draw_line(canvas, start_x, start_y, start_x+x_gap_per_layer[min(layer_nr, len(x_gap_per_layer)-1)], start_y+y_gap_per_layer)
         draw_tree_recursion(canvas, node.right, start_x+x_gap_per_layer[min(layer_nr, len(x_gap_per_layer)-1)], start_y+y_gap_per_layer, layer_nr+1)


################################
#      MAIN to run GUI
################################

# Constants
window_height = 900
window_width = 1400

# Initsialization
root = Tk()
root.geometry(str(window_width) + "x" + str(window_height) + "+300+300")
root.title("AVL-tree visualization")
root.resizable(False, False)

top_frame = Frame(root)
top_frame.pack(side=TOP)
canvas = Canvas(root, width=window_width, height=window_height)

# User inputs
number_input = StringVar(top_frame)
number_textbox = Entry(top_frame, width=100, textvariable=number_input)
number_textbox.pack(side=LEFT, pady=4, padx=4)

read_button = Button(top_frame, text="Read", command= lambda: read_instruction(canvas))
read_button.pack(side=LEFT, padx=4)

insert_button = Button(top_frame, text="Insert", command= lambda: insert_new_node(canvas))
insert_button.pack(side=LEFT, padx=4)

find_button = Button(top_frame, text="Find", command= lambda: find_node())
find_button.pack(side=LEFT, padx=4)

del_button = Button(top_frame, text="Delete", command= lambda: delete_node(canvas, int(number_input.get()), True))
del_button.pack(side=LEFT, padx=4)

undo_button = Button(top_frame, text="Undo", command= lambda: undo_change(canvas))
undo_button.pack(side=LEFT, padx=4)

clear_button = Button(top_frame, text="Clear", command= lambda: canvas_clear_all(canvas))
clear_button.pack(side=LEFT, padx=4)

# Run GUI
root.mainloop()
