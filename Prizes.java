class Prizes {
	String prize1;
	String prize2;
	String prize3;
	String prize4;
	int numPrizes;
	String mysteryPrize;

	public void changePrize(String p, int n){
		if (n == 1) {
			this.prize1 = p;
		}
		if (n == 2) {
			this.prize2 = p;
		}
		if (n == 3) {
			this.prize3 = p;
		}
		if (n == 4) {
			this.prize4 = p;
		}
	}

	public String getNextPrize() {
		String p = "";
		if (this.numPrizes == 4) {
			p = this.prize4;
		}
		else if (this.numPrizes == 3) {
			p = this.prize3;
		}
		else if (this.numPrizes == 2) {
			p = this.prize2;
		}
		else if (this.numPrizes == 1) {
			p = this.prize1;
		}
		else {
			p = "There are no more prizes";
		}
		this.numPrizes = this.numPrizes - 1;
		return p;
	}

	public String getMystery() {
		return this.mysteryPrize;
	}

	public Prizes(String m) {
		this.prize1 = "Civies Pass";
		this.prize2 = "Mystery Box";
		this.prize3 = "Mr. Stubb's brings cookies";
		this.prize4 = "Pizza Party with Mr. Guadnola";
		this.numPrizes = 4;
		this.mysteryPrize = m;

	}

}