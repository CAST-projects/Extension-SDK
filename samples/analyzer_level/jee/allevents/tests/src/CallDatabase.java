

class CallDatabase
{
	static void call()
	{
		String query = "select * from ";
		
		if (true)
		{
			query += "Client";
		}
		else
		{
			query += "Customer";
		}
		
	
		java.sql.Statement.executeQuery(query);
	}
	
	void f()
	{
		
	}
	
	/// Inner class 
	/*
	 * So that one can see 
	 * start_type
	 * ...
	 *   start_type  --> start visit of inner class
	 *   ...
	 *   
	 *   end_type
	 * end_type
	 */
	public class Inner
	{
		
		void g()
		{
			
		}
	}
	
	
}