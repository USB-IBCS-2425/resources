import java.util.*;

class ArrayListNotes {
	
	public static void main(String[] args) {
		
		// ArrayLists need to be imported
		// Create an instance by giving it
		// a specific data type

		ArrayList<Integer> a = new ArrayList<Integer>();
		a.add(5);
		a.add(7);
		System.out.println(a);
		a.add(0, 9);
		System.out.println(a);
		// get() is the way to access elements
		// print element at position 0
		System.out.println(a.get(0));

		// Example of a random list of integers 1-10
		ArrayList<Integer> b = new ArrayList<Integer>();
		for (int i=0; i<50; i++) {
			b.add((int)(Math.random()*10)+1);
		}
		System.out.println(b);
		Integer x = 5;
		while (true) {
			// break the loop if no more 5's
			if (b.contains(5)) {
				b.remove(x);
			}
			// get rid of all 5's
			else {
				break;
			}
		}
		System.out.println(b);
		
		// set can change elements at specific positions
		b.set(0, 99);
		System.out.println(b)

	}

}