

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
		
		
		java.sql.Statement.executeQuery(query);
	}

	void f2()
	{
		java.sql.Statement.executeQuery("DELETE FROM Client");
	}
	
}