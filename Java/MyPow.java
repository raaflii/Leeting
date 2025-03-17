public class MyPow {
    public static double myPow(double x, long n) {
        if (n < 0) {
            return 1 / myPow(x, -n);
        }
    
        if (n == 0) {
            return 1.0;
        }
    
        double half = myPow(x, n / 2);
        
        if (n % 2 == 0) {
            return half * half;  
        } else {
            return half * half * x;
        }
    }

    public static void main(String[] args) {
        double a = myPow(1.00000, -2147483648);
        System.out.println(a);
    }
}