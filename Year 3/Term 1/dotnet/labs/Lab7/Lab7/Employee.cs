using System;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;

namespace Lab7
{
    public class Employee
    {
        [Key]
        public int employee_id { get; set; }
        
        public int person_id { get; set; }
        public int job_id { get; set; }
        
        public DateTime start_date { get; set; }
        public DateTime end_date { get; set; }
        
        [ForeignKey("person_id")]
        public Person Person { get; set; }
        
        [ForeignKey("job_id")]
        public Job Job { get; set; }
    }
}