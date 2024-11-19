import java.util.*;

class SortingLab {

	public static ArrayList<Integer> a;
	public static int n;

	public SortingLab(int num) {
		a = new ArrayList<Integer>();
		n = num;
		for (int i = 0; i < num; i++) {
			int newNum = 1 + (int)(Math.random()*num);
			a.add(newNum);
		}
	}

	public static void resetList() {
		for (int i = 0; i < n; i++) {
			int newNum = 1 + (int)(Math.random()*n);
			a.set(i, newNum);
		}
	}

	public static void BubbleSort() {
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
	}

	public static void SelectionSort() {
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
	}

	public static void InsertionSort() {

		for (int i=0; i<a.size(); i++) {
			// compare with the sorted elements.
			// i amount of sorted elements
			int elem = a.get(i);
			for (int j=i; j>0; j--) {
				// comparison with each sorted element
				if (elem < a.get(j-1)) {
					// move element at j-1 up
					a.set(j, a.get(j-1));
				}
				else {
					a.set(j, elem);
					break;
				}
			}
		}
	}

	public static int QuickSplit(int start, int stop) {
		// pick the last element to be the pivot
		int piv = a.get(stop);
		int pos = start;

		// loop through list to compare each element with pivot
		for (int i = start; i < stop; i++) {
			if (a.get(i) <= piv) {
				// increase the pivots final position
				pos = pos + 1;
				// Swap the lower value to the left
				int temp = a.get(pos - 1);
				a.set(pos - 1, a.get(i));
				a.set(i, temp);
			}
		}
		// move the pivot to the right spot
		int temp2 = a.get(pos);
		a.set(pos, a.get(stop));
		a.set(stop, temp2);

		return pos;
	}

	public static void QuickSort(int start, int stop) {
		// keep sorting if the starting index is less than the stopping index
		if (start < stop) {
			// 
			int p = QuickSplit(start, stop);

			// recursively call Quicksort on the lower half
			// and upper half of the pivot
			QuickSort(start, p-1);
			QuickSort(p+1, stop);
		}
		// else the method doesn't do anything (it terminates recursion)
	}

	public static void Merge(int start, int middle, int stop) {
		
		// i is the index of the left-hand side list
		int i = start;
		// j is the index of the right-hand side list
		int j = middle + 1;
		// k is the index of the current element
		int k = 0;
		// temporary array to hold the values so it does not overwrite
		// we will merge onto a new array then replace
		// all items in the arraylist with this temp array
		int[] tempArr = new int[stop - start + 1];

		while ((i <= middle) && (j <= stop)) {
			if (a.get(i) <= a.get(j)) {
				tempArr[k] = a.get(i);
				i++;
			}
			else {
				tempArr[k] = a.get(j);
				j++;
			}
			k++;
		}
		// add all remaining elements from left or right
		while (i <= middle) {
			tempArr[k] = a.get(i);
			i++;
			k++;
		}
		while (j <= stop) {
			tempArr[k] = a.get(j);
			j++;
			k++;
		}
		// add temporary array back into arraylist
		for (i = start; i <= stop; i++) {
			a.remove(i);
			// insert element from temp array at position i
			// i - start keeps track of the relative postion
			// in temporary array
			a.add(i, tempArr[i - start]);
		}
	}

	public static void MergeSort(int start, int stop) {
		if (start < stop) {
			// similar to binary search, find median value.
			int middle = (start + stop)/2;
			// recursively call Merge sort on both halves
			MergeSort(start, middle);
			MergeSort(middle+1, stop);

			// merge two halves together
			Merge(start, middle, stop);
		}
	}

	public static void main(String[] args) {

		SortingLab s = new SortingLab(200000);
		int num = s.a.size();
		int start_pos = 0;
		int stop_pos = num;

		// keep track of the time in nanoseconds
		long start = System.nanoTime();
		//QuickSort(start_pos, stop_pos-1);
		MergeSort(start_pos, stop_pos - 1);
		long end = System.nanoTime();
		long total = end - start;

		System.out.println(s.a);
		
		System.out.println("Sorted! Took " + total+ " nanoseconds");
		
	}
}