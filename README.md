# Multiple Traveling Salesman Problem (mTSP)

## Introduction
The Traveling Salesman Problem (TSP) is a classic challenge that seeks to find the shortest route to visit a set of cities once and return to the starting city. Although effective approximation algorithms exist for TSP, new methods continue to be explored, such as evolutionary algorithms, due to their applicability to real-world problems. This project focuses on a variation of TSP known as the Multiple Traveling Salesman Problem (mTSP), where more than one traveling salesman is involved, each with a specific set of cities to visit.

## Constructive Heuristic
The heuristic used to solve the mTSP is the Centroid Heuristic. This method aims to find a midpoint, called the centroid, which represents a central position in relation to the cities to be visited. It begins with the random selection of a city as the starting point, followed by the calculation of the centroid of the remaining cities. The process continues by selecting the city closest to the centroid to visit, repeating until all cities have been visited. Although it provides an approximate solution to the problem, the Centroid Heuristic is effective and relatively simple to implement, making it suitable for practical situations where computational complexity is a concern.

## Computational Experiments
The experiments were conducted on a macOS Sonoma computer with an Apple M1 chip and 16GB of RAM. The project was implemented in Python 3.12.4 and developed in Visual Studio Code 2024. The test set consists of 9 instances, varying the number of cities and the number of salesmen. The results obtained for each instance are summarized in Table 1 below. There is a disparity in relation to the optimal solutions provided, which was expected due to the approximate nature of the heuristic used. However, the results demonstrate the effectiveness of the Centroid Heuristic in the practical resolution of the mTSP.

### Test Instances
- **Number of cities (n)**: 13, 17, 19, 31, 47, 59, 71, 83, 91
- **Number of salesmen (m)**: 1, 3, 5

### Results
| Instance       | n   | m   | k  | f(x) | r    |
|----------------|-----|-----|----|------|------|
| mTSP-n13-m1    | 13  | 1   | 13 | 3071 | 4148 |
| mTSP-n17-m1    | 17  | 1   | 17 | 3948 | 5766 |
| mTSP-n19-m1    | 19  | 1   | 19 | 4218 | 7614 |
| mTSP-n31-m3    | 31  | 3   | 11 | 5841 | 8319 |
| mTSP-n47-m3    | 47  | 3   | 16 | 6477 | 12346|
| mTSP-n59-m3    | 59  | 3   | 20 | 6786 | 12078|
| mTSP-n71-m5    | 71  | 5   | 15 | 8618 | 16762|
| mTSP-n83-m5    | 83  | 5   | 17 | 9246 | 16911|
| mTSP-n91-m5    | 91  | 5   | 19 | 9586 | 19082|

**Table 1:** Instance Results

## Conclusion
The results of the experiments demonstrate the effectiveness of the Centroid Heuristic in the practical solution of the Multiple Traveling Salesman Problem. Although the approximate solutions show disparities compared to the optimal solutions, the simplicity and effectiveness of this approach make it a viable choice for real-world problems where computational complexity is a concern.

# Authors

| [<img loading="lazy" src="https://avatars.githubusercontent.com/u/114159027?v=4" width=115><br><sub>Eduarda Paiva</sub>](https://github.com/PaivaEduarda) | [<img loading="lazy" src="https://avatars.githubusercontent.com/u/114162946?v=4" width=115><br><sub>Eloisa Paixão</sub>](https://github.com/eloisapaixao) | 
| :---: | :---: |

