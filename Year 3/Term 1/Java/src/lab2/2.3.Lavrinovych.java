/*
Прочитати текстовий файл (кілька речень). Порахувати кількість речень, слів, букв, голосних, приголосних.
*/

package lab2;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;


class FileReader {
    public static void main(String[] args) throws FileNotFoundException {
        File file = new File(System.getProperty("user.dir")+"\\src\\lab2\\input_file.txt");
        Scanner scanner = new Scanner(file);

        String text = "";

        int numOfLinesToRead = 2;
        for (int i = 0; i < numOfLinesToRead; i++) {
            if(scanner.hasNextLine())
                text += scanner.nextLine();
        }

        String[] sentences = text.split("[!?.]+");
        System.out.println("Text:");
        for (String sentence : sentences) System.out.println(sentence);

        int sentencesSum = sentences.length;
        int wordsSum = text.split("\\s+").length;
        int lettersSum = lettersCalculator(text);

        int[] vowelsConsonantsSums = vowelsConsonantsCalculator(text);
        int vowelsSum = vowelsConsonantsSums[0];
        int consonantsSum = vowelsConsonantsSums[1];

        System.out.println("\nSentences: " + sentencesSum);
        System.out.println("Words: " + wordsSum);
        System.out.println("Letters: " + lettersSum);
        System.out.println("Vowels: " + vowelsSum);
        System.out.println("Consonants: " + consonantsSum);
    }

    static int lettersCalculator(String text) {
        int count = 0;
        for(int i = 0; i < text.length(); i++){
            if(Character.isLetter(text.charAt(i)))
                count++;
        }

        return count;
    }
    static int[] vowelsConsonantsCalculator(String text) {
        int vowelsCount = 0;
        int consonantsCount = 0;

        text = text.toLowerCase();
        for(int i = 0; i < text.length(); i++) {
            if(text.charAt(i) == 'a' || text.charAt(i) == 'e' || text.charAt(i) == 'i'
                                     || text.charAt(i) == 'o' || text.charAt(i) == 'u')
                vowelsCount++;
            else if(text.charAt(i) >= 'a' && text.charAt(i) <= 'z')
                consonantsCount++;
        }

        return new int[]{vowelsCount, consonantsCount};
    }

}