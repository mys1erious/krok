using System;

namespace prac1.PracExamples
{
    // Basic Delegate Example
    public class Ex2
    {
        private delegate void Print(int value);

        public static void Exec()
        {
            Print printDel = Utils.PrintNumber; // same as -> Print printDel = new Print(PrintNumber);
            printDel(100000);
            printDel(200);

            printDel = Utils.PrintMoney;
            printDel(10000);
            printDel(200);
        }
    }
}