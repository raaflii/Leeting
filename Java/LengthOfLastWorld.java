public class LengthOfLastWorld {
    public static int lengthOfLastWord(String s) {
        s = s.trim();
        int i = s.lastIndexOf(" ");
        return (s.substring(i + 1, s.length())).length();
    }
    public static void main(String[] args) {
        int a = lengthOfLastWord("luffy is still joyboy");
        System.out.println(a);
    }
    
}