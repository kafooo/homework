from abc import ABC, abstractmethod

class GNode(ABC):
    '''An abstract base class representing a node in a graph'''
    @abstractmethod
    def getName(self) -> str:
        '''Returns the name of the node as a string'''
        pass

    @abstractmethod
    def getChildren(self) -> list['GNode']:
        '''Returns a list of child nodes of this node'''
        pass

class specificNode(GNode):
    '''A class representing a specific implementation of a GNode'''
    def __init__(self, name, children):
        self.name = name
        self.children = children

    def getName(self) -> str:
        return self.name

    def getChildren(self) -> list['GNode']:
        return self.children


def walkGraph(node: 'GNode') -> list['GNode']:
    '''Returns list of all GNode's in the graph without duplicates'''
    def dfs(node):
        nodeName = node.getName()
        if nodeName in visited:
            return
        visited.add(nodeName)
        result.append(nodeName)
        for child in node.getChildren():
            dfs(child)
    
    visited = set()
    result = []
    dfs(node)
    return result

def paths(node: 'GNode') -> list[list['GNode']]:
    '''Returns list of all possible paths through the graph'''
    nodeName = node.getName()
    if not node.getChildren():
        return [[nodeName]]
    result = []
    for child in node.getChildren():
        child_paths = paths(child)
        for path in child_paths:
            result.append([nodeName] + path)
    return result

if __name__ == '__main__':
    testNode = specificNode('A', [
        specificNode('B', [
            specificNode('E', []),
            specificNode('F', []),
        ]),
        specificNode('C', [
            specificNode('E', []),
            specificNode('G', []),
            specificNode('H', []),
        ]),
        specificNode('D', [
            specificNode('J', []),
        ]),
    ])

    print(f'walkGraph result:\n{walkGraph(testNode)}\n')
    print(f'paths result:\n{paths(testNode)}\n')