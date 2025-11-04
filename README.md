# A-search-and-Edmonds-Karp-Network-Flow-algorithms


I built this project out of curiosity to explore two elegant algorithmic ideas:
- A* search for solving sliding puzzles (8-puzzle, 15-puzzle, and general $N \times N$).
- Edmonds–Karp (BFS-based) max-flow for directed networks.

## Why I did it
- A* search shows how informed search can find optimal solutions fast by combining path cost and heuristics. It’s the backbone of many routing, planning, and puzzle solvers.
- Max flow sits at the core of graph optimization: matching, scheduling, cuts, connectivity, and more. Edmonds–Karp is a robust baseline: predictable, easy to implement, and guarantees optimality.
- Designing general solutions (no hardcoded sizes for puzzles).
- Choosing admissible/consistent heuristics for optimal A*.
- Working with residual graphs, BFS, and flow augmentation.
- Practical use of hashable states, priority queues, and memory-efficient bookkeeping.
- Designing general solutions (no hardcoded sizes for puzzles).
- Choosing admissible/consistent heuristics for optimal A*.
- Working with residual graphs, BFS, and flow augmentation.
- Practical use of hashable states, priority queues, and memory-efficient bookkeeping.
- 
## Context

- A* Puzzle Solver
  - Works for any $N \times N$ board (not hardcoded).
  - Represents states, legal moves (L/R/U/D), and reconstructs the optimal move sequence.
  - Uses the Manhattan-distance heuristic (monotone/consistent), so A* returns an optimal solution.
  - Solves all 8-puzzle instances in reasonable time with efficient open/closed sets.

- Edmonds–Karp Max Flow
  - Input: capacities as a 2D array (directed graph).
  - Computes maximum flow value, per-edge flow, and a cut derived from the final BFS partition (proof of optimality).
  - Uses BFS to find shortest augmenting paths in the residual graph each iteration.

## Key ideas 

- A* search
  - State: board layout with $0$ as the empty tile.
  - Cost: number of moves taken so far ($g$).
  - Heuristic: sum of Manhattan distances for all tiles to their goal positions ($h$).
  - Priority: $f = g + h$ in a min-priority queue. A consistent $h$ ensures optimality.

- Edmonds–Karp
  - Repeatedly find augmenting paths via BFS in the residual graph.
  - Augment flow along the path by the bottleneck capacity.
  - Stop when no path exists from source to sink.
  - Produces a cut from the final reachable set in the residual graph.




## Quick start

- Puzzle:
  - Create a board as a flat list or 2D array with $0$ as the empty tile.
  - Call the solver; it returns the optimal move sequence (e.g., `RRD`) and the visited stats.

- Max flow:
  - Provide a capacity matrix `C[u][v]` (non-negative integers).
  - Call `solve()` to get max flow; call `cut()` to get the source-side partition.
  - Inspect per-edge flows from the internal state after `solve()`.


