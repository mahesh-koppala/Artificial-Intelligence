NAME : Mahesh Koppala

UTA_ID : 1001764522

PROGRAMMING LANGUAGE : Python

CODE STRUCTURE : 
1. class Node used to initialize a node.
2. Main function is used to read the command line arguments and decide if uniformed or informed search is performed. Call to the respective methods based on the decision.
3. In the find_route method first read the input file for uninformed and input file and heuristic file for informed search.
4. Start loop until queue is not empty, pop an item from queue, find its successors and append them to the queue and sort the queue.
5. Once the Queue is empty, Print the values Nodes expanded, Nodes generated , Max nodes in memory, Distance and the path from source to destination for each case when goal  is found and when goal not found.

INSTRUCTIONS :
Make sure all the 3 files(2 input files and the Python file) are in the same folder.
To run Uninformed Search : python find_route.py input1.txt Source Destination
To run Informed Search : python find_route.py input1.txt Source Destination h_kassel.txt