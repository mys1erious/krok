/*
Текстовий файл містить: Прізвище, Ім'я, Посада, Оклад (int), Кількість дітей (int, 0-7). Від 10-ти записів.
Створити методи:

Прочитати текстовий файл у 2 масиви відповідного типу
Розрахувати податки залежно від кількості дітей (3 варіанти-довільно) - записати у float array
Пошук по символу/слову (String array)
Фільтр, max, min, avg для int, float arrays.
Виведення інформації на екран - з усіх 3-х масивів  синхронно.
*/


package lab3;

import java.io.*;
import java.util.Scanner;


class FileInfo {
    public static void main(String[] args) throws IOException {
        String userDir = System.getProperty("user.dir");
        String fileName = "data.txt";
        String filePath = userDir+"\\src\\lab3\\"+fileName;

        int numOfStrFields = 3;
        int numOfIntFields = 2;


        // // Reading a text file in 2 arrays of the corresponding types
        Object[] tempArray = ReadFileDataInTwoArrays(filePath,numOfStrFields, numOfIntFields);
        String[][] strArray = (String[][]) tempArray[0];
        int[][] intArray = (int[][]) tempArray[1];
        tempArray = null;


        // Calculating taxes depending on the number of children
        float[] taxesArray = TaxesPerChild(intArray);


        // Creating a single table(array) from 3 arrays (for convenience)
        Object[][] table = CreateTable(strArray, intArray, taxesArray);


        // Search by a Surname
        String Surname = "Surname3";
        int surnameIndex = SearchBySurname(strArray, Surname);

        if(surnameIndex != -1){
            Object[] row = GetRowAtIndex(table, surnameIndex);
            System.out.println("Row with Surname: "+Surname);
            PrintRowTemplate(row);
        } else {
            System.out.println("Row with Surname '"+Surname+"' doesnt exist");
        }


        // Filters, min, avg, max
        float[] minMaxAvgTaxesArray = MinAvgMaxOfArray(taxesArray);
        float minTaxes = minMaxAvgTaxesArray[0];
        float avgTaxes = minMaxAvgTaxesArray[1];
        float maxTaxes = minMaxAvgTaxesArray[2];

        System.out.println("\nMin, Avg, Max of taxes array: " +
                "\nMin: "+minTaxes+
                "\nAvg: "+avgTaxes+
                "\nMax: "+maxTaxes);


        // Printing arrays
        System.out.println("\nTable of 3 arrays: ");
        PrintTable(table);
    }


    // Read a text file in 2 arrays of the corresponding types
    public static Object[] ReadFileDataInTwoArrays(String filePath, int numOfStrFields, int numOfIntFields)
            throws FileNotFoundException {

        int fileLenByLines = GetFileLenByLines(filePath);

        String[][] strArray = new String[fileLenByLines][numOfStrFields];
        int[][] intArray = new int[fileLenByLines][numOfIntFields];

        File file = new File(filePath);
        Scanner scanner = new Scanner(file);

        for (int i = 0; i < fileLenByLines; i++) {
            if(scanner.hasNextLine()){
                String[] text = scanner.nextLine().split(",");
                for (int j = 0; j < text.length; j++){
                    if (j < numOfStrFields)
                        strArray[i][j] = text[j];
                    else
                        intArray[i][j-numOfStrFields] = Integer.parseInt(text[j]);
                }
            }
            else
                break;
        }

        return new Object[]{strArray, intArray};
    }


    private static int GetFileLenByLines(String fileName){
        try (
                FileReader input = new FileReader(fileName);
                LineNumberReader count = new LineNumberReader(input);
        ) {
            count.skip(Long.MAX_VALUE);
            return count.getLineNumber();
        } catch (IOException e) {
            e.printStackTrace();
        }
        return -1;
    }


    // Calculate taxes depending on the number of children
    public static float[] TaxesPerChild(int[][] arr) {
        int arrLen = arr.length;
        float[] result = new float[arrLen];

        for (int i = 0; i < arrLen; i++) {
            result[i] = arr[i][0] / arr[i][1];
        }

        return result;
    }


    // Search by a surname
    public static int SearchBySurname(String[][] arr, String Surname) {
        int arrLen = arr.length;

        for (int i = 0; i < arrLen; i++) {
            if (arr[i][1].equals(Surname))
                return i;
        }

        return -1;
    }


    // Filters, min, avg, max
    // return: result
    // where result[0] -> Min value of an array
    //       result[1] -> Avg value of an array
    //       result[2] -> Max value of an array
    public static float[] MinAvgMaxOfArray(float[] arr){
        float[] result = new float[3];

        result[0] = arrayMin(arr);
        result[2] = arrayMax(arr);
        result[1] = arrayAvg(result[0], result[2]);

        return result;
    }


    private static float arrayMax(float[] arr) {
        float max = Float.NEGATIVE_INFINITY;

        for (float cur : arr)
            max = Math.max(max, cur);

        return max;
    }


    private static float arrayMin(float[] arr) {
        float min = Float.POSITIVE_INFINITY;

        for (float cur : arr)
            min = Math.min(min, cur);

        return min;
    }

    private static float arrayAvg(float min, float max){
        return (min+max)/2;
    }


    // Prints table
    public static void PrintTable(Object[][] table){
        for (final Object[] row : table) {
            PrintRowTemplate(row);
        }
    }


    private static void PrintRowTemplate(Object[] row){
        System.out.format("%-15s%-15s%-15s%-15s%-15s%-15s%n", row);
    }


    // Creates Table from 3 arrays
    private static Object[][] CreateTable(String[][] strArray, int[][] intArray, float[] taxArray){
        int arrLen = strArray.length;
        final Object[][] table = new String[arrLen+1][];

        // Column names
        table[0] = new String[] { "Name", "Surname", "Position", "Salary", "Children", "TaxPerChild" };

        for (int i = 0; i < arrLen; i++) {
            table[i+1] = new String[] {strArray[i][0], strArray[i][1], strArray[i][2],
                    String.valueOf(intArray[i][0]), String.valueOf(intArray[i][1]),
                    String.valueOf(taxArray[i])};
        }

        return table;
    }


    private static String[] GetRowAtIndex(Object[][] table, int index){
        int len = table[0].length;
        String[] result = new String[len];

        for (int i = 0; i < len; i++) {
            result[i] = (String) table[index+1][i];
        }

        return result;
    }
}
