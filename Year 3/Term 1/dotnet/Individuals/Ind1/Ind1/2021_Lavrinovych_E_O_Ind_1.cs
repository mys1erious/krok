/*
ННИИКТ, КН19, Лавринович Евгений
Индивидуальная работа № 1
Вариант 12

Задания: 1.17 м; 3.2 в; 3.6 е; 3.12 д; 3.29 е; 4.8; 4.97; 5.17; 6.28 а; 7.10; 8.4 в; 11.19 а; 11.44; 12.25 з;
 */

using System;
using System.Collections.Generic;
using System.Linq;

namespace Ind1


{
    internal class Program
    {
        public static void Main(string[] args)
        {
            Console.WriteLine("Tests: ");
            
            double task_1_17_m = Task_1_17_m(2, 3, 4);
            bool task_3_2_v = Task_3_2_v(false, true, false);
            bool task_3_6_e = Task_3_6_e(false, false, true);
            bool task_3_12_d = Task_3_12_d(2, 1);
            bool[] task_3_29_e = {Task_3_29_e(1, 1, 1), Task_3_29_e(1, 101, 1)};
            int task_4_8 = Task_4_8(1, 3000);
            String task_4_97 = Task_4_97(4);

            double[] task_5_17_x = new double[25];
            for (int i = 0; i < task_5_17_x.Length; i++)
                task_5_17_x[i] = i + 4;
            double[] task_5_17 = Task_5_17(task_5_17_x);
            
            int[] task_6_28_a = Task_6_28_a(123945678);
            List<int> task_7_10 = Task_7_10(8);
            int task_11_19_a = Task_11_19_a(new int[]{1, 2, 3, 4, 5});

            int[] task_11_44_array = new int[20];
            Random task_11_44_randNum = new Random();
            for (int i = 0; i < task_11_44_array.Length; i++)
                task_11_44_array[i] = task_11_44_randNum.Next(0, 10);
            int[] task_11_44 = Task_11_44(task_11_44_array);

            int[,] task_12_25_z = Task_12_25_z();
            
            
            Console.WriteLine("task_1_17_m: " + task_1_17_m);
            Console.WriteLine("task_3_2_v: " + task_3_2_v);
            Console.WriteLine("task_3_6_e: " + task_3_6_e);
            Console.WriteLine("task_3_12_d: " + task_3_12_d);
            Console.WriteLine("task_3_29_e: " + 
                              "input1: (1, 1, 1) -> " + task_3_29_e[0] + "; " +
                              "input2: (1, 101, 1) -> " + task_3_29_e[1]);
            Console.WriteLine("task_4_8: " + task_4_8);
            Console.WriteLine("task_4_97: " + task_4_97);
            Console.WriteLine("task_5_17: " + "[{0}]", string.Join(", ", task_5_17));
            Console.WriteLine("task_6_28_a: " + 
                              "indexFromStart: " + task_6_28_a[0] + "; " +
                              "indexFromEnd: " + task_6_28_a[1]);
            Console.WriteLine("task_7_10: " + "[{0}]", string.Join(", ", task_7_10));
            Console.WriteLine("task_8_4_v: "); Task_8_4_v();
            Console.WriteLine("task_11_19_a: " + task_11_19_a);
            Console.WriteLine("task_11_44: " + "[{0}]", string.Join(", ", task_11_44));
            
            Console.WriteLine("task_12_25_z: ");
            for (int i = 0; i < task_12_25_z.GetLength(0); i++)
            {
                for (int j = 0; j < task_12_25_z.GetLength(1); j++)
                {
                    Console.Write("{0} ", task_12_25_z[i, j]);
                }
                Console.Write(Environment.NewLine + Environment.NewLine);
            }
        }


        static double Task_1_17_m(double a, double b, double c)
        {
            // Задание: Записать по правилам изучаемого языка программирования выражение
            return Math.Sqrt(Math.Pow(a, 2) + Math.Pow(b, 2) - 2 * a * b * Math.Cos(c));
        }

        
        static bool Task_3_2_v(bool x, bool y, bool z)
        {
            // Задание: Вычислить значение логического выражения
            return x & z;
        }


        static bool Task_3_6_e(bool x, bool y, bool z)
        {
            // Задание: Вычислить значение логического выражения
            return x | !(y | z);
        }


        static bool Task_3_12_d(int x, int y)
        {
            // Задание: Вычислить значение логического выражения
            return (x * y != 0) || (y < x);
        }


        static bool Task_3_29_e(int x, int y, int z)
        {
            // Задание: Записать условие, которое является истинным, когда хотя бы одно из чисел x, y, z больше 100
            return (x | y | z) > 100;
        }


        static int Task_4_8(double km, double ft)
        {
            // Задание: Известно 2 расстояние в км. и футах (1фут = 0.45м) какое из расстояний меньше?
            
            double kmToMeters = km * 1000;
            double ftToMeters = ft * 0.45;
            
            // Возвращает 1 если km меньше(или km и ft одинаковы), 2 если ft меньше
            if (kmToMeters <= ftToMeters) return 1;
            return 2;
        }

        
        static String Task_4_97(int month)
        {
            // Задание: Составить программу, которая в зависимости от порядкового номера
            //          месяца выводит на экран время года, к которому относится месяц
            
            switch (month)
            {
                case 1:
                case 2:
                    return "Winter";
                case 3:
                case 4:
                case 5:
                    return "Spring";
                case 6:
                case 7:
                case 8:
                    return "Summer";
                case 9:
                case 10:
                case 11:
                    return "Autumn";
                case 12:
                    return "Winter";
            }
            return "";
        }


        static double[] Task_5_17(double[] x)
        {
            // Задание: Рассчитать значения y для значений x

            double[] y = new double[x.Length];
            double t;
            
            for (int i = 0; i < x.Length; i++)
            {
                t = x[i] + 2;
                y[i] = 2 * Math.Pow(t, 2) + 5.5 * t - 2;
            }

            return y;
        }


        static int[] Task_6_28_a(int x)
        {
            // Задание: Дано натуральное число, в котором все цифры различны,
            //          определить порядковый номер максимальной цифры(от начала и конца)

            var xStack = new Stack<int>();
            for (; x > 0; x /= 10)
                xStack.Push(x % 10);
            int[] xArray = xStack.ToArray();

            if (xArray.Length != xArray.Distinct().Count())
                throw new ArgumentException("Input value contains duplicates, its not allowed");

            int maxVal = xArray.Max();
            int idxFromStart = Array.IndexOf(xArray, maxVal);
            int idxFromEnd = xArray.Length - idxFromStart - 1;

            return new int[] { idxFromStart, idxFromEnd };
        }


        static List<int> Task_7_10(int n)
        {
            // Задание: Найти все двузначные числа, которые делятся на n
            //          или содержат цифру n

            var resultList = new List<int>();
            
            for (int val = 10; val < 100; val++)
            {
                if(val % n == 0 || val.ToString().Contains(n.ToString()))
                    resultList.Add(val);
            }

            return resultList;
        }


        static void Task_8_4_v()
        {
            // Задание: Напечатать числа в виде таблицы(треугольника)
            int val = 30;
            int spaces = 4;
            for (int i = 0; i < 5; i++)
            {
                String row = "";
                for (int j = 0; j < 5; j++)
                {
                    row += val + j - i + new String(' ', spaces);
                }
                Console.WriteLine(row.Remove((i+1)*2 + spaces*i));
            }
        }


        static int Task_11_19_a(int[] arr)
        {
            // Задание: Определить сумму всех элеменов массива
            return arr.Sum();
        }


        static int[] Task_11_44(int[] arr)
        {
            // Задание: Массив хранит информацию о количестве побед 20 команд
            //          определить номера команд, имеющих меньше 3 побед
            
            var result = new List<int>();

            for(int i = 0; i < arr.Length; i++)
            {
                if(arr[i] < 3) result.Add(i);
            }

            return result.ToArray();
        }


        static int[,] Task_12_25_z()
        {
            // Задание: Заполнить массив определенным образом
            int rowLen = 12;
            int colLen = 10;
            
            int[,] result = new int[rowLen, colLen];

            int startVal = 109;
            int colShift = 12;

            for (int i = 0; i < result.GetLength(0); i++)
            {
                for (int j = 0; j < result.GetLength(1); j++)
                {
                    result[i, j] = startVal + i - (j * colShift);
                }
            }

            return result;
        }
    }
}
