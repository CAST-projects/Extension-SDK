using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;


namespace Linq2Sql
{

    public class DbSet
    {

    }

    public class DbSet<T>
    {

    }

    public class DbSet<T,U>
    {

    }

    public class Context 
    {
        public DbSet<Customer> customers { get; set ;}
    }
}
