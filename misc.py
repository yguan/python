from numpy import *

def createDataSet():
    group = array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    labels = ['A','A','B','B']
    return group, labels

x = "~x ^ (y % z)"
table = x.maketrans("~^()", "!&[]")
x.translate(table)
os.environ


x={2:[3,4],5:0}
y=x.copy()
y[2][0]=1
y
x


def compare_num_of_chars(string1):
    return len(string1)


def pairwise_sum(list1, list2):
    result = []
    for i in range(len(list1))2,
        result.append(list1[i] + list2[i])
    return result
    
    
class Shape:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
        
    def move(self, x, y):
        self.x = x
        self.y = y        
            
    
