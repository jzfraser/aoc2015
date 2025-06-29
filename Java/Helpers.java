package Java;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Scanner;

public class Helpers {
    public static ArrayList<String> readFile(String filepath) throws FileNotFoundException {
        try {
            File input = new File(filepath);
            Scanner s = new Scanner(input);
            ArrayList<String> lines = new ArrayList<String>();
            while (s.hasNextLine()) {
                lines.add(s.nextLine());
            }
            s.close();
            return lines;
        } catch (FileNotFoundException e) {
            System.out.println("File could not be found");
            throw e;
        }
    }
}
