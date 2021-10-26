using System;
using System.Text.RegularExpressions;

namespace Lab5
{
    internal static class Lab5
    {
        public static void Main(string[] args)
        {
            string[] phoneNumberSamples = new[]
            {
                "3087774825",
                "1334431660",
                "(281)388-0388",
                "(979)826-3273",
                "(979) 778-0978",
                "281-342-2452",
                "dwads",
                "3213131"
            };

            string[] floatNumberSamples = new[]
            {
                "12",
                ".3",
                "12.321341",
                "awas",
                "12.3.4"
            };
            

            Console.WriteLine("Phone number checks: ");
            foreach (var phone in phoneNumberSamples)
            {
                Console.WriteLine($"{phone} : {PhoneNumberCheck(phone)}");
            }
            
            Console.WriteLine("\nFloat number checks: ");
            foreach (var num in floatNumberSamples)
            {
                Console.WriteLine($"{num} : {FloatNumberCheck(num)}");
            }
            
            
        }

        
        public static bool PhoneNumberCheck(string phoneNumber)
        {
            string pattern = @"\(?\d{3}\)?-? *\d{3}-? *-?\d{4}";
            Regex rgx = new Regex(pattern);
            
            return rgx.IsMatch(phoneNumber);
        }


        public static bool FloatNumberCheck(string floatNumber)
        {
            string pattern = @"^[0-9]*(?:\.[0-9]*)?$";
            Regex rgx = new Regex(pattern);
            
            return rgx.IsMatch(floatNumber);
        }
    }
}