# 2121A-Letter-Home

**Problem:** [2121A-Letter-Home](https://codeforces.com/contest/2121/problem/A)

**time limit per test:** 1 second

**memory limit per test:** 256 megabytes

---

You are given an array of distinct integers x_1, x_2, …, x_n and an integer s. 

Initially, you are at position pos = s on the X axis. In one step, you can perform exactly one of the following two actions:

-  Move from position pos to position pos + 1. 
-  Move from position pos to position pos - 1. 
A sequence of steps will be considered successful if, during the entire journey, you visit each position x_i on the X axis at least once. Note that the initial position pos = s is also considered visited. 

Your task is to determine the minimum number of steps in any successful sequence of steps.


**Input**

Each test consists of multiple test cases. The first line contains a single integer t (1 ≤q t ≤q 1000) — the number of test cases. The description of the test cases follows.

The first line of each test case contains two integers n and s (1 ≤q n ≤q 10, 1 ≤q s ≤q 100) — the number of positions to visit and the starting position. 

The second line of each test case contains n integers x_1, x_2, …, x_n (1 ≤q x_i ≤q 100). It is guaranteed that for all 1 ≤q i  \lt  n, it holds that x_i  \lt  x_{i + 1}.


**Output**

For each test case, output the minimum number of steps in any successful sequence of steps.


**Example**

**Input**

```
12
1 1
1
1 2
1
1 1
2
2 1
2 3
2 2
1 3
2 3
1 2
3 1
1 2 3
3 2
1 3 4
3 3
1 2 3
4 3
1 2 3 10
5 5
1 2 3 6 7
6 6
1 2 3 9 10 11
```

**Output**

```
0
1
1
2
3
2
2
4
2
11
8
15
```


**Note**

In the first test case, no steps need to be taken, so the only visited position will be 1. 

In the second test case, the following path can be taken: 2 → 1. The number of steps is 1. 

In the third test case, the following path can be taken: 1 → 2. The number of steps is 1.

In the fifth test case, the following path can be taken: 2 → 1 → 2 → 3. The number of steps is 3.
