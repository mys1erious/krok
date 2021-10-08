using System;
using System.Collections.Generic;
using System.Configuration;


namespace Lab2
{
    
    public class Polynomial
    {
        public static void Main(string[] args)
        {
            var poly = new Polynomial(new double[] { 3, 0, -5, 2, 1 });

            int val = 2;
            var polyValue = poly.Calculate(val);
            
            var polyDerivative = poly.Derivative();
            
            var polyCopy = poly.Copy();
            var polyRef = poly;
            
            Console.WriteLine($"Polynomial: {poly}");
            Console.WriteLine($"Polynomial value for x={val}: {polyValue}");
            Console.WriteLine($"Polynomial Derivative: {polyDerivative}");
            
            Console.WriteLine($"\nCopy of poly: {polyCopy}");
            Console.WriteLine($"References equality with Copy method: " +
                              $"{object.ReferenceEquals(poly, polyCopy)}");
            Console.WriteLine($"References equality without Copy method: " +
                              $"{object.ReferenceEquals(poly, polyRef)}");
        }


        public Polynomial(double[] coefficients)
        {
            Coefficients = coefficients;
        }


        public double[] Coefficients { get; set; }


        // Value calculation
        public double Calculate(double value)
        {
            double result = 0;
            
            foreach (var coeff in Coefficients)
                result = result * value + coeff;

            return result;
        }
        
        
        // Derivative
        public Polynomial Derivative()
        {
            List<double> derivedCoeffs = new List<double>();
            int exponent = Coefficients.Length - 1;

            for (int i = 0; i < Coefficients.Length - 1; i++)
            {
                derivedCoeffs.Add(Coefficients[i] * exponent);
                exponent -= 1;
            }

            return new Polynomial(derivedCoeffs.ToArray());
        }

        
        // Copy of Polynomial
        public Polynomial Copy()
        {
            Polynomial other = (Polynomial)this.MemberwiseClone();
            Coefficients.CopyTo(other.Coefficients, 0);

            return other;
        }


        // String representation
        public override string ToString()
        {
            String XDegree(int deg)
            {
                String res;

                switch (deg)
                {
                    case 0:
                        res = "";
                        break;
                    case 1:
                        res = "x";
                        break;
                    default:
                        res = $"X^{deg}";
                        break;
                }

                return res;
            }

            int degree = Coefficients.Length-1;
            String result = "";
            
            for (int i = 0; i < degree + 1; i++)
            {
                double coeff = Coefficients[i];

                if (Math.Abs((int)coeff) == 1 && i < degree)
                    result += $"{(coeff > 0 ? "+" : "-")}{XDegree(degree-i)}";
                else if (coeff != 0)
                    result += $"{(coeff > 0 ? "+" : "")}{coeff}{XDegree(degree-i)}";
            }
            
            return result.Trim('+');
        }
    }
}