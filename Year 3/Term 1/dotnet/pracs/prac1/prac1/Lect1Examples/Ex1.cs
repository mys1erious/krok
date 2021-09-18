using System;

namespace prac1.Lect1Examples
{
    // Delegates
    public class Ex1
    {
        delegate void GetMessage();

        public static void Exec()
        {
            GetMessage del;
            
            if (DateTime.Now.Hour < 12) del = GoodMorning;
            else del = GoodEvening;
            del.Invoke();
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