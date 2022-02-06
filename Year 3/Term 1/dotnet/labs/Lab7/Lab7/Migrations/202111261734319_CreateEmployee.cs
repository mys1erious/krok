namespace Lab7.Migrations
{
    using System;
    using System.Data.Entity.Migrations;
    
    public partial class CreateEmployee : DbMigration
    {
        public override void Up()
        {
            CreateTable(
                "dbo.Employees",
                c => new
                    {
                        employee_id = c.Int(nullable: false, identity: true),
                        person_id = c.Int(nullable: false),
                        job_id = c.Int(nullable: false),
                        start_date = c.DateTime(nullable: false),
                        end_date = c.DateTime(nullable: false),
                    })
                .PrimaryKey(t => t.employee_id)
                .ForeignKey("dbo.Jobs", t => t.job_id, cascadeDelete: true)
                .ForeignKey("dbo.People", t => t.person_id, cascadeDelete: true)
                .Index(t => t.person_id)
                .Index(t => t.job_id);
            
        }
        
        public override void Down()
        {
            DropForeignKey("dbo.Employees", "person_id", "dbo.People");
            DropForeignKey("dbo.Employees", "job_id", "dbo.Jobs");
            DropIndex("dbo.Employees", new[] { "job_id" });
            DropIndex("dbo.Employees", new[] { "person_id" });
            DropTable("dbo.Employees");
        }
    }
}
