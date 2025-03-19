Link to solving process: https://youtu.be/CapPbLev1iw
1) The steps you took to solve the problem:  
In my opinion there is no characteristic to determine the optimal path so my approach is using BFS to do a brute force search with all nodes as the starting point. 
Different from tradition BFS where the path is not allowed to visit nodes that have been visited before, the optimal path of this solution may visit the same node multiple times. So a good way to optimise it is to put the state into consideration. State is the array of nodes that we have visited before and a node is only allowed to be visited once more if we bring in a new state.    
If there is no characteristic to determine the optimal path, this is probably quite a good solution.

2) Challenges I faced:  
use GPT-4o-mini to check the syntax. Luckily in this question, the code is not complicated and the error message is enough for me to spot the bug

3) AI Tools for assistance:  
GPT-4o-mini  
GPT-4o: it gives me inspiration on using bitwise actions to record the state, otherwise, I was thinking to use set/arrays to record the state which might cost extra runtime to convert array/set to tuple and makes the code look complicated.  
(Although GPT-4o already gives the correct solution, it is meaningless to just submit that...) 