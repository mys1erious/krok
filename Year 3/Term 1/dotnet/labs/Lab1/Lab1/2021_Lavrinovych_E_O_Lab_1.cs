using System;

namespace Lab1

{
    internal class Fraction
    {
        private int _numerator;
        private int _denominator;
       
        
        public static void Main(string[] args)
        {
            var fraction1 = new Fraction(-19, 20);
            var fraction2 = new Fraction("7/2");

            Console.WriteLine($"fraction1: {fraction1}");
            Console.WriteLine($"fraction2: {fraction2}\n");
            
            Console.WriteLine($"Addition =  {fraction1 + fraction2}");
            Console.WriteLine($"Subtraction = {fraction1 - fraction2}");
            Console.WriteLine($"Multiplication = {fraction1 * fraction2}");
            Console.WriteLine($"Division = {fraction1 / fraction2}");
            Console.WriteLine($"fraction1 Converted to double = {(double) fraction1}");
            
        }
        

        // Default Constructor
        public Fraction()
        {
        }
        
        
        // String-based Constructor 
        public Fraction(string fraction)
        {
            string[] splitFraction = fraction.Split('/');
            SetFraction(int.Parse(splitFraction[0]), int.Parse(splitFraction[1]));
        }

        
        // Constructor with parameters
        public Fraction(int numerator, int denominator)
        {
            SetFraction(numerator, denominator);
        }
        
        
        // Numerator Getter/Setter
        private int Numerator
        {
            get { return _numerator; }
            set { _numerator = value; }
        }

        
        // Denominator Getter/Setter
        private int Denominator
        {
            get { return _denominator; }
            set
            {
                if (value != 0)
                    _denominator = value;
                else
                    throw new ArgumentException("Denominator cant be 0");
            }
        }

        
        // Fraction Setter
        public void SetFraction(int numerator, int denominator)
        {
            Numerator = numerator;
            Denominator = denominator;
            FractionSimplification();
        }

        
        private void FractionSimplification()
        {
            if (Denominator < 0)
            {
                Numerator = -Numerator;
                Denominator = -Denominator;
            }

            int gcd = GCD(Numerator, Denominator);
            Numerator /= gcd;
            Denominator /= gcd;
        }


        private static int GCD(int a, int b)
        {
            if (a < 0)
                a = -a;
            if (b < 0)
                b = -b;
            
            while (a != 0 && b != 0)
            {
                if (a > b) 
                    a %= b;
                else 
                    b %= a;
            }

            return a | b;
        }

        
        // Addition
        public static Fraction operator + (Fraction a, Fraction b)
        {
            if (a.Denominator == b.Denominator)
                return new Fraction(a.Numerator + b.Numerator, a.Denominator);

            int numerator = (a.Numerator * b.Denominator) + (a.Denominator * b.Numerator);
            int denominator = a.Denominator * b.Denominator;
            return new Fraction(numerator, denominator);
        }


        public static Fraction operator - (Fraction a)
        {
            return new Fraction(-a.Numerator, a.Denominator);
        }

        
        // Subtraction
        public static Fraction operator - (Fraction a, Fraction b)
        {
            if (a.Denominator == b.Denominator)
                return new Fraction(a.Numerator - b.Numerator, a.Denominator);
            
            int numerator = (a.Numerator * b.Denominator) - (a.Denominator * b.Numerator);
            int denominator = a.Denominator * b.Denominator;
            return new Fraction(numerator, denominator);
        }
        

        // Multiplication
        public static Fraction operator * (Fraction a, Fraction b)
        {
            return new Fraction(a.Numerator * b.Numerator, a.Denominator * b.Denominator);
        }


        public static Fraction operator / (Fraction a, Fraction b)
        {
            return new Fraction(a.Numerator * b.Denominator, a.Denominator * b.Numerator);
        }


        public static implicit operator double (Fraction a)
        {
            return (double) a.Numerator / a.Denominator;
        }
        
        
         public override string ToString()
         {
             return $"{Numerator}/{Denominator}";
         }
    }
}