package lab0;


import java.util.Scanner;

import java.time.LocalDate;
import java.time.Period;


// Displays number of years, months, days that have passed since given birthdate to the current date
public class Lab0 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Enter your birthdate in format: year month day");
        int year, month, day;

        try {
            year = scanner.nextInt();
            month = scanner.nextInt();
            day = scanner.nextInt();
        } catch (Exception e) {
            throw new IllegalArgumentException("Wrong input format");
        }

        LocalDate birthdate = LocalDate.of(year, month, day);
        LocalDate currentDate = LocalDate.now();
        Period period = Period.between(birthdate, currentDate);

        int[] age = new int[]{period.getYears(), period.getMonths(), period.getDays()};

        System.out.println("Number of years, months, days that have passed since given birthdate to the current date: " +
                "\nyears: " + age[0] +
                "\nmonths: " + age[1] +
                "\ndays: " + age[2]);
    }
}
