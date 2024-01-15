import re
import copy
class Instruction:
    def __init__(self, Action, number_of_times, KeyWord, list_of_specifications, list_of_nodes):
        self._action = Action
        self._number_of_times = number_of_times
        self._key_word = KeyWord
        self._list_of_specifications = list_of_specifications
        self._list_of_nodes = list_of_nodes

    @property
    def action(self):
        return self._action

    @action.setter
    def action(self, value):
        self._action = value

    @property
    def number_of_times(self):
        return self._number_of_times

    @number_of_times.setter
    def number_of_times(self, value):
        self._number_of_times = value

    @property
    def key_word(self):
        return self._key_word

    @key_word.setter
    def key_word(self, value):
        self._key_word = value

    @property
    def list_of_specifications(self):
        return self._list_of_specifications

    @list_of_specifications.setter
    def list_of_specifications(self, value):
        self._list_of_specifications = value

    @property
    def list_of_nodes(self):
        return self._list_of_nodes

    @list_of_nodes.setter
    def list_of_nodes(self, value):
        self._list_of_nodes = value

    def print(self):
        action = self._action
        print(f"New Instruction created  \n"
                f"Action: {action}, \n"
                f"Number of Times: {self._number_of_times}, ")
        if self._key_word:
            print(f"Key Word: {self._key_word},")
        else:
            print(f"Key Word: None,")
        if self._list_of_specifications:
            for specification in self._list_of_specifications:
                print(f"List of Specifications: {specification.specification_type},")
            print(f"List of Nodes: {self._list_of_nodes}\n")
        else:
            print(f"List of Specifications: {self._list_of_specifications}, \n"
                f"List of Nodes: {self._list_of_nodes}\n")



class KeyWord:
    def __init__(self, name, is_used):
        self._name = name
        self._is_used = is_used

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def is_used(self):
        return self._is_used

    @is_used.setter
    def is_used(self, value):
        self._is_used = value


keyword_instance = KeyWord('Example', False)

class Action:
    def __init__(self, name, is_used, action_type):
        self._name = name
        self._is_used = is_used
        self._action_type = action_type

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def is_used(self):
        return self._is_used

    @is_used.setter
    def is_used(self, value):
        self._is_used = value

    @property
    def action_type(self):
        return self._action_type

    @action_type.setter
    def action_type(self, value):
        self._action_type = value

class Specification:
    def __init__(self, name, is_used, specification_type):
        self._name = name
        self._is_used = is_used
        self._specification_type = specification_type


    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def is_used(self):
        return self._is_used

    @is_used.setter
    def is_used(self, value):
        self._is_used = value

    @property
    def specification_type(self):
        return self._specification_type

    @specification_type.setter
    def specification_type(self, value):
        self._specification_type = value


class Number:
    def __init__(self, number, is_used):
        self._number = number
        self._is_used = is_used

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, value):
        self._number = value

    @property
    def is_used(self):
        return self._is_used

    @is_used.setter
    def is_used(self, value):
        self._is_used = value

class And:
    def __init__(self, name, is_used):
        self._name = name
        self._is_used = is_used

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._number = value

    @property
    def is_used(self):
        return self._is_used

    @is_used.setter
    def is_used(self, value):
        self._is_used = value
        
#KeyWord
list_of_key_words = ['nodes','node','root']

def is_key_word(word):
    for key_word in list_of_key_words:
        if word == key_word:
            return word
#Action
list_of_action_type_create = ['create','add','draw']
list_of_action_type_delete = ['remove','delete','supr']
list_of_action_type_start = ['start']
list_of_action_types = [list_of_action_type_create,list_of_action_type_delete,list_of_action_type_start]

list_of_action_types_cases = ['create','delete','start']

def is_action_type(word):
    for index_list_of_action_type in range(len(list_of_action_types)):
        list_of_action_type = list_of_action_types[index_list_of_action_type]
        for index_action_type in range(len(list_of_action_type)):
            word_action_type = list_of_action_type[index_action_type]
            if word == word_action_type:#we have found the word
                list_of_action_types_cases[index_list_of_action_type]
                return list_of_action_types_cases[index_list_of_action_type]
            
#Specification
list_of_specification_upper = ['upper','bigger','larger','above','superior']
list_of_specification_lower = ['lower','smaller','below','inferior']

list_of_specification_uppest = ['uppest','biggest','largest']
list_of_specification_lowest = ['lowest','smallest']

list_of_specification_range = ['range','between']

list_of_specifications = [list_of_specification_upper,list_of_specification_lower,
                          list_of_specification_uppest,list_of_specification_lowest,
                          list_of_specification_range]
list_of_specifications_cases = ['upper','lower','uppest','lowest','range']

list_of_all_words = []
for list_of_specification in list_of_specifications:
    for word in list_of_specification:
        list_of_all_words.append(word)
for list_of_action_type in list_of_action_types:
    for word in list_of_action_type:
        list_of_all_words.append(word)

def is_specification(word):
    for index_list_of_specification in range(len(list_of_specifications)):
        list_of_specification = list_of_specifications[index_list_of_specification]
        for index_specification in range(len(list_of_specification)):
            word_specification = list_of_specification[index_specification]
            if word == word_specification:#we have found the word
                #print(list_of_specifications_cases[index_list_of_specification])
                return list_of_specifications_cases[index_list_of_specification]

def is_and(word):
    return word == 'and'
def get_human_list_of_translated_sentence(list_of_translated_sentence):
    human_list_of_translated_sentence = []
    for element in list_of_translated_sentence:
        if type(element) == KeyWord:
            human_list_of_translated_sentence.append('KeyWord')
        elif type(element) == Number:
            human_list_of_translated_sentence.append('Number')
        elif type(element) == Action:
            human_list_of_translated_sentence.append('Action')
        elif type(element) == Specification:
            human_list_of_translated_sentence.append('Specification')
    return human_list_of_translated_sentence

sentence = 'Delete the 5 lowest nodes and add 2 nodes.'
#sentence = 'Draw a tree with 4 nodes: 12 14 81 23 with a root of 5'
#sentence = 'Draw a tree with 5 nodes in range 0 to 10'
#sentence = 'Add 5 nodes superior to 5 and inferior to 10'
#sentence = 'Delete the 5 lowest nodes'
#sentence = 'Add 1 node.'
##sentence = 'Add a node.'
#sentence = 'Add the node 36'
#sentence = 'add a node with a value of 42'
#sentence = 'Add 2 nodes above the lowest node'
#sentence = 'create a tree with a root of 3'
#sentence = 'Add 42'
#sentence = 'Create a tree with a root of 5. Add 12.'
#sentence = 'Delete 2 nodes'
#sentence = 'Delete a node inferior to 36'
#sentence = 'Add 2 nodes above 10'
#sentence = 'Delete the lowest value'
#sentence = 'Add a root of 42 and 5 nodes'
#sentence = 'Add a root of 42 and add 5 nodes'
#sentence = 'Add 5 nodes inferior to 6 and superior to 2'
#sentence = 'Add 5 nodes inferior to 6 and 2 nodes superior to 2'
#sentence = 'Add 2 nodes between 0 and 10.'
#sentence = 'Add 1 node superior to 5 and 2 lower than the uppest value'
#sentence = 'Add 1 node superior to 2 and 3 nodes inferior to 4.'
#sentence = 'Add 1 node superior to 2 and 3 inferior to 4.'
#sentence = 'Add the node 10.'
#sentence = 'Delete 10'
def get_list_of_translated_sentence(sentence):
    sentence = re.findall(r'\b\w+\b|[.,;!?]', sentence)
    list_of_translated_sentence = []
    index_last_key_word = 0
    index_new_key_word = None
    for index_word in range(len(sentence)):
        word = sentence[index_word].lower()
        try:
            number = int(word)
            list_of_translated_sentence.append(Number(number,False))

        except:
            specification_type = is_specification(word)
            action_type = is_action_type(word)
            key_word = is_key_word(word)
            and_type = is_and(word)
            if specification_type:#The word is a specification
                list_of_translated_sentence.append(Specification(word, False, specification_type))

            elif action_type:#The word is an action type
                list_of_translated_sentence.append(Action(word, False, action_type))
            elif key_word:
                if index_last_key_word == 0:#Initialisation
                    last_key_word = KeyWord(word, False)
                    new_key_word = last_key_word
                    index_last_key_word = len(list_of_translated_sentence)
                else:
                    new_key_word = KeyWord(word, False)
                list_of_translated_sentence.append(new_key_word)
            elif and_type:
                new_and_type = And('and', False)
                list_of_translated_sentence.append(new_and_type)
    return list_of_translated_sentence


def get_list_of_partitionized_translated_sentence(list_of_translated_sentence):
    list_of_partitionized_translated_sentence = []
    previous_element = list_of_translated_sentence[0]
    partitionized_translated_sentence = [previous_element]
    old_element = None
    test_key_word = False
    old_action = previous_element
    old_specification = Specification(None,None,None)
    buffer_range = 0
    for index_element in range(1,len(list_of_translated_sentence)):
        new_element = list_of_translated_sentence[index_element]
        if (not test_key_word and (type(old_element) == Number and (type(new_element) == Action or type(new_element) == Specification)) or (type(new_element) == Number and index_element == len(list_of_translated_sentence)-1)) and not test_key_word:
            test_key_word = True
            partitionized_translated_sentence.insert(len(partitionized_translated_sentence),KeyWord('nodes',False))
        #if ((type(old_element) == Number and not test_key_word) and (type(new_element) == Action or type(new_element) == Number) or index_element == len(list_of_translated_sentence)-1):#Correct this sentence:Add 1 node superior to 2 and 3 inferior to 4.
        #    test_key_word = True
        #    partitionized_translated_sentence.insert(len(partitionized_translated_sentence),KeyWord('nodes',False))
        if (type(new_element) == Action):
            test_key_word = False
            buffer_range = 0
            old_action = new_element
            if len(partitionized_translated_sentence)>1:
                list_of_partitionized_translated_sentence.append(partitionized_translated_sentence)
            partitionized_translated_sentence = [new_element]
        elif (type(new_element) == KeyWord):#new_element.name == 'root')
            test_key_word = True
            if (new_element.name == 'root'):
                buffer_range = 0
                if len(partitionized_translated_sentence)>1:
                    list_of_partitionized_translated_sentence.append(partitionized_translated_sentence)
                partitionized_translated_sentence = [new_element]
            else:
                partitionized_translated_sentence.append(new_element)
        elif (type(old_element) == And and type(new_element) == Number and not (buffer_range==1 and old_specification.specification_type == 'range')):#And 34
            test_key_word = False
            list_of_partitionized_translated_sentence.append(partitionized_translated_sentence)
            partitionized_translated_sentence = [old_action, new_element]

        else:
            if (type(new_element) == Specification):
                old_specification = new_element
                
            elif (type(new_element) == Number and old_specification.specification_type == 'range'):
                buffer_range += 1#2 number needed for a range

            partitionized_translated_sentence.append(new_element)
        old_element = new_element
    list_of_partitionized_translated_sentence.append(partitionized_translated_sentence)
    return list_of_partitionized_translated_sentence



def get_list_of_instructions(sentence):#Simple with the following pattern: Action Number KeyWord Number
    list_of_translated_sentence = get_list_of_translated_sentence(sentence)
    list_of_partitionized_translated_sentence = get_list_of_partitionized_translated_sentence(list_of_translated_sentence)
    list_of_instructions = []

    for list_of_translated_sentence in list_of_partitionized_translated_sentence:
        instruction = Instruction(None, None, None, [], [])
        for element in list_of_translated_sentence:
            if type(element) == Action:
                if instruction.key_word == None and instruction.number_of_times!=None:#Action Number. (Add 42.)
                    list_of_nodes.append(number_of_times)
                    number_of_times = 1
                instruction  = Instruction(element.action_type, None, None, [], [])
                list_of_instructions.append(instruction)
            elif (type(element) == KeyWord and element.name == 'root'):
                action = Action('start',False,'start')
                instruction  = Instruction(action.action_type, None, element.name, [], [])
                list_of_instructions.append(instruction)
            elif type(element) == Specification:
                instruction.list_of_specifications.append(element)
                
            elif type(element) == Number:
                if  instruction.key_word == None:#Before the key word
                    instruction.number_of_times = element.number
                else:
                    instruction.list_of_nodes.append(element.number)
                    
            elif type(element) == KeyWord:
                instruction.key_word = element.name
    return list_of_instructions

    
def print_list_of_partitionized_translated_sentence(list_of_partitionized_translated_sentence):
    print('\n')
    for list_of_translated_sentence in list_of_partitionized_translated_sentence:
        print(get_human_list_of_translated_sentence(list_of_translated_sentence))
        print('-'*50)
def print_list_of_instructions(list_of_instructions):
    for instruction in list_of_instructions:
        instruction.print()
        print('-'*50)

#list_of_translated_sentence = get_list_of_instructions(sentence)
print(sentence,'\n')
#list_of_instructions = get_list_of_instructions(sentence)
#print_list_of_instructions(list_of_instructions)
list_of_translated_sentence = get_list_of_translated_sentence(sentence)
print(get_human_list_of_translated_sentence(list_of_translated_sentence))
list_of_partitionized_translated_sentence = get_list_of_partitionized_translated_sentence(list_of_translated_sentence)
print_list_of_partitionized_translated_sentence(list_of_partitionized_translated_sentence)
#print(get_human_list_of_translated_sentence(list_of_translated_sentence))

list_of_instructions = get_list_of_instructions(sentence)
print_list_of_instructions(list_of_instructions)
