package day_6;

public class ExceptionClass {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int x=5;
        try{
            int arr[] =new int[6];
            arr[7]=23;
            arr[4]=10/0;
        }
        catch (ArithmeticException e){
            System.out.println(e);
        }
        catch (ArrayIndexOutOfBoundsException e){
            System.out.println(e);
        }
        System.out.println("***********");
	}

}
