class Prizes {
	String prize1;
	String prize2;
	String prize3;
	String prize4;
	int numPrizes;

	public String getNextPrize() {
		String p = "";
		if (numPrizes == 4) {
			p = prize4;
		}
		else if (numPrizes == 3) {
			p = prize3;
		}
		else if (numPrizes == 2) {
			p = prize2;
		}
		else if (numPrizes == 1) {
			p = prize1;
		}
		else {
			p = "There are no more prizes";
		}
		numPrizes = numPrizes - 1;
		return p;
	}

	public Prizes() {
		prize1 = "Civies Pass";
		prize2 = "Mystery Box";
		prize3 = "Mr. Stubb's brings cookies";
		prize4 = "Pizza Party with Mr. Guadnola";
		numPrizes = 4;
	}

}