
public class Armstrong {

    public static void main(String[] args) {
        int num = 1000;
        int count = 0;
        for(int i = 10; i <= num; i++) {
            if (isArmstrong(i)) {
                count++;
            }
        }
        System.out.println("The number of Armstrong numbers between 10 and " + num + " is: " + count);


    }

    public static boolean isArmstrong(int  num) {
        int result = 0;
        int originalNum = num;
        int remainder;

        while (originalNum != 0) {
            remainder = originalNum % 10;
            result += remainder * remainder * remainder;
            originalNum /= 10;
        }

        return result == num;
    }

}