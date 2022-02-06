namespace Lab7.Migrations
{
    using System;
    using System.Data.Entity.Migrations;
    
    public partial class CreatePeople : DbMigration
    {
        public override void Up()
        {
            CreateTable(
                "dbo.People",
                c => new
                    {
                        person_id = c.Int(nullable: false, identity: true),
                        fname = c.String(),
                        name = c.String(),
                        sname = c.String(),
                        when_born = c.DateTime(nullable: false),
                    })
                .PrimaryKey(t => t.person_id);
            
        }
        
        public override void Down()
        {
            DropTable("dbo.People");
        }
    }
}
