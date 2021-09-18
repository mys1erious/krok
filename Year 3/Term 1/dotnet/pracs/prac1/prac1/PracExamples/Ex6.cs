namespace prac1.PracExamples
{
    // Multicast Delegate
    public class Ex6
    {
        private delegate void Print(int value);
        
        public static void Exec()
        {
            Print printDel = Utils.PrintNumber;
            printDel += Utils.PrintHexadecimal;
            printDel += Utils.PrintMoney;
            printDel(1000);

            printDel -= Utils.PrintHexadecimal;
            printDel(2000);
        }
    }
}