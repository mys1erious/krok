using System;

namespace prac1.Lect1Examples
{
    // Delegate as Parameter
    public class Ex3
    {
        delegate void GetMessage();

        public static void Exec()
        {
            
            if (DateTime.Now.Hour < 12) ShowMessage(GoodMorning);
            else ShowMessage(GoodEvening);
        }

        private static void ShowMessage(GetMessage fun)
        {
            fun.Invoke();
        }
        
        private static void GoodMorning()
        {
            Console.WriteLine("Good Morning");
        }
        
        private static void GoodEvening()
        {
            Console.WriteLine("Good Evening");
        }
    }
}