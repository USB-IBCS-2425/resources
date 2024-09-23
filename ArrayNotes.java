// import the utility library
import java.util.*;

class ArrayNotes {
	// Arrays are collections of data
	// They have fixed length
	// The collection must have the same data type
	public static void main(String[] args) {
		
		// create an array
		int[] a = {5, 4, 3, 2, 1};
		// access elements in the array by their position
		// a[0] is the element at position 0
		System.out.println(a[0]);
		System.out.println(a[3]);
		System.out.println(a[2]);

		// initialize an array without specific values
		double[] b = new double[10];

		b[4] = 77.7;

		// print out everything in the array
		for (int i = 0; i < 10; i++) {
			System.out.println(b[i]);
		}


	}
}






