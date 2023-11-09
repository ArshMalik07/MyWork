import java.util.*;

class RomanToInt {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String romanNumeral = sc.nextLine(); 
        int result = romanToInt(romanNumeral);
        System.out.println("Integer value: " + result);
        sc.close();
    }

    public static int romanToInt(String s) {
        Map<Character, Integer> m = new HashMap<>();
        m.put('I', 1);
        m.put('V', 5);
        m.put('X', 10);
        m.put('L', 50);
        m.put('C', 100);
        m.put('D', 500);
        m.put('M', 1000);
        int ans = 0;

        for (int i = 0; i < s.length(); i++) {
            if (i < s.length() - 1 && m.get(s.charAt(i)) < m.get(s.charAt(i + 1))) {
                ans = ans - m.get(s.charAt(i));
            } else {
                ans = ans + m.get(s.charAt(i));
            }
        }
        return ans;
    }
}
