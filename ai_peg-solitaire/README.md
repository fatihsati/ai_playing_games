# peg_solitaire_experiment

An experiment of uninformed search algorithms on Peg Solitaire (Solo Test).

## Used Algorithms
- [x] Breadth-First Search
- [x] Depth-First Search
- [x] Iterative Deepening Search
- [x] Depth-First Search with Random Selection
- [X] Depth-First Search with a Node Selection Heuristic

## Resutls

The purpose of the experiment is to compare different uninformed search algorithms and be able to observe their speed, time complexity and also space complexity. <br/>
None of the algorithm was able to find the solution in one hour.

### Breadth-First Search
```
Method: BFS - Time limit: 3600 seconds
Sub-optimal solution found with 25 remaining pegs
No Optimal solution found - Time Limit
Time spent: 3600.07
Explored node count: 79762
Max number of nodes in memory: 657415
```

### Depth-First Search
```
Method: DFS - Time limit: 3600 seconds
Sub-optimal solution found with 2 remaining pegs
No Optimal solution found - Time Limit
Time spent: 3600.0
Explored node count: 265144102
Max number of nodes in memory: 159
```

### Iterative Deepening Search
```
Method: IDS - Time limit: 3600 seconds
Sub-optimal solution found with 23 remaining pegs
No Optimal solution found - Time Limit
Time spent: 3642.48
Explored node count: 44236751
Max number of nodes in memory: 86
```

### Depth-First Search with Random Selection
```
Method: DFS Random Selection - Time limit: 3600 seconds
Sub-optimal solution found with 3 remaining pegs
No Optimal solution found - Time Limit
Time spent: 3600.0
Explored node count: 264804840
Max number of nodes in memory: 175
```

### Depth-First Search with a Node Selection Heuristic
```
Method: DFS with Heuristic - Time limit: 3600 seconds
Sub-optimal solution found with 2 remaining pegs
No Optimal solution found - Time Limit
Time spent: 3600.0
Explored node count: 195581593
Max number of nodes in memory: 201
```
