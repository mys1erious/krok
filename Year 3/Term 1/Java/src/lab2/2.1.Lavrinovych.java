/*
1. Виконати наданий код:

import java.util.Scanner;
public class Joke
{ public static void main(String[] args)
{ Scanner scanner = new Scanner(System.in);
System.out.println("Enter your first name ");
String name = scanner.next();
String reverse = "";
for (int i = name.length()-2; i>=0; i--)
{ reverse += name.substring(i,i+1); }
reverse = name.substring(name.length()-1,name.length()).toUpperCase() + reverse.toLowerCase();
System.out.println("Then my name is "+reverse); } }

Розписати кожен рядочок.
 */

package lab2;

// importing Scanner
import java.util.Scanner;


// Making class 'Joke'
class Joke {
    // Making function 'main'
    public static void main(String[] args) {

        // Initializing variable 'scanner' to class Scanner
        Scanner scanner = new Scanner(System.in);

        // Printing a message to console that asks a user to enter his first name
        System.out.println("Enter your first name ");

        // Getting first element of user`s input and saving it to variable 'name'
        String name = scanner.next();

        // Creating variable 'reverse' with type String
        String reverse = "";

        // Creating a loop from (name length -1) to 0, with step -1
        for (int i = name.length()-2; i>=0; i--) {

            // Adding element at position i in 'name' to 'reverse'
            reverse += name.substring(i,i+1);
        }

        // Adding in front of lower case 'reverse' upper case substring from 'name' at positions (name.length()-1, name.length())
        reverse = name.substring(name.length()-1,name.length()).toUpperCase() + reverse.toLowerCase();

        // Printing result
        System.out.println("Then my name is "+reverse); } }