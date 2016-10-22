using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.ComponentModel.DataAnnotations;

namespace SchoolDomainClasses
{
    [Table("StudentInfo")]
    public class Student
    {
        public Student()
        { 
        
        }
        
        [Key]
        public int SID { get; set; }

        [Required(ErrorMessage="Student Name is Required" )]
        [Column("Name", TypeName="ntext")]        
        [MaxLength(20), MinLength(2, ErrorMessage="Student name can not be 2 character or less")]
        public string StudentName { get; set; }

        [NotMapped]
        public int? Age { get; set; }

        [ConcurrencyCheck()]
        [Timestamp]
        public Byte[] LastModifiedTimestamp { get; set; }

        public int? MathScore { get; set; }
        
        public int? ScienceScore { get; set; }


        [DatabaseGenerated(DatabaseGeneratedOption.Computed)]
        public int? TotalScore
        {
            get;
            set;

        }
        
        public int StdId { get; set; }

        [ForeignKey("StdId")]
        public virtual Standard Standard { get; set; }
    }
    
    public class LazyStudent : Student
    {
    	public int Field { get; set; }
    }
}
