using System;


namespace Lab3
{
    // Tasks 1, 3, 5, 6
    public static class Binary
    {
        public static void Main(string[] args)
        {
            int numDec = 22;
            int[] numBin = DecToBin(numDec);
            Console.WriteLine($"Task_3_1:\n" +
                              $"Decimal {numDec} = Binary " + BinaryToString(numBin));
            
            int n = 9;
            int i = 1;
            Console.WriteLine($"\nTask_3_3:\n" +
                              $"for n = {n}, i = {i}; result = {Task_3_3(n, i)}");

            Console.WriteLine($"\nTask_3_5:\n" +
                              $"int {BinaryToString(numBin)} - {Task_3_5(numBin)} 1s");


            int a = 8;
            int b = 7;
            (int, int) task_3_6 = Task_3_6(a, b);
            
            Console.WriteLine($"\nTask_3_6:\n" +
                              $"for a = {a}, b = {b}; new a = {task_3_6.Item1}, b = {task_3_6.Item2}");

        
    }
        
        
        // Task_3_1
        // Transforms an unsigned integer to binary
        public static int[] DecToBin(int decNum)
        {
            int len = BinaryValueLengthBasedOnDecimal(decNum);

            int[] binNum = new int[len];
            
            int index = 0;
            int i;
            for (i = 1 << len-1; i > 0; i /= 2)
            {
                if ((decNum & i) != 0)
                    binNum[index] = 1;
                else
                    binNum[index] = 0;
                index++;
            }

            return binNum;
        }


        public static int BinToDec(int[] binNum)
        {
            Array.Reverse(binNum);
            
            int decNum = 0;
            for (int i = 0; i < binNum.Length; i++)
            {
                if (binNum[i] == 1)
                {
                    if (i == 0)
                        decNum += 1;
                    else
                        decNum += (int)Math.Pow(2, i);
                }
            }

            return decNum;
        }
        
        
        // Task_3_3
        // Changes i`s bit in n to 1
        public static int Task_3_3(int n, int i)
        {

            int[] binNum = DecToBin(n);
            binNum[i+1] = 1;

            int result = BinToDec(binNum);

            return result;
        }
        
        
        // Task_3_5
        // Calculate 1s in a binary number
        public static int Task_3_5(int[] binNum)
        {
            int result = 0;
            foreach (var bit in binNum)
            {
                if (bit == 1)
                    result += 1;
            }
            
            return result;
        }
        
        
        // Task_3_6
        // Swap 2 integers using only bit operations
        public static (int, int) Task_3_6(int a, int b)
        {
            a ^= b;
            b ^= a;
            a ^= b;
            return (a, b);
        }
        
        
        public static string BinaryToString(int[] binNum)
        {
            return string.Join("", binNum);
        }
        
        public static int BinaryValueLengthBasedOnDecimal(int val)
        {
            return (int) Math.Log(val, 2) + 1;
        }
    }
}


// *
// * *
// ****