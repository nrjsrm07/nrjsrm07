package day_6;

class MinBalanceException extends Exception{

	public MinBalanceException() {
		super();
		// TODO Auto-generated constructor stub
		System.out.println("Balnace is low");
	}
	
}

public class CustomMain {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
try {
	int acc[] = {100,101,102,103,104,105};
	int balance[] = {9000,2000,150,7000,5000};
	System.out.println("Account no. \t " +"Balance \t");
	System.out.println("***************************");
	for (int i =0; i<5; i++) {
	System.out.println(acc[i] +"\t\t   " + balance[i] );
	if(balance[i]<1000) {
		throw new MinBalanceException();	
	}
	}
}catch(MinBalanceException e) {
//	System.out.println("Exception Caught");
}
	}

}
