from CONST import *
from informations import *
from math import log2

def calculate_entropy(dictionary : dict) :
    _entropy = 0.0
    for param, paramValue in dictionary.items():
        child_entropy = 0.0
        tmp = dict()
        len_param = len(dictionary[param])
        for instance, instanceValue in paramValue.items():
            result = instanceValue['satisfaction']
            if not result in tmp:
                tmp.update({result : list()})
                tmp[result].append(instance)
            else:
                tmp[result].append(instance)
        for res in tmp:
            len_result = len(tmp[res])
            ent = (len_result / len_param) * log2(len_result / len_param)
            child_entropy += ent
        _entropy -= child_entropy


    return _entropy


def calculate_gini(dictionary : dict):
    _gini = 0.0
    for param in dictionary:
        child_gini = 1.0
        tmp = dict()
        len_param = len(dictionary[param])
        for name, instance in dictionary[param].items():
            result = instance['satisfaction']
            if not result in tmp:
                tmp.update({result: list()})
                tmp[result].append(instance)
            else:
                tmp[result].append(instance)
        for res in tmp:
            len_result = len(tmp[res])
            gin = (len_result / len_param)
            child_gini -= gin ** 2
        _gini += child_gini

    return _gini



class Tree:
    def __init__(self, parent , attributes: list, instances: dict, parameter):
        self.parent : Tree = parent
        self.attributes = attributes
        self.instances = instances
        self.parameter = parameter
        self.label_attribute = None
        self.children = list()
        self.entropy = 0
        self.result = None
        Nodes.append(self)
        self.setAttribute(self.result)

    def setAttribute(self, setReult):
        best_entropy = 2147483647
        for attribute in self.attributes:
            temp = dict() # to save types of each attribute
            for instance, instanceValue in self.instances.items():
                parameter = self.instances[instance][attribute]
                if not parameter in temp:
                    temp.update({parameter:dict()})
                    temp[parameter].update({instance : instanceValue})
                else:
                    temp[parameter].update({instance : instanceValue})

            if useEntropy:
                ent = calculate_entropy(temp)
            elif not useEntropy:
                ent = calculate_gini(temp)
            else:
                ent = best_entropy + 1

            if ent <= best_entropy:
                best_entropy = ent
                self.label_attribute = attribute

        self.entropy = best_entropy
        sibling_entropy = 0
        if not self.parent is None:
            for child in self.parent.children:
                sibling_entropy += child.entropy

        if not ( (useEntropy and best_entropy == 0 )
                or (not useEntropy and best_entropy == 0)
                or not self.parent is None and (self.parent.entropy - sibling_entropy >= deltaEntropy)
            ):

            self.createChild()
        else:
            all_values = self.instances.values()
            all_results = []
            for k in all_values:
                all_results.append(k['satisfaction'])

            setReult = max(all_results)
            self.result = setReult


    def createChild(self):
        children = dict()
        # print(self.instances.items())
        for instance, instanceValue in self.instances.items():
            parameter = self.instances[instance][self.label_attribute]
            if not parameter in children:
                children.update({parameter: dict()})
                children[parameter].update({instance: instanceValue})
            else:
                children[parameter].update({instance: instanceValue})

        if len(self.attributes) > 1:
            # print(f'>>>{self.attributes}')
            self.attributes.remove(self.label_attribute)
            for childName, childValue in children.items():
                new_node = Tree(self, self.attributes, childValue, childName)
                self.children.append(new_node)
        else:
            return

def quality(tree: Tree, all_instances: dict, count: int) -> float:
    true_predicts , false_predicts = list(), list()
    for test_name, instance in all_instances.items():
        real_result = instance['satisfaction']
        myNode = tree
        counter = count
        try:
            while True:
                if count == -1 :
                    break
                counter -= 1

                if len(myNode.children) == 0:
                    if real_result == myNode.result:
                        true_predicts.append(test_name)
                    else:
                        false_predicts.append(test_name)
                    break

                elif len(myNode.children) > 0:
                    for child in myNode.children:
                        if child.parameter == instance[myNode.label_attribute]:
                            myNode = child
                else:
                    break
        except:
            break

    return 100 * len(true_predicts) / (len(true_predicts) + len(false_predicts)) if not len(true_predicts) == 0 else 0


def show(nodes: list):
    for node in nodes:
        if not node.parent is None:
            print(f"Parent: {node.parent.label_attribute}")
        else:
            print(f"Parent: ROOT")

        print(f"Parameter: {node.parameter}")

        print(f"Attribute: {node.label_attribute}\n")

        print(f"Entropy: {node.entropy}")

        for num, child in enumerate(node.children):
            if not child.label_attribute is None:
                print(f"Child {num+1}: {child.label_attribute}")
        else:
            if not node.result is None:
                print(f"Result: {node.result}")
        print('=============================================')


def project1():
    tree = Tree(None, all_attributes[:-1], train_instances, None)

    show(Nodes)

    accurate = quality(tree, test_instances, len(Nodes))
    print(f"accurate: {round(accurate, 2)}%")


def project2():
    tree = Tree(None, airplane_attributes[:-1], airplane_train, None)

    print(len(Nodes))
    show(Nodes)

    print("Train Accurate")
    train_accurate = quality(tree, airplane_train, len(Nodes))
    print(f"accurate: {round(train_accurate, 2)}%\n")
    print("Test Accurate")
    test_instance = quality(tree, airplane_test, len(Nodes))
    print(f"accurate: {round(test_instance, 2)}%")


if __name__ == '__main__':
    Nodes = []

    print("Project one")
    project1()

    print("Project two")
    project2()
