using System;

namespace prac1.PracExamples


{
    // Anonymous method (access to variable in outer function and Delegate as parameter)
    public class Ex14
    {
        private delegate void Print(int value);

        public static void Exec()
        {
            int i = 10;
            
            Print print = delegate(int val)
            {
                val += i;
                Console.WriteLine("Inside Anonymous method. Value: {0}", val);
            };
            
            PrintHelperMethod(print, 100);
        }

        private static void PrintHelperMethod(Print func, int val)
        {
            func(val);
        }

    }
}