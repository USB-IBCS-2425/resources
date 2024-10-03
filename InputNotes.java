import java.util.*;

class InputNotes {
	public static void main(String[] args) {
		
		// Create a scanner object to get user input
		Scanner s = new Scanner(System.in);
		// nextLine() method prompts the user to type in
		// string input (into the command line)
		System.out.println("What's your name?");
		String inp = s.nextLine();
		System.out.println("Hello, " + inp + ". Nice to meet you!");

		// continue to get input by calling methods on 
		// this scanner object
		System.out.println("What are your plans this weekend?");
		String plan = s.nextLine();
		System.out.println("Cool! I have always wanted to " + plan);

		// Get an integer
		int num = s.nextInt();
		System.out.println("Doubled, that is: " + num*2);


	}
}