using System;

namespace prac1.PracExamples


{
    public class Utils
    {
        public static void PrintNumber(int num)
        {
            Console.WriteLine("Number: {0, -12:N0}", num);
        }
        public static void PrintMoney(int money)
        {
            Console.WriteLine("Money: {0:C}", money);
        }
        
        public static void PrintHexadecimal(int dec)
        {
            Console.WriteLine("Hexadecimal: {0:X}", dec);
        }
    }
}