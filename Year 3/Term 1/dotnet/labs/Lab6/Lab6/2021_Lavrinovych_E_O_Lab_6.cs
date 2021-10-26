using System;

using System.Linq;

namespace Lab6
{
    internal static class Lab6
    {
        public static void Main(string[] args)
        {
            Random randNum = new Random();
            int[] array = Enumerable
                .Repeat(0, 20)
                .Select(i => randNum.Next(0, 100))
                .ToArray();
            
            Console.WriteLine($"Array: [{string.Join(", ", array)}]");
            Console.WriteLine($"Array of Even numbers: [{string.Join(", ", GetEvenNumbers(array))}]");
            Console.WriteLine($"Array of Odd numbers: [{string.Join(", ", GetOddNumbers(array))}]");
            Console.WriteLine($"Array of numbers that end with 5: " +
                              $"[{string.Join(", ", GetNumbersWhichEndWith5(array))}]");
        }
        
        
        public static int[] GetEvenNumbers(int[] array)
        {
            var result = (
                from num in array
                where num % 2 == 0
                select num).ToArray();
            
            return result;
        }
        
        
        public static int[] GetOddNumbers(int[] array)
        {
            var result = (
                from num in array
                where num % 2 != 0
                select num).ToArray();
            
            return result;
        }


        public static int[] GetNumbersWhichEndWith5(int[] array)
        {
            var result = (
                from num in array
                where num % 10 == 5
                select num).ToArray();
            
            return result;
        }
    }
}