using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

using System.ComponentModel.DataAnnotations;

namespace SchoolDomainClasses
{

    [Table("StandardInfo")]
    public class Standard
    {
        public Standard()
        { 
        
        }
        [Key]
        public int StdId { get; set; }

        [Required]
        [MaxLength(100)]
        public string StandardName { get; set; }

        [StringLength(100)]
        public string Description { get; set; }
    }
}
