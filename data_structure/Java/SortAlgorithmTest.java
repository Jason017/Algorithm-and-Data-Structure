import org.junit.jupiter.api.Test;

/**
 * JUnit5 Testing
 * 
 * @author Bo Guan
 *
 */
public class SortAlgorithmTest {
    private int[] arr;
    private int n;

    @Test
    void sortTest() {
        // heapify
        System.out.println("Heap Sort Test");
        arr = new int[] { 4, 10, 3, 5, 1, 2 };
        n = arr.length;
        SortAlgorithm.heapify(arr, n, 0);
        System.out.println(">>> heapify");
        for (int i = 0; i < n; i++) {
            System.out.println(arr[i]);
        }

        // buildHeap
        arr = new int[] { 2, 5, 3, 1, 10, 4 };
        n = arr.length;
        SortAlgorithm.buildHeap(arr);
        System.out.println(">>> buildHeap");
        for (int i = 0; i < n; i++) {
            System.out.println(arr[i]);
        }

        // heapSort
        arr = new int[] { 2, 5, 3, 1, 10, 4 };
        n = arr.length;
        SortAlgorithm.heapSort(arr);
        System.out.println(">>> heapSort");
        for (int i = 0; i < n; i++) {
            System.out.println(arr[i]);
        }

        // radixSort
        System.out.println("Radix Sort Test");
        arr = new int[] { 2, 5, 3, 1, 10, 4 };
        n = arr.length;
        int maxDigit = SortAlgorithm.getMaxDigit(arr);
        arr = SortAlgorithm.radixSort(arr, maxDigit);
        for (int i = 0; i < n; i++) {
            System.out.println(arr[i]);
        }

        // mergeSort
        System.out.println("Merge Sort Test");
        arr = new int[] { 6, 7, 9, 13, 21, 45, 101, 102 };
        n = arr.length;
        SortAlgorithm.mergeSort(arr, 0, n - 1);
        for (int i = 0; i < n; i++) {
            System.out.println(arr[i]);
        }

        // shellSort
        System.out.println("Shell Sort Test");
        arr = new int[] { 2, 5, 3, 1, 10, 4 };
        n = arr.length;
        SortAlgorithm.shellSort(arr);
        for (int i = 0; i < n; i++) {
            System.out.println(arr[i]);
        }

        // selectionSort
        System.out.println("Selection Sort Test");
        arr = new int[] { 2, 5, 3, 1, 10, 4 };
        n = arr.length;
        SortAlgorithm.selectionSort(arr);
        for (int i = 0; i < n; i++) {
            System.out.println(arr[i]);
        }

        // insertionSort
        System.out.println("Insertion Sort Test");
        arr = new int[] { 2, 5, 3, 1, 10, 4 };
        SortAlgorithm.insertionSort(arr);
        for (int i = 0; i < n; i++) {
            System.out.println(arr[i]);
        }
    }
}
