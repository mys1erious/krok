using System;
using System.ComponentModel.DataAnnotations;

namespace Lab7
{
    public class Person
    {   
        [Key]
        public int person_id { get; set; }
        
        public string fname { get; set; }
        public string name { get; set; }
        public string sname { get; set; }
        public DateTime when_born { get; set; }
    }
}