namespace Lab4
{
    public static class CalculatorLogic
    {
        public delegate double CalcDelegate(double firstNum, double secondNum);
        
        public static double Divide(double firstNum, double secondNum)
        {
            if (firstNum == 0 || secondNum == 0)
                return 0;
            return firstNum / secondNum;
        }
        
        public static double Multiple(double firstNum, double secondNum)
        {
            return firstNum * secondNum;
        }
        
        public static double Add(double firstNum, double secondNum)
        {
            return firstNum + secondNum;
        }
        
        public static double Subtract(double firstNum, double secondNum)
        {
            return firstNum - secondNum;
        }
    }
}