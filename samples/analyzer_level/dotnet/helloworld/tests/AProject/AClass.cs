using System;
using System.Text;

namespace AProject
{
    public class AClass
    {
        public AClass()
        {
            m_number = 0;
        }

        public void setNumber(int number)
        {
            m_number = number;
        }

        public int getNumber()
        {
            return m_number;
        }

        /// <summary>
        /// A number
        /// </summary>
        private int m_number;
    }
}
