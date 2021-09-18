using System;

namespace prac1.Lect1Examples
{
    // Events Example: User withdraws a certain amount of money from the account
    //                 then need to display a message about the operation
    
    // ------------------------------------------ Fix bugs ----------------------------------------------------
    public class Ex4
    {
        public static void Exec()
        {
            Account account = new Account(200);
            Account.AccountStateHandler colorDelegate = new Account.AccountStateHandler(Color_Message);
            account.RegisterHandler(new Account.AccountStateHandler(Show_Message));
            
            
            account.RegisterHandler(colorDelegate);
            account.Withdraw(100);
            account.Withdraw(150);
            account.UnregisterHandler(colorDelegate);
            account.Withdraw(50);
        }
        
        private static void Show_Message(string message)
        {
            Console.WriteLine(message);
        }

        private static void Color_Message(string message)
        {
            Console.ForegroundColor = ConsoleColor.Red;
            Console.WriteLine(message);
            Console.ResetColor();
        }
    }

    class Account
    {
        int sum;
        public Account(int _sum) { sum = _sum; }
        public int Sum { get { return sum; } }
        public void Put(int _sum) { sum += sum; }


        public delegate void AccountStateHandler(string message);
        AccountStateHandler fun;

        public void RegisterHandler(AccountStateHandler del)
        {
            //Delegate mainDel = System.Delegate.Combine(fun, _fun);
            //fun = mainDel as AccountStateHandler;
            fun += del;
        }
        
        public void UnregisterHandler(AccountStateHandler del)
        {
            //Delegate mainDel = System.Delegate.Remove(fun, del);
            //fun = mainDel as AccountStateHandler;
            fun -= del;
        }
        

        public void Withdraw(int _sum)
        {
            if (_sum <= sum)
            {
                sum -= _sum;
                if (fun != null)
                    fun($"{sum} has been withdrawn from the account");
            }
            else
            {
                if (fun != null)
                    fun("Not enough money in the account");
            }

        }
    }
}