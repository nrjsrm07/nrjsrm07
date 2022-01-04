package day_6;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.ListIterator;

public class EmployeeArray {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		ArrayList<String> emp = new ArrayList<String>();
		emp.add("Amit");
		emp.add("Anurag");
		emp.add("Babulal");
		emp.add("Chandu");
		emp.add("Dev");
		emp.add("Eklakh");
		emp.add("Farooq");
		emp.add("Ganesh");
		emp.add("Hitesh");
		emp.add("Ishita");
		emp.add("Jacqline");
		emp.add("Kapil");
		emp.add("Dev");
		
		for (int i=0; i<emp.size();i++) {
			System.out.println("Employee Name at index: " + i + " is :\t" + emp.get(i));} 
		
		System.out.println(emp);
		
		//IndexOf() 
		System.out.println("Dev is at index: " + emp.indexOf("Dev"));
		
		//lastIndexOf()
		System.out.println("Last index of Dev: " + emp.lastIndexOf("Dev"));
		
		//toArray()
		Object[] arr = emp.toArray();  
        System.out.println("Elements of ArrayList"+" as Array: " + Arrays.toString(arr));
		
        //subList()
        List<String> emp2 = emp.subList(2, 7);
		System.out.println("Sub List from 2nd Index to 7th Index : " + emp2);
		emp2.add(3, "Devansh");
		System.out.println(emp2);
		
		//retainAll()
		emp2.retainAll(emp);
		System.out.println("After retainAll Method: "+ emp2 );
		
		//ListIterator
		ListIterator<String> namesIterator = emp2.listIterator();
		while (namesIterator.hasNext()) {
            System.out.println(namesIterator.next());
		}
		
		//Adding array into arrayList
		List al = Arrays.asList(emp);
		System.out.println(emp);
		String[] gems = {"Rahul", "Utkarsh",
                "Shubham", "Neelam"};
		List<String> a2 = new ArrayList<String>(Arrays.asList(gems));
        System.out.println(a2);
        a2.add("Shashank");
        a2.add("Nishant");
        System.out.println("ArrayList After adding two more names: ");
        System.out.println(a2);
        
        // Sorting
        Collections.sort(a2);
        System.out.println("After Sorting: "+ a2);   
		        
	}
}
