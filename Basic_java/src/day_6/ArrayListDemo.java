package day_6;

import java.util.ArrayList;
import java.util.List;

public class ArrayListDemo {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
List<String> list = new ArrayList<String>();

ArrayList<String> l1 = new ArrayList<String>();

list.add("Delhi");
list.add("Mumbai"); 
list.add("Chennai");
list.add("Pune");

System.out.println(list);


list.add(3,"Banaras");
l1.add("Hyderabad");
list.addAll(l1);
System.out.println(list);

ArrayList<String> color = new ArrayList<String>();
color.add("Red");
color.add("Green");
color.add("White");
color.add("Black");
color.add("Pink");

System.out.println(color.get(2));
System.out.println(color.set(0, "Yellow"));
System.out.println(color);
System.out.println(color.isEmpty());
	}
}
