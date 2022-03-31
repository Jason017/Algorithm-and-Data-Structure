import java.util.Arrays;

/**
 * All sorting algorithms to sort int array into an ascending order
 * 
 * @author Bo Guan
 *
 */
public class SortAlgorithm {

    public static void main(String[] args) {
        int[] arr = { 4, 10, 3, 5, 1, 2 };
    }

    public static void swap(int[] arr, int i, int j) {
        int tmp = arr[i];
        arr[i] = arr[j];
        arr[j] = tmp;
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

    public static int[] arrayAppend(int[] arr, int value) {
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

    public static void merge(int arr[], int start, int mid, int end) {
        int temp[] = new int[end - start + 1];
        int i = start, j = mid + 1, k = 0;

        while (i <= mid && j <= end) {
            if (arr[i] <= arr[j]) {
                temp[k] = arr[i];
                k += 1;
                i += 1;
            } else {
                temp[k] = arr[j];
                k += 1;
                j += 1;
            }
        }

        while (i <= mid) {
            temp[k] = arr[i];
            k += 1;
            i += 1;
        }

        while (j <= end) {
            temp[k] = arr[j];
            k += 1;
            j += 1;
        }

        for (i = start; i <= end; i += 1) {
            arr[i] = temp[i - start];
        }
    }

    public static void mergeSort(int[] arr, int start, int end) {
        if (start < end) {
            int mid = (start + end) / 2;
            mergeSort(arr, start, mid);
            mergeSort(arr, mid + 1, end);
            merge(arr, start, mid, end);
        }
    }

    // --------------------------heap sort--------------------------
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

    public static void heapSort(int[] arr) {
        int n = arr.length;
        buildHeap(arr);
        for (int i = n - 1; i >= 0; i--) {
            swap(arr, i, 0);
            heapify(arr, i, 0);
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
    public static void insertionSort(int[] arr) {
        int n = arr.length;
        for (int i = 1; i < n; i++) {
            int key = arr[i];
            int j = i - 1;
            while ((j >= 0) && (key < arr[j])) {
                arr[j + 1] = arr[j];
                j--;
            }
            arr[j + 1] = key;
        }
    }
}
