using System;

namespace prac1.PracExamples


{
    public class Ex5
    {
        // Example of Delegate as parameter
        private delegate void Print(int value);

        public static void Exec()
        {
            PrintHelper(Utils.PrintNumber, 10000);
            PrintHelper(Utils.PrintMoney, 10000);
        }

        private static void PrintHelper(Print delegateFunc, int numToPrint)
        {
            delegateFunc(numToPrint);
        }
    }
}