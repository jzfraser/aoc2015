package Java;

import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Arrays;

class Dimensions {
    public int l;
    public int w;
    public int h;

    Dimensions() {
        l = 0;
        w = 0;
        h = 0;
    }

    Dimensions(int length, int width, int height) {
        l = length;
        w = width;
        h = height;
    }

    @Override
    public String toString() {
        return String.format("%dx%dx%d", l, w, h);
    }
}

class Day2 {
    public static void main(String[] args) {
        try {
            ArrayList<String> input = Helpers.readFile("./inputs/day2input.txt");
            Dimensions[] dims = processDims(input);
            int[] totals = getTotalPaperAndRibbon(dims);
            System.out.printf("Total WP: %d\nTotal Ribbon: %d\n", totals[0], totals[1]);
        } catch (FileNotFoundException e) {
        }
    }

    public static Dimensions[] processDims(ArrayList<String> input) {
        Dimensions[] allDims = new Dimensions[input.size()];
        int end = 0;
        for (int i = 0; i < input.size(); i++) {
            Dimensions newDims = getDimensions(input.get(i)); 
            // System.out.println(newDims);
            allDims[end] = newDims;
            end++;
        }
        return allDims;
    }

    public static Dimensions getDimensions(String dims) {
        String[] parts = dims.split("x");
        int length = Integer.parseInt(parts[0]);
        int width = Integer.parseInt(parts[1]);
        int height = Integer.parseInt(parts[2]);
        Dimensions newDims = new Dimensions(length, width, height);
        return newDims;
    }

    public static int[] getTotalPaperAndRibbon(Dimensions[] allDims) {
        int totalWP = 0;
        int totalRibbon = 0;
        for (int i = 0; i < allDims.length; i++) {
            Dimensions dims = allDims[i];
            totalWP += getWrappingPaper(dims);
            totalRibbon += getRibbon(dims);
        }
        int[] ans = {totalWP, totalRibbon};
        return ans;
    }

    public static int getWrappingPaper(Dimensions dims) {
        int s1 = dims.l * dims.w;
        int s2 = dims.w * dims.h;
        int s3 = dims.h * dims.l;
        int smallest = Math.min(s1, Math.min(s2, s3));
        return 2 * s1 + 2 * s2 + 2 * s3 + smallest;
    }

    public static int getRibbon(Dimensions dims) {
        int[] lwh = {dims.l, dims.w, dims.h};
        Arrays.sort(lwh);
        int x = lwh[0];
        int y = lwh[1];
        int len1 = 2 * x + 2 * y;
        int len2 = dims.l * dims.w * dims.h;
        return len1 + len2;
    }
}