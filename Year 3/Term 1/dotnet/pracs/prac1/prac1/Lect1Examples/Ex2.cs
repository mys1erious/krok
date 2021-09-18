using System;


namespace prac1.Lect1Examples
{
    // Delegates
    public class Ex2
    {
        delegate int Operation(int x, int y);

        public static void Exec()
        {
            Operation del = new Operation(Add); // why use 'new Operation(Add)' if can just write del = Add; ?
            int result = del(4, 5); // Difference with .Invoke() and without ?
            Console.WriteLine(result);

            del = Multiply;
            result = del(3, 8);
            Console.WriteLine(result);
        }

        private static int Add(int x, int y)
        {
            return x + y;
        }
        
        private static int Multiply(int x, int y)
        {
            return x * y;
        }
    }
}