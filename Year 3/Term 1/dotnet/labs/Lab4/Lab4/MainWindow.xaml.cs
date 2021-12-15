using System;
using System.Linq;
using System.Windows;
using System.Windows.Controls;

namespace Lab4
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    
    public partial class MainWindow
    {
        public double Num1 { get; set; }
        public double Num2 { get; set; }
        public string Operation { get; set;}

        public readonly char[] Operations = { '/', '*', '-', '+' };
        
        public CalculatorLogic.CalcDelegate Divide = CalculatorLogic.Divide;
        public CalculatorLogic.CalcDelegate Multiply = CalculatorLogic.Multiple;
        public CalculatorLogic.CalcDelegate Subtract = CalculatorLogic.Subtract;
        public CalculatorLogic.CalcDelegate Add = CalculatorLogic.Add;
        
        public MainWindow()
        {
            InitializeComponent();
        }
        
        private void ButtonNumber_Click(object sender, RoutedEventArgs e)
        {
            var btnValue = Convert.ToDouble(((Button)sender).Content.ToString());
            
            if (Operation == null)
            {
                Num1 = (Num1 * 10) + btnValue;
                TextBox.Text = Num1.ToString();
            }
            else
            {
                Num2 = (Num2 * 10) + btnValue;
                TextBox.Text += btnValue;
            }
        }

        private void ButtonOperation_Click(object sender, RoutedEventArgs e)
        {
            string curOperation = ((Button)sender).Content.ToString();
            if (Operation == null)
                Operation = curOperation;
            
            if (Operations.Contains(TextBox.Text.Last()))
            {
                TextBox.Text = TextBox.Text.Substring(0, TextBox.Text.Length - 1) + Operation;
            }
            else
                TextBox.Text += $"{Operation}";

            (Num1, Num2) = OperationHandle(Num1, Num2);
            
            Operation = curOperation;
            TextBox.Text = $"{Num1}{Operation}";
        }

        private (double, double) OperationHandle(double num1, double num2)
        {
            if (num1 != 0 && num2 != 0)
            {
                switch (Operation)
                {
                    case "/":
                        num1 = Divide(num1, num2);
                        break;
                    case "*":
                        num1 = Multiply(num1, num2);
                        break;
                    case "-":
                        num1 = Subtract(num1, num2);
                        break;
                    case "+":
                        num1 = Add(num1, num2);
                        break;
                }
                num2 = 0;
            }

            return (num1, num2);
        }

        private void ButtonResult_Click(object sender, RoutedEventArgs e)
        {
            (Num1, Num2) = OperationHandle(Num1, Num2);
            Operation = null;
            TextBox.Text = $"{Num1}";
        }
        
        private void ButtonClear_Click(object sender, RoutedEventArgs e)
        {
            Num1 = 0;
            Num2 = 0;
            Operation = null;
            TextBox.Text = string.Empty;
        }
    }
}
