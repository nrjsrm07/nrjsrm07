package day_6;

public class NstedClass {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
try {
	
	try {
		System.out.println("Inside Block 1");
		int p =100/0;
		System.out.println(p);
	}catch (ArithmeticException e) {
		System.out.println("Exception 1");
	}
	try {
		System.out.println("Inside Block 2");
		int q = 20/0;
		System.out.println(q);
	}catch(ArrayIndexOutOfBoundsException e) {
		System.out.println("Exception 2");
	}
	try {
		System.out.println("Block 3");
		int x [] =new int[3];
		x[5]=25;
	}catch (Exception e) {
		// T000:handle exception
		System.out.println("Exception 3");
	}
}catch(ArithmeticException e2){
	System.out.println("Arithmetic Exception");
	System.out.println("Parent try block");
}catch(ArrayIndexOutOfBoundsException e4) {
	System.out.println("Array Problem");
	System.out.println("Inside Parent try");
}
System.out.println("default");
	}

}
