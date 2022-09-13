// https://www.geeksforgeeks.org/all-topological-sorts-of-a-directed-acyclic-graph/

import java.util.*;

class Graph {
    private static void allTopologicalSortsUtil(
            int n,
            boolean[] visited,
            int[] indegree,
            List<Integer> path,
            Map<Integer, List<Integer>> adjMap) {
        boolean flag = false;
        for (int i = 0; i < n; i++) {
            if (!visited[i] && indegree[i] == 0) {
                visited[i] = true;
                path.add(i);
                for (int nei : adjMap.get(i)) {
                    indegree[nei]--;
                }
                allTopologicalSortsUtil(n, visited, indegree, path, adjMap);
                visited[i] = false;
                path.remove(path.size() - 1);
                for (int nei : adjMap.get(i)) {
                    indegree[nei]++;
                }

                flag = true;
            }
        }

        if (!flag) {
            path.forEach(i -> System.out.print(i + " "));
            System.out.println();
        }
    }

    public static void allTopologicalSorts(int n, int[][] graph) {
        Map<Integer, List<Integer>> adjMap = new HashMap<>();
        boolean[] visited = new boolean[n];
        int[] indegree = new int[n];
        for (int i = 0; i < n; i++) {
            adjMap.put(i, new ArrayList<>());
        }
        for (int[] pair : graph) {
            adjMap.get(pair[0]).add(pair[1]);
        }

        for (int i = 0; i < n; i++) {
            for (int node : adjMap.get(i)) {
                indegree[node]++;
            }
        }
        allTopologicalSortsUtil(n, visited, indegree, new ArrayList<>(), adjMap);
    }

    public static void main(String[] args) {
        int n = 6;
        int[][] graph = { { 5, 2 }, { 5, 0 }, { 4, 0 }, { 4, 1 }, { 2, 3 }, { 3, 1 } };
        allTopologicalSorts(n, graph);
    }
}
