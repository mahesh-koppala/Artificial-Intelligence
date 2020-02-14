import sys
from collections import deque

class Node:
    def __init__(self, name, cumulative, d, f):
        self.name = name
        self.parents = None
        self.cumulative = cumulative
        self.d = d
        self.f = f
        
        
class informed_search:
    
    
    def find_route(self, start, target):
        
        
           z=0
           input_file = sys.argv[1]
           Heuristic_file = sys.argv[4]
           f = open(input_file, "r")
           h = open(Heuristic_file, "r")
           PATH = []
           Heuristic = []
           V = []
           for line in h:
               if "END OF INPUT" in line:
                   break
               else:
                   Hu = line.split()
                   heuristic_city = Hu[0]
                   heuristic_num = Hu[1]
                   Heuristic.append([heuristic_city, heuristic_num])
           for line in f:
               if "END OF INPUT" in line:
                   break
               else:
                   City = line.split()
                   Src = City[0]
                   Destination = City[1]
                   distance = City[2]
                   path1 = [Src, Destination, distance]
                   path2 = [Destination, Src, distance]
                   PATH.append(path1)
                   PATH.append(path2)
           Queue = deque()
           Queue.append(Node(start, 0, 0, 0))
           nodes_generated=0
           no_target = False
           while True:
               if len(Queue) != 0:
                   global w
                   if(len(Queue)>w):
                       w = len(Queue)
                   nExpected = Queue.popleft()
                   z=z+1
                   nodes_generated += 1
                   if nExpected.name == target:
                       break
                   else:
                       if nExpected.name not in V:
                           V.append(nExpected.name)
                           for num in PATH:
                               if num[0] == nExpected.name:
                                   for hu in Heuristic:
                                       if hu[0] == num[1]:
                                           Hunum=hu[1]
 
                                   n = Node(num[1], nExpected.cumulative+int(num[2]), nExpected.d+1, nExpected.cumulative+int(num[2])+int(Hunum))
                                   n.parents= nExpected
                                   Queue.append(n)
                                   s=sorted(Queue, key=lambda node:node.f)
                                   Queue=deque(s)
               else:
                   no_target = True
                   break
           z=z+len(Queue)
           if(no_target == True):
               print ("Nodes Expanded: "+str(nodes_generated))
               print("Nodes Generated:" +str(z-1))
               print("Max Nodes In Memory:" +str(w))
               print ("Distance: Infinity")
               print ("Route: None")
           else:
               print ("Nodes Expanded: "+str(nodes_generated))
               print("Nodes Generated:" +str(z-1))
               print("Max Nodes In Memory:" +str(w))
               print ("Distance: " + str(nExpected.cumulative))
               print ("Route: ")
               path = []
               path.append(target)
               while nExpected.parents != None:
                   path.append(nExpected.parents.name)
                   nExpected = nExpected.parents
               path.reverse()
               i=0
               while i < len(path)-1:
                   for v in PATH:
                       if path[i]==v[0] and path[i+1] == v[1]:
                           print (v[0] +" to "+ v[1]+ " - "+v[2])
                   i += 1








class uninformed_search:
    
    
       def find_route(self, start, target):
          
          
           z=0
           input_file = sys.argv[1] 
           f = open(input_file, "r")
           PATH = []
           V = []
           for line in f:
               if "END OF INPUT" in line:
                   break
               else:
                   City = line.split()
                   Src = City[0]
                   Destination = City[1]
                   distance = City[2]
                   path1 = [Src, Destination, distance]
                   path2 = [Destination, Src, distance]
                   PATH.append(path1)
                   PATH.append(path2)
           Queue = deque()
           Queue.append(Node(start, 0, 0, None)) 
           nodes_generated = 0
           no_target = False
           while True:
               if len(Queue) != 0:
                   global w
                   if(len(Queue)>w):
                       w = len(Queue)
                   nExpected = Queue.popleft() 
                   z=z+1
                   nodes_generated += 1
                   if nExpected.name == target: 
                       break
                   else:
                       if nExpected.name not in V: 
                           V.append(nExpected.name) 
                           for num in PATH:
                               if num[0] == nExpected.name:
                                   n = Node(num[1], nExpected.cumulative+int(num[2]), nExpected.d+1, None)
                                   n.parents= nExpected
                                   Queue.append(n)
                                   s=sorted(Queue, key=lambda node:node.cumulative)
                                   Queue=deque(s)
               else:
                   no_target = True
                   break
 
           z=z+len(Queue)
           if(no_target == True):
               print ("Nodes Expanded: "+str(nodes_generated))
               print("Nodes Generated:" +str(z-1))
               print("Max Nodes In Memory:" +str(w))
               print ("Distance: Infinity")
               print ("Route: None")
           else:
               print ("Nodes Expanded: "+str(nodes_generated))
               print("Nodes Generated:" +str(z-1))
               print("Max Nodes in Memory:" +str(w))
               print ("Distance: " + str(nExpected.cumulative))
               print ("Route: ")
               path = []
               path.append(target)
               while nExpected.parents != None:
                   path.append(nExpected.parents.name)
                   nExpected = nExpected.parents
               path.reverse()
               i=0
               while i < len(path)-1:
                   for v in PATH:
                       if path[i]==v[0] and path[i+1] == v[1]:
                           print (v[0] +" to "+ v[1]+ " - "+v[2])
                   i += 1
 


if __name__ == "__main__":
            w=0
            source = sys.argv[2]
            destination = sys.argv[3]
            
            if len(sys.argv) >4:
                u=informed_search()
            else:
                u=uninformed_search()
            u.find_route(source, destination)
 
