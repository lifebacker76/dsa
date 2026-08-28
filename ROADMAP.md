# DSA Learning Roadmap (Python)

> For someone with a Data Analyst background transitioning into DSA & problem-solving.

---

## How to Use This Repo

Each folder contains a **Jupyter notebook** you can run cell-by-cell.
Every notebook follows the same pattern:

1. **Concept** — visual explanation with diagrams
2. **Implementation** — build the data structure / algorithm from scratch
3. **Walkthrough** — step-by-step trace of how it works
4. **Practice Problems** — easy → medium, with hints and solutions
5. **Real-World Connection** — how this relates to data/analytics work

---

## Learning Order & Time Estimates

| # | Topic | Folder | Estimated Time | Prereqs |
|---|-------|--------|---------------|---------|
| 0 | Python Foundations for DSA | `00_Python_Foundations/` | 2-3 hours | — |
| 1 | Big-O & Complexity Analysis | `01_Big_O_and_Complexity/` | 3-4 hours | Topic 0 |
| 2 | Arrays & Strings | `02_Arrays_and_Strings/` | 5-6 hours | Topics 0-1 |
| 3 | Linked Lists | `03_Linked_Lists/` | 4-5 hours | Topics 0-1 |
| 4 | Stacks & Queues | `04_Stacks_and_Queues/` | 3-4 hours | Topics 2-3 |
| 5 | Hash Maps & Sets | `05_Hash_Maps/` | 4-5 hours | Topics 0-2 |
| 6 | Recursion & Backtracking | `06_Recursion/` | 6-8 hours | Topics 0-4 |
| 7 | Sorting Algorithms | `07_Sorting_Algorithms/` | 5-6 hours | Topics 0-2, 6 |
| 8 | Searching (Binary Search) | `08_Searching_Algorithms/` | 4-5 hours | Topics 0-2, 7 |
| 9 | Trees (Binary Tree, BST, Heaps) | `09_Trees/` | 8-10 hours | Topics 3-6 |
| 10 | Graphs (BFS, DFS, Shortest Path) | `10_Graphs/` | 8-10 hours | Topics 4-6, 9 |
| 11 | Dynamic Programming | `11_Dynamic_Programming/` | 10-12 hours | Topics 2, 6 |
| 12 | Greedy Algorithms | `12_Greedy_Algorithms/` | 4-5 hours | Topics 7-8 |

**Total estimated time: 65-85 hours** (spread over 8-12 weeks at ~1 hour/day)

---

## Detailed Topics Checklist

### 1. Arrays & Strings
- [ ] Two Pointer Technique
- [ ] Sliding Window (Fixed & Variable)
- [ ] Prefix Sum & Suffix Arrays
- [ ] Kadane's Algorithm (Max Subarray)
- [ ] Dutch National Flag (Sort 0,1,2)
- [ ] Merge Intervals
- [ ] Trapping Rain Water
- [ ] Next Permutation
- [ ] Rotate Array / Matrix
- [ ] String Matching (KMP, Rabin-Karp)
- [ ] Longest Substring Without Repeating Chars
- [ ] Anagram Checking & Grouping
- [ ] Stock Buy & Sell Problems
- [ ] Spiral Matrix Traversal
- [ ] Subarray Sum Equals K

### 2. Hashing & HashMaps
- [ ] Two Sum / Three Sum / Four Sum
- [ ] Frequency Counting
- [ ] Longest Consecutive Sequence
- [ ] Subarray with Given Sum
- [ ] Group Anagrams
- [ ] Count Distinct Elements in Window
- [ ] First Non-Repeating Character
- [ ] Longest Substring with K Distinct Chars
- [ ] Hashing Collision Resolution (Chaining / Open Addressing)

### 3. Linked Lists
- [ ] Reverse a Linked List (Iterative & Recursive)
- [ ] Detect & Remove Cycle (Floyd's Algorithm)
- [ ] Merge Two Sorted Lists
- [ ] Merge K Sorted Lists
- [ ] Remove Nth Node from End
- [ ] Palindrome Linked List
- [ ] Intersection of Two Linked Lists
- [ ] Flatten a Multi-Level List
- [ ] LRU Cache Implementation
- [ ] Clone a List with Random Pointer
- [ ] Add Two Numbers (Linked List)
- [ ] Rotate Linked List

### 4. Stacks & Queues
- [ ] Next Greater / Smaller Element
- [ ] Min Stack / Max Stack
- [ ] Largest Rectangle in Histogram
- [ ] Valid Parentheses
- [ ] Implement Queue using Stacks
- [ ] Implement Stack using Queues
- [ ] Sliding Window Maximum (Deque)
- [ ] Stock Span Problem
- [ ] Celebrity Problem
- [ ] Trapping Rain Water (Stack approach)
- [ ] Evaluate Postfix / Prefix Expressions
- [ ] Monotonic Stack / Queue Patterns

### 5. Binary Trees
- [ ] All Traversals (Inorder, Preorder, Postorder, Level-Order)
- [ ] Height / Depth of Tree
- [ ] Diameter of Binary Tree
- [ ] Check Balanced Tree
- [ ] Lowest Common Ancestor (LCA)
- [ ] Boundary Traversal
- [ ] Vertical Order Traversal
- [ ] Top View / Bottom View / Left View / Right View
- [ ] Zigzag Level Order Traversal
- [ ] Flatten BT to Linked List
- [ ] Serialize & Deserialize Binary Tree
- [ ] Maximum Path Sum
- [ ] Check Mirror / Symmetric Tree
- [ ] Construct BT from Inorder + Preorder/Postorder

### 6. Binary Search Trees (BST)
- [ ] Search / Insert / Delete in BST
- [ ] Validate BST
- [ ] Kth Smallest/Largest in BST
- [ ] LCA in BST
- [ ] Floor & Ceil in BST
- [ ] Convert Sorted Array to BST
- [ ] Inorder Successor/Predecessor
- [ ] Merge Two BSTs
- [ ] Two Sum in BST
- [ ] Recover BST (Two nodes swapped)

### 7. Heaps & Priority Queues
- [ ] Kth Largest/Smallest Element
- [ ] Top K Frequent Elements
- [ ] Merge K Sorted Lists/Arrays
- [ ] Median in a Stream
- [ ] Heap Sort
- [ ] Task Scheduler
- [ ] Reorganize String
- [ ] Meeting Rooms I & II
- [ ] K Closest Points to Origin
- [ ] Min Cost to Connect Sticks

### 8. Recursion & Backtracking
- [ ] Subsets / Subsequences Generation
- [ ] Permutations (with/without duplicates)
- [ ] Combination Sum I, II, III, IV
- [ ] N-Queens Problem
- [ ] Sudoku Solver
- [ ] Word Search / Boggle
- [ ] Rat in a Maze
- [ ] Generate Parentheses
- [ ] Letter Combinations of Phone Number
- [ ] Palindrome Partitioning
- [ ] Knight's Tour
- [ ] M-Coloring Problem

### 9. Dynamic Programming (Critical!)
- [ ] 0/1 Knapsack & Variations
- [ ] Unbounded Knapsack
- [ ] Longest Common Subsequence (LCS)
- [ ] Longest Increasing Subsequence (LIS)
- [ ] Edit Distance
- [ ] Coin Change (Min Coins / Count Ways)
- [ ] Matrix Chain Multiplication
- [ ] Partition Equal Subset Sum
- [ ] Rod Cutting
- [ ] Egg Drop Problem
- [ ] Longest Palindromic Subsequence
- [ ] Word Break Problem
- [ ] Distinct Subsequences
- [ ] Burst Balloons
- [ ] DP on Trees (House Robber III)
- [ ] DP on Grids (Unique Paths, Min Path Sum)
- [ ] DP with Bitmask
- [ ] Digit DP (Experienced)
- [ ] String DP (Wildcard, Regex Matching)
- [ ] Stock Problems (All variants)

### 10. Graphs (Very Important!)
- [ ] BFS / DFS Traversal
- [ ] Number of Islands / Connected Components
- [ ] Cycle Detection (Directed & Undirected)
- [ ] Topological Sort (Kahn's + DFS)
- [ ] Shortest Path: Dijkstra's Algorithm
- [ ] Shortest Path: Bellman-Ford
- [ ] Shortest Path: Floyd-Warshall
- [ ] Minimum Spanning Tree (Prim's & Kruskal's)
- [ ] Union-Find / Disjoint Set Union (DSU)
- [ ] Bipartite Graph Check
- [ ] Bridges & Articulation Points (Tarjan's)
- [ ] Strongly Connected Components (Kosaraju's)
- [ ] Word Ladder I & II
- [ ] Clone Graph
- [ ] Alien Dictionary
- [ ] Course Schedule I & II
- [ ] Cheapest Flights Within K Stops
- [ ] Network Delay Time
- [ ] Accounts Merge
- [ ] Graph Coloring

### 11. Binary Search (Advanced)
- [ ] Search in Rotated Sorted Array
- [ ] Find Minimum in Rotated Array
- [ ] Median of Two Sorted Arrays
- [ ] Koko Eating Bananas
- [ ] Aggressive Cows / Book Allocation
- [ ] Painter's Partition
- [ ] Peak Element
- [ ] Search in 2D Matrix
- [ ] Binary Search on Answer (Pattern)
- [ ] Split Array Largest Sum
- [ ] Capacity to Ship Packages
- [ ] Nth Root of a Number

### 12. Greedy Algorithms
- [ ] Activity Selection / Job Scheduling
- [ ] Fractional Knapsack
- [ ] Huffman Encoding
- [ ] Minimum Platforms
- [ ] Jump Game I & II
- [ ] Gas Station
- [ ] Candy Distribution
- [ ] Assign Cookies
- [ ] Non-overlapping Intervals
- [ ] Meeting Rooms
- [ ] Minimum Number of Coins

### 13. Tries (Bonus)
- [ ] Implement Trie (Insert, Search, StartsWith)
- [ ] Word Search II (Trie + Backtracking)
- [ ] Longest Common Prefix using Trie
- [ ] Auto-Complete System
- [ ] Maximum XOR of Two Numbers (Trie)
- [ ] Count Distinct Substrings
- [ ] Palindrome Pairs

### 14. Segment Trees & BIT (Competitive)
- [ ] Range Sum Query (Mutable)
- [ ] Range Minimum Query
- [ ] Lazy Propagation
- [ ] Count of Smaller Numbers After Self
- [ ] Binary Indexed Tree (Fenwick Tree)
- [ ] Merge Sort Tree

### 15. Bit Manipulation
- [ ] Single Number (I, II, III)
- [ ] Power of Two / Four
- [ ] Counting Bits
- [ ] Subsets using Bitmask
- [ ] XOR from 1 to N
- [ ] Find Two Non-Repeating Elements
- [ ] Reverse Bits
- [ ] Missing Number (XOR approach)

---

## Suggested Weekly Plan

### Weeks 1-2: Build the Base
- [ ] Complete Topic 0 (Python Foundations)
- [ ] Complete Topic 1 (Big-O)
- [ ] Solve 5 easy array problems on LeetCode

### Weeks 3-4: Linear Structures
- [ ] Complete Topic 2 (Arrays & Strings)
- [ ] Complete Topic 3 (Linked Lists)
- [ ] Complete Topic 4 (Stacks & Queues)
- [ ] Solve 10 easy problems (mix of arrays, strings, stacks)

### Weeks 5-6: Hashing & Recursion
- [ ] Complete Topic 5 (Hash Maps)
- [ ] Complete Topic 6 (Recursion)
- [ ] Solve 10 problems (5 easy + 5 medium)

### Weeks 7-8: Sorting & Searching
- [ ] Complete Topic 7 (Sorting)
- [ ] Complete Topic 8 (Binary Search Advanced)
- [ ] Solve 10 problems (mix of sorting, binary search)

### Weeks 9-10: Trees & Graphs
- [ ] Complete Topic 9 (Trees + BST + Heaps)
- [ ] Complete Topic 10 (Graphs)
- [ ] Solve 15 problems (mix of tree and graph)

### Weeks 11-12: Advanced
- [ ] Complete Topic 11 (Dynamic Programming)
- [ ] Complete Topic 12 (Greedy)
- [ ] Solve 15 problems (DP + greedy)

### Weeks 13-14: Bonus & Revision
- [ ] Topics 13-15 (Tries, Segment Trees, Bit Manipulation)
- [ ] Revisit weak areas
- [ ] Mock interview practice

---

## Tips for Data Analysts

1. **You already know more than you think** — pandas uses hash maps, SQL JOINs are graph problems, window functions are like sliding window patterns.
2. **Think in terms of data flow** — just like ETL pipelines, algorithms transform input data step-by-step.
3. **Visualize everything** — draw arrays, draw pointers, draw trees. Use the notebook cells to print intermediate states.
4. **Don't memorize — understand the pattern** — there are ~15 core patterns that cover 90% of problems.
5. **Track your progress** — use the `practice_log/` folder to log problems you solve.

---

## Resources

- **Practice**: [LeetCode](https://leetcode.com), [NeetCode 150](https://neetcode.io/practice)
- **Visualize**: [VisuAlgo](https://visualgo.net), [Python Tutor](https://pythontutor.com)
- **Video**: [NeetCode YouTube](https://youtube.com/@NeetCode)
- **Book**: "Grokking Algorithms" by Aditya Bhargava (very visual, beginner-friendly)
