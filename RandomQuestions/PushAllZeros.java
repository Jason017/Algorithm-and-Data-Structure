// package Example;

import java.util.Arrays;

public class PushAllZeros {
    public static void main(String[] args) {
        int[] num = new int[]{1, 0, 2, 0, 3};
        int[] num1 = new int[]{1, 0, 2, 0, 4, 0, 6, 7, 0, 2, 1, 8, 0, 3};
        int[] newNum = pushZeros1(num, 0, num.length - 1);
        int[] newNum1 = pushZeros2(num1);
        System.out.println(Arrays.toString(newNum));
        System.out.println(Arrays.toString(newNum1));
    }

    private static int[] pushZeros1(int[] arr, int l, int r) {
        int end = r;
        for (int i = r; i > l; --i)
            if (arr[i] == 0) {
                swap(arr, i, end);
                --end;
            }
        return arr;
    }

    private static void swap(int[] arr, int i, int j) {
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }

    private static int[] pushZeros2(int[] arr) {
        int[] newArr = new int[arr.length];
        int count = 0;
        for (int i = 0; i < arr.length; i++)
            if (arr[i] != 0
                newArr[count++] += arr[i];
        return newArr;
    }

    private static void pushZeros3(int arr[], int n) {
        int count = 0;
        for (int i = 0; i < n; i++)
            if (arr[i] != 0)
                arr[count++] = arr[i];
        while (count < n)
            arr[count++] = 0;
    }
}