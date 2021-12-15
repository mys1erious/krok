using System.Data.Entity;

namespace Lab7
{
    public class Lab7DbContext : DbContext
    {
        public DbSet<Person> People { get; set; }
        public DbSet<Job> Jobs { get; set; }
        public DbSet<Employee> Employees { get; set; }
    }
}