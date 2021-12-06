import java.util.*;

public class DFS_algorithm {

    private static LinkedList<Integer> adjLists[];
    private static boolean visited[];

    public DFS_algorithm(int vertices) {
        adjLists = new LinkedList[vertices];
        visited = new boolean[vertices];

        for(int i=0; i<vertices; i++) {
            adjLists[i] = new LinkedList<Integer>();
        }
    }

    public void addEdge(int src, int dest) {
        adjLists[src].add(dest);
    }

    public void DFS(int vertex) {
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
        DFS_algorithm g = new DFS_algorithm(4);
        g.addEdge(0, 1);
        g.addEdge(0, 2);
        g.addEdge(1, 2);
        g.addEdge(2, 3);

        System.out.println("Following is Depth First Traversal");
        g.DFS(2);
    }
}
