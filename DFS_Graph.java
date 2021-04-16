import java.util.*;

public class DFS_Graph {
    private static LinkedList<Integer> adjLists[];
    private static boolean visited[];

    public DFS_Graph(int vertices) {
        adjLists = new LinkedList[vertices];
        visited = new boolean[vertices];

        for(int i=0; i<vertices; i++) {
            adjLists[i] = new LinkedList<Integer>();
        }
    }

    public static void addEdge(int src, int dest) {
        adjLists[src].add(dest);
    }

    public static void DFS(int vertex) {
        visited[vertex] = true;
        System.out.println(vertex + " ");

        Iterator<Integer> iter = adjLists[vertex].listIterator();
        while(iter.hasNext()) {
            int adj = iter.next();
            if(!visited[adj])
            DFS(adj);
        }
    }
    public static void main(String args[]) {
        DFS_Graph g = new DFS_Graph(4);
        g.addEdge(0, 1);
        g.addEdge(0, 2);
        g.addEdge(1, 2);
        g.addEdge(2, 3);

        System.out.println("Following is Depth First Traversal");
        g.DFS(2);
    }
}
