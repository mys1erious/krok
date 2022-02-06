/*
2. Реалізувати найпростіший калькулятор, який приймає у циклі введення послідосності число/операція (+, -, *, /, ^.)
Завершення вводу - символ, відмінний від числа та операції.
 */

package lab2;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;


class Calculator {
    public static void main(String[] args) {
        System.out.println("Enter a sequence of numbers and operators(+, -, *, /, ^):");

        String[] allowedOperators = new String[]{"+", "-", "*", "/", "^"};
        String exitOperator = "=";

        List<String> operators = new ArrayList<String>();
        List<Double> values = new ArrayList<Double>();

        Scanner scanner = new Scanner(System.in);

        // Loop that takes a sequence of numbers and operators
        while(true) {
            if(scanner.hasNext()) {
                String currentValue = scanner.next();

                if(currentValue.equals(exitOperator))
                    break;
                else if (Arrays.asList(allowedOperators).contains(currentValue))
                    operators.add(currentValue);

                try {
                    values.add(Double.parseDouble(currentValue));
                } catch(NumberFormatException ignored) {
                    ;
                }
            }
        }

        if(operators.toArray().length+1 != values.toArray().length)
            throw new IllegalArgumentException("Wrong input");

        // Simple-calculator logic
        double result = values.get(0);
        for (int i = 1; i < values.toArray().length; i++) {
            switch (operators.get(i - 1)) {
                case "+" -> result += values.get(i);
                case "-" -> result -= values.get(i);
                case "*" -> result *= values.get(i);
                case "/" -> result /= values.get(i);
                case "^" -> result = Math.pow(result, values.get(i));
            }
        }

        System.out.println(result);
    }
}
