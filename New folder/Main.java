import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {
	public static void main(String[] args) 
	{
		try
		{
			BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
			System.out.println("Enter the number of players");
			int x=Integer.parseInt(br.readLine());
			Player[] plist=new Player[x];
			for(int i=0;i<x;i++)
			{	
			System.out.println("Enter the player name");
			String name=br.readLine();
			System.out.println("Enter the country name");
			String country=br.readLine();
			System.out.println("Enter the skill");
			String skill=br.readLine();
			plist[i]=new Player(name, country, skill);
			}
		 PlayerBO pbo=new PlayerBO();
		 pbo.displayAllPlayerDetails(plist);
		 System.out.println("Enter the country name for which players details to be known");
		 String cname=br.readLine();
		 pbo.displaySpecificPlayerDetails(plist,cname);
		}.
	}

}
