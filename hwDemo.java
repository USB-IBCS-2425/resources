import java.util.*;

class Student {
	int rafNum;
	String name;

	public Student(String n) {
		name = n;
		rafNum = (int)(Math.random()*10000);
	}

	public int getNum() {
		return rafNum;
	}

	public String getName() {
		return name;
	}
}

class Raffle {
	// we need an array for students and an array of raffle nums
	Student[] sArr;
	int[] rafNums;

	public Raffle(Student[] s) {
		sArr = s;
		// need to create a empty array of integers first
		rafNums = new int[s.length];
		// loop through the array to set values
		// equal to each student's number
		for (int i = 0; i < sArr.length; i++) {
			// sArr[i] is a student
			rafNums[i] = sArr[i].getNum();
		}
	}

	public void printRaf() {
		for (int n : rafNums) {
			System.out.println(n);
		}
	}

	public Student getWinner() {
		int choice = (int)(Math.random()*5);
		//System.out.println(choice);

		return sArr[choice];
	}
}

class hwDemo {
	public static void main(String[] args) {
		Student s1 = new Student("A");
		Student s2 = new Student("B");
		Student s3 = new Student("C");
		Student s4 = new Student("D");
		Student s5 = new Student("E");
		Student[] s = {s1, s2, s3, s4, s5};

		Raffle r = new Raffle(s);
		r.printRaf();
		Student win = r.getWinner();
		System.out.println(win.getName() + " is the winner!");

	}
}