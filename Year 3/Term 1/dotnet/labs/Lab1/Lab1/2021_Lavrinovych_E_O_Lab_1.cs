namespace Lab1
// http://csharphelper.com/blog/2015/06/make-a-fraction-class-in-c/ Example
{
    internal class Program
    {
        public static void Main(string[] args)
        {
            
        }
    }
}

class Fraction
{
    private int numerator;
    private int denominator;
    public Fraction(string fraction)
    {
        string[] splitFraction = fraction.Split('/');
        numerator = int.Parse(splitFraction[0]);
        denominator = int.Parse(splitFraction[1]);
        
    }

    public Fraction(int numerator_, int denominator_)
    {
        numerator = nunumerator_;
        denominator = denominator_;
    }
}