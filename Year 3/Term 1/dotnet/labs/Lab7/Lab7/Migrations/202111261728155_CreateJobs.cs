namespace Lab7.Migrations
{
    using System;
    using System.Data.Entity.Migrations;
    
    public partial class CreateJobs : DbMigration
    {
        public override void Up()
        {
            CreateTable(
                "dbo.Jobs",
                c => new
                    {
                        job_id = c.Int(nullable: false, identity: true),
                        job_name = c.String(),
                    })
                .PrimaryKey(t => t.job_id);
            
        }
        
        public override void Down()
        {
            DropTable("dbo.Jobs");
        }
    }
}
