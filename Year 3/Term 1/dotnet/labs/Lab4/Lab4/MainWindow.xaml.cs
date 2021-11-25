using System;
using System.Linq;
using System.Net.Mime;
using System.Windows;
using System.Windows.Controls;

namespace Lab4
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    
    // TRY REWORK FOR EVAL
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
                TextBox.Text += Num2.ToString();
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

            if (Num1 != 0 && Num2 != 0)
            {
                switch (Operation)
                {
                    case "/":
                        Num1 = Divide(Num1, Num2);
                        break;
                    case "*":
                        Num1 = Multiply(Num1, Num2);
                        break;
                    case "-":
                        Num1 = Subtract(Num1, Num2);
                        break;
                    case "+":
                        Num1 = Add(Num1, Num2);
                        break;
                }
                Num2 = 0;
            }
            
            Operation = curOperation;
            TextBox.Text = $"{Num1}{Operation}";
        }

        private void ButtonResult_Click(object sender, RoutedEventArgs e)
        {
            
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
