using System;
using System.Runtime.CompilerServices;

namespace Ind2

{
    public static class Program
    {
        public static void Main(string[] args)
        {
            var v1 = new Vector(new double[]{1, 2, 3});
            var v2 = new Vector(new double[]{4, 5, 6});
            
            int c = 2;
            int index = 1;
            int val = 20;

            Console.WriteLine($"v1 = {v1}");
            Console.WriteLine($"v2 = {v2}");
            
            
            // Operations (addition, subtraction, const * vector, scalar product
            Console.WriteLine($"\nv1 + v2 = {v1 + v2}");
            Console.WriteLine($"v1 - v2 = {v1 - v2}");
            Console.WriteLine($"const({c}) * v2 = {c * v2}");
            Console.WriteLine($"v1 * v2(Scalar) = {v1 * v2}");
            
            
            // Converting vector to a string
            string strV1 = v1.ToString();

            
            // Getting value and settings new value for a vector
            Console.WriteLine($"\nElement at index {index} in v2 = {v2[index]}");
            v2[index] = val;
            Console.WriteLine($"Element after replacement at index {index} in v2 = {v2[index]}");
            Console.WriteLine($"v2 = {v2}");
        }
    }
    
    public class Vector
    {
        public Vector()
        {
        }
        
        
        public Vector(int N)
        {
            if (N < 0)
                throw new ArgumentException("Vector len cant be < 0");

            try
            {
                Data = new double[N];
            }
            catch (Exception e)
            {
                Console.WriteLine(e);
                throw;
            }
                
        }
        
        
        public Vector(double[] d)
        {
            try
            {
                Data = d;
            }
            catch (Exception e)
            {
                Console.WriteLine(e);
                throw;
            }
        }
        
        
        private double[] Data { get; }


        // Addition
        public static Vector operator + (Vector v1,Vector v2)
        {

            if (v1.Length != v2.Length)
            {
                throw new Exception("Lenght of the vectors must be the same to add them");
            }

            int len = v1.Length;
            Vector v = new Vector(len);

            for(int i = 0; i < len; i++)
            {
                v[i] = v1[i] + v2[i];
            }

            return v;
        }

        
        // Subtraction
        public static Vector operator - (Vector v1, Vector v2)
        {
            if (v1.Length != v2.Length)
            {
                throw new Exception("Lenght of the vectors must be the same to subtract one from another");
            }

            int len = v1.Length;
            Vector v = new Vector(len);

            for(int i = 0; i < len; i++)
            {
                v[i] = v1[i] - v2[i];
            }

            return v;
        }
        

        // Scalar product
        public static double operator * (Vector v1,Vector v2)
        {
            if (v1.Length != v2.Length)
            {
                throw new Exception("Lenght of the vectors must be the same to calculate Scalar product");
            }
            int len = v1.Length;
            
            double scalar = 0;
            
            for (int i = 0; i < len; i++)
            {
                scalar += v1[i] * v2[i];
            }
            return scalar;
        }
        
        
        // Multiply by constant
        public static Vector operator * (double c, Vector v)
        {

            for (int i = 0; i < v.Length; i++)
            {
                v[i] *= c;
            }
            return v;
        }
        
        
        public static Vector operator * (Vector v, double c)
        {

            for (int i = 0; i < v.Length; i++)
            {
                v[i] *= c;
            }
            return v;
        }


        // String representation
        public override string ToString()
        {
            String result = "[";
            for (int i = 0; i < this.Length; i++)
                result += $"{this[i]} ";

            result = result.TrimEnd(',', ' ');
            result += ']';
            
            return result;
        }
        
        
        public int Count { get; set; }
        
        
        public int Length
        {
            get { return Data.Length; }
            set {}
        }
        
        
        // Getter and Setter of vector
        public double this[int index]
        {
            get
            {
                return Data[index];
            }

            set
            {
                Data[index] = value;
            }
        }
    }
}