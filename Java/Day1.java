package Java;

import java.io.FileNotFoundException;
import java.util.ArrayList;

class Day1 {
    public static void main(String[] args) {
        try {
            ArrayList<String> data = Helpers.readFile("./inputs/day1input.txt");
            String input = data.get(0);
            System.out.println(part1(input));
            System.out.println(part2(input));

        } catch (FileNotFoundException e) {
        }
    }

    public static int part1(String input) {
        int ans = 0;
        for (int i = 0; i < input.length(); i++) {
            char c = input.charAt(i);
            if (c == '(') {
                ans++;
            } else if (c == ')') {
                ans--;
            }
        }
        return ans;
    }

    public static int part2(String input) {
        int ans = 0;
        for (int i = 0; i < input.length(); i++) {
            char c = input.charAt(i);
            if (c == '(') {
                ans++;
            } else if (c == ')') {
                ans--;
            }
            if (ans < 0) {
                return i + 1;
            }
        }
        return ans;
    }
}
