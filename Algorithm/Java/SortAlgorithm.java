import java.util.Arrays;

public class SortAlgorithm {

    private static int[] arr;
    private static int n;

    public static void main(String[] args) {

        // // bubbleSort
        // System.out.println("Bubble Sort Test");
        // arr = new int[] { 2, 5, 13, 3, 1, 10, 4 };
        // n = arr.length;
        // bubbleSort1(arr);
        // for (int i = 0; i < n; i++) {
        // System.out.println(arr[i]);
        // }

        // // selectionSort
        // System.out.println("Selection Sort Test");
        // arr = new int[] { 2, 5, 13, 3, 1, 10, 4 };
        // n = arr.length;
        // selectionSort(arr);
        // for (int i = 0; i < n; i++) {
        // System.out.println(arr[i]);
        // }

        // // insertionSort
        // System.out.println("Insertion Sort Test");
        // arr = new int[] { 2, 5, 13, 3, 1, 10, 4 };
        // n = arr.length;
        // insertionSort(arr);
        // for (int i = 0; i < n; i++) {
        // System.out.println(arr[i]);
        // }

        // // heapify
        // arr = new int[] { 2, 5, 13, 3, 1, 10, 4 };
        // n = arr.length;
        // heapify(arr, n, 0);
        // System.out.println(">>> heapify");
        // for (int i = 0; i < n; i++) {
        // System.out.println(arr[i]);
        // }

        // // buildHeap
        // arr = new int[] { 2, 5, 13, 3, 1, 10, 4 };
        // buildHeap(arr);
        // n = arr.length;
        // for (int i = 0; i < n; i++) {
        // System.out.println(arr[i]);
        // }

        // // heapSort
        // System.out.println("Heap Sort Test");
        // arr = new int[] { 2, 5, 13, 3, 1, 10, 4 };
        // n = arr.length;
        // heapSort(arr);
        // for (int i = 0; i < n; i++) {
        // System.out.println(arr[i]);
        // }

        // // mergeSort
        // System.out.println("Merge Sort Test");
        // arr = new int[] { 2, 5, 13, 3, 1, 10, 4 };
        // mergeSort(arr, 0, n - 1);
        // for (int i = 0; i < n; i++) {
        // System.out.println(arr[i]);
        // }
        // arr = new int[] { 2, 5, 13, 3, 1, 10, 4 };
        // n = arr.length;
        // arr = mergeSort(arr);
        // for (int i = 0; i < n; i++) {
        // System.out.println(arr[i]);
        // }

        // quicksort
        System.out.println("Quick Sort Test");
        arr = new int[] { 2, 5, 13, 3, 1, 10, 4 };
        n = arr.length;
        quickSort(arr, 0, n - 1);
        for (int i = 0; i < n; i++) {
            System.out.println(arr[i]);
        }

        // // radixSort
        // System.out.println("Radix Sort Test");
        // arr = new int[] { 2, 5, 13, 3, 1, 10, 4 };
        // n = arr.length;
        // int maxDigit = getMaxDigit(arr);
        // arr = radixSort(arr, maxDigit);
        // for (int i = 0; i < n; i++) {
        // System.out.println(arr[i]);
        // }

        // // shellSort
        // arr = new int[] { 2, 5, 13, 3, 1, 10, 4 };
        // n = arr.length;
        // shellSort(arr);
        // for (int i = 0; i < n; i++) {
        // System.out.println(arr[i]);
        // }
    }

    // --------------------------bubble sort--------------------------
    // O(N^2)
    public static void bubbleSort1(int[] arr) {
        boolean swapped = true;
        for (int i = 0; i < arr.length - 1; i++) {
            for (int j = 0; j < arr.length - i - 1; j++) {
                if (arr[j] > arr[j + 1]) {
                    swap(arr, j, j + 1);
                    swapped = true;
                }
            }
            if (!swapped) {
                break;
            }
        }
    }

    public static void bubbleSort2(int[] arr) {
        boolean swapped = true;
        while (swapped) {
            swapped = false;
            for (int i = 0; i < arr.length - 1; i++) {
                if (arr[i] > arr[i + 1]) {
                    swap(arr, i, i + 1);
                    swapped = true;
                }
            }
        }
    }

    // --------------------------selection sort--------------------------
    // O(N^2)
    public static void selectionSort(int[] arr) {
        int n = arr.length;
        for (int i = 0; i < n - 1; i++) {
            int small = i;
            for (int j = i + 1; j < n; j++) {
                if (arr[j] < arr[small])
                    small = j;
            }
            swap(arr, i, small);
        }
    }

    // --------------------------insertion sort--------------------------
    // O(N^2)
    public static void insertionSort(int[] arr) {
        int n = arr.length;
        for (int i = 1; i < n; i++) {
            int key = arr[i];
            int j = i - 1;
            while (j >= 0 && key < arr[j]) {
                arr[j + 1] = arr[j];
                j--;
            }
            arr[j + 1] = key;
        }
    }

    // --------------------------radix sort--------------------------
    public static int getMaxDigit(int[] arr) {
        int maxValue = getMaxValue(arr);
        return getNumLenght(maxValue);
    }

    public static int getMaxValue(int[] arr) {
        int maxValue = arr[0];
        for (int value : arr) {
            if (maxValue < value) {
                maxValue = value;
            }
        }
        return maxValue;
    }

    public static int getNumLenght(int num) {
        if (num == 0) {
            return 1;
        }
        int lenght = 0;
        for (int temp = num; temp != 0; temp /= 10) {
            lenght++;
        }
        return lenght;
    }

    public static int[] radixSort(int[] arr, int maxDigit) {
        int mod = 10;
        int dev = 1;

        for (int i = 0; i < maxDigit; i++, dev *= 10, mod *= 10) {
            int[][] counter = new int[mod * 2][0];

            for (int j = 0; j < arr.length; j++) {
                int bucket = ((arr[j] % mod) / dev) + mod;
                counter[bucket] = arrayAppend(counter[bucket], arr[j]);
            }

            int pos = 0;
            for (int[] bucket : counter) {
                for (int value : bucket) {
                    arr[pos++] = value;
                }
            }
        }
        return arr;
    }

    private static int[] arrayAppend(int[] arr, int value) {
        arr = Arrays.copyOf(arr, arr.length + 1);
        arr[arr.length - 1] = value;
        return arr;
    }

    // --------------------------shell sort--------------------------
    public static void shellSort(int[] arr) {
        int n = arr.length;
        int mid = n / 2;
        while (mid > 0) {
            for (int i = mid; i < n; i++) {
                int j = i - mid;
                while (j >= 0 && arr[j] > arr[j + mid]) {
                    swap(arr, j, j + mid);
                    j -= mid;
                }
            }
            mid /= 2;
        }
    }

    // --------------------------merge sort--------------------------
    // O(N*log(N))), O(N)

    // Sorting in-place
    public static void mergeSort(int[] arr, int start, int end) {
        if (start < end) {
            int mid = (start + end) / 2;
            mergeSort(arr, start, mid);
            mergeSort(arr, mid + 1, end);
            merge(arr, start, mid, end);
        }
    }

    private static void merge(int arr[], int start, int mid, int end) {
        int temp[] = new int[end - start + 1];
        int i = start, j = mid + 1, k = 0;

        while (i <= mid && j <= end) {
            if (arr[i] <= arr[j]) {
                temp[k++] = arr[i++];
            } else {
                temp[k++] = arr[j++];
            }
        }

        while (i <= mid) {
            temp[k++] = arr[i++];
        }

        while (j <= end) {
            temp[k++] = arr[j++];
        }

        for (i = start; i <= end; i++) {
            arr[i] = temp[i - start];
        }
    }

    // Not sorting in-place
    public static int[] mergeSort(int[] arr) {
        int n = arr.length;
        if (n == 1)
            return arr;

        int[] arr1 = Arrays.copyOfRange(arr, 0, n / 2);
        int[] arr2 = Arrays.copyOfRange(arr, n / 2, n);

        return merge(mergeSort(arr1), mergeSort(arr2));
    }

    private static int[] merge(int[] arr1, int[] arr2) {
        int n1 = arr1.length, n2 = arr2.length;
        int[] res = new int[n1 + n2];
        int i = 0, j = 0, k = 0;

        while (i < n1 && j < n2) {
            if (arr1[i] < arr2[j]) {
                res[k++] = arr1[i++];
            } else {
                res[k++] = arr2[j++];
            }
        }

        while (i < n1) {
            res[k++] = arr1[i++];
        }

        while (j < n2) {
            res[k++] = arr2[j++];
        }

        return res;
    }

    // --------------------------heap sort--------------------------
    // O(N*log(N))
    public static void heapSort(int[] arr) {
        buildHeap(arr);
        for (int i = arr.length - 1; i >= 0; i--) {
            swap(arr, i, 0);
            heapify(arr, i, 0);
        }
    }

    public static void heapify(int[] arr, int n, int i) {
        if (i >= n) {
            return;
        }

        int leftChildIdx = 2 * i + 1;
        int rightChildIdx = 2 * i + 2;
        int max = i;
        if (leftChildIdx < n && arr[leftChildIdx] > arr[max]) {
            max = leftChildIdx;
        }
        if (rightChildIdx < n && arr[rightChildIdx] > arr[max]) {
            max = rightChildIdx;
        }
        if (max != i) {
            swap(arr, max, i);
            heapify(arr, n, max);
        }
    }

    public static void buildHeap(int[] arr) {
        int n = arr.length;
        int parentIdx = (n - 1) / 2;
        for (int i = parentIdx; i >= 0; i--) {
            heapify(arr, n, i);
        }
    }

    // --------------------------heap sort--------------------------
    // O(N*log(N))
    public static void quickSort(int[] arr, int start, int end) {
        if (start < end) {
            int pivot = partition(arr, start, end);
            quickSort(arr, start, pivot - 1);
            quickSort(arr, pivot + 1, end);
        }
    }

    private static int partition(int[] arr, int start, int end) {
        int pivot = nums[end];
        int i = start - 1;
        for (int j = start; j < end; j++) {
            if (nums[j] < pivot) {
                swap(nums, ++i, j);
            }
        }
        swap(nums, i + 1, end);
        return i + 1;
    }

    private static int partition2(int[] arr, int start, int end) {
        int pivot = nums[start];
        int j = start + 1;
        for (int i = j; i <= end; i++) {
            if (nums[i] < pivot) {
                swap(nums, i, j++);
            }
        }
        swap(nums, j - 1, start);
        return j - 1;
    }

    private static void swap(int[] arr, int i, int j) {
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }
}
