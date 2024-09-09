class notes9_9 {

	public static void main(String[] args) {
		
		int x = 10;
		double y = 5.2;

		String response = "WOAH";

		// conditions use the key words 'if' and 'else' ('elif')
		// the parantheses require a boolean condition
		// between the braces is the consequence (if true)
		if (x > 8) {
			System.out.println("the variable x is greater than 8");
		}
		// if nothing needs to happen if it is false. do not
		// use an 'else'

		if (y / 2 <= 4) {
			System.out.println(response);
		}
		// else statement is AFTER the braces. It has its own
		// set of braces
		else {
			y = y++;
		}

		// '==' is it equal?
		if (x == 4) {
			// do something
			System.out.println("x is 4");
		}

		String response2 = "WOAH";

		if (response == response2) {
			System.out.println("Strings can be compared");
		}

	}




}