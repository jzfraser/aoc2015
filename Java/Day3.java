package Java;

import java.io.FileNotFoundException;
import java.util.HashMap;

class Coord {
    public int x;
    public int y;

    public Coord(int x, int y) {
        this.x = x;
        this.y = y;
    }

    @Override
    public int hashCode() {
        final int prime = 31;
        int result = 1;
        result = prime * result + x;
        result = prime * result + y;
        return result;
    }

    @Override
    public boolean equals(Object obj) {
        if (this == obj)
            return true;
        if (obj == null)
            return false;
        if (getClass() != obj.getClass())
            return false;
        Coord other = (Coord) obj;
        if (x != other.x)
            return false;
        if (y != other.y)
            return false;
        return true;
    }

    @Override
    public String toString() {
        return String.format("(%d, %d)", x, y);
    }
}

public class Day3 {
    public static void main(String[] args) {
        try {
            String directns = Helpers.readFile("./inputs/day3input.txt").get(0);
            part1(directns);
            part2(directns);
        } catch (FileNotFoundException e) {
        }
    }

    public static void part1(String directns) {
        HashMap<Coord, Integer> houses = new HashMap<Coord, Integer>();
        houses.put(new Coord(0, 0), 1);
        int x = 0;
        int y = 0;
        for (int i = 0; i < directns.length(); i++) {
            char d = directns.charAt(i);
            if (d == '^') {
                y += 1;
            } else if (d == '>') {
                x += 1;
            } else if (d == 'v') {
                y -= 1;
            } else if (d == '<') {
                x -= 1;
            }
            Coord current = new Coord(x, y);
            Integer inserted = houses.putIfAbsent(current, 1);
            if (inserted != null) {
                houses.put(current, inserted + 1);
            }
        }
        System.out.println(houses.size());
    }

    public static void part2(String directns) {
        HashMap<Coord, Integer> houses = new HashMap<Coord, Integer>();
        houses.put(new Coord(0, 0), 2);
        int x = 0;
        int y = 0;
        int x2 = 0;
        int y2 = 0;
        boolean santasTurn = true;
        for (int i = 0; i < directns.length(); i++) {
            char d = directns.charAt(i);
            if (d == '^') {
                if (santasTurn) {
                    y += 1;
                } else {
                    y2 += 1;
                }
            } else if (d == '>') {
                if (santasTurn) {
                    x += 1;
                } else {
                    x2 += 1;
                }
            } else if (d == 'v') {
                if (santasTurn) {
                    y -= 1;
                } else {
                    y2 -= 1;
                }
            } else if (d == '<') {
                if (santasTurn) {
                    x -= 1;
                } else {
                    x2 -= 1;
                }
            }
            Coord current;
            if (santasTurn) {
                current = new Coord(x, y);
            } else {
                current = new Coord(x2, y2);
            }
            Integer inserted = houses.putIfAbsent(current, 1);
            if (inserted != null) {
                houses.put(current, inserted + 1);
            }
            santasTurn = !santasTurn;
        }
    System.out.println(houses.size());
    }
}