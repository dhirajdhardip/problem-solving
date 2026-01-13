import java.util.Scanner;

public class RemoveDuplicates {
    public static void main(String[] args) {

        Scanner input = new Scanner(System.in);

        System.out.print("Enter  the number of elements: ");
        int num = input.nextInt();

        int[] arr = new int[num];
        System.out.println("Enter the sorted elements:");
        for (int i = 0; i < num; i++) {
            arr[i] = sc.nextInt();
        }

        int[] temp = new int[num];
        int j = 0;

        temp[j++] = arr[0];

        for (int i = 1; i < num; i++) {
            if (arr[i] != arr[i - 1]) {
                temp[j] = arr[i];
                j++;
            }
        }

        System.out.println("Array after removing duplicates:");
        for (int i = 0; i < j; i++) {
            System.out.print(temp[i] + " ");
        }
    }
}
