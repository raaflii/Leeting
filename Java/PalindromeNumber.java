public class PalindromeNumber {
    public static boolean isPalindrome(int x) {
        if (x < 0 || (x % 10 == 0 && x != 0)) {
            return false;
        }

        int reversed = 0;
        int ori = x;

        while (x > 0) {
            int lastDigit = x % 10;

            reversed = reversed * 10 + lastDigit;
            x /= 10;
        }

        return reversed == ori;
    }

    public static void main(String[] args) {
        boolean a = isPalindrome(121);
        boolean b = isPalindrome(-121);
        boolean c = isPalindrome(10);

        System.out.println(a);
        System.out.println(b);
        System.out.println(c);
    }
}
