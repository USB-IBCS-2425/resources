import java.util.*;

class SortingLab {

	public static ArrayList<Integer> BubbleSort(ArrayList<Integer> a) {
		while (true) {
			boolean swapped = false;
			for (int i = 0; i < a.size() - 1; i++) {
				int x = a.get(i);
				int y = a.get(i+1);
				if (x > y) {
					//swap
					int temp = x;
					a.set(i, y);
					a.set(i+1, temp);
					swapped = true;
				}
			}
			if (swapped == false) {
				break;
			}
		}
		return a;
	}

	public static ArrayList<Integer> SelectionSort(ArrayList<Integer> a) {
		for (int i=0; i < a.size(); i++) {
			int min = a.get(i);
			int minI = i;
			for (int j=i; j<a.size(); j++) {
				if (a.get(j) < min) {
					min = a.get(j);
					minI = j;
				}
			}
			// swap
			int temp = a.get(i);
			a.set(i, min);
			a.set(minI, temp);
		}
		return a;
	}

	public static ArrayList<Integer> InsertionSort(ArrayList<Integer> a) {
		return null;
	}

	public static void main(String[] args) {
		
		// Create an arraylist of n integers
		// with random integers from 1 - n
		ArrayList<Integer> a = new ArrayList<Integer>();
		int n = 1000;
		for (int i = 0; i < n; i++) {
			int newNum = 1 + (int)(Math.random()*n);
			a.add(newNum);
		}
		System.out.println(a);

		// keep track of the time in nanoseconds
		long start = System.nanoTime();
		ArrayList<Integer> b = SelectionSort(a);
		long end = System.nanoTime();
		long total = end - start;

		System.out.println(b);
		
		System.out.println("Sorted! Took " + total + " nanoseconds");
		
	}
}