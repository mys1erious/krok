
using System;
using System.Data.Entity;
using System.Data.Entity.Migrations;
using System.Linq;

namespace Lab7.Migrations
{
    internal sealed class Configuration : DbMigrationsConfiguration<Lab7.Lab7DbContext>
    {
        public Configuration()
        {
            AutomaticMigrationsEnabled = false;
        }
    } 
}