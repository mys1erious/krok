using System.ComponentModel.DataAnnotations;

namespace Lab7
{
    public class Job
    {
        [Key]
        public int job_id { get; set; }
        
        public string job_name { get; set; }
    }
}