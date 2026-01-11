import java.util.Scanner;

class Solution {

    static boolean isSorted(int[] arr) {
        for (int i = 0; i < arr.length - 1; i++) {
            if (arr[i] > arr[i + 1]) {
                return false; 
            }
        }
        return true; 
    }

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        
        System.out.print("Enter the number of array: ");
        int n = input.nextInt();

        int[] arr = new int[n];
        System.out.println("Enter the number of array elements:");
        for (int i = 0; i < n; i++) {
            arr[i] = input.nextInt();
        }

        
        if (isSorted(arr)) {
            System.out.println("Array is sorted now ");
        } else {
            System.out.println("Array is NOT sorted");
        }
    }
}
