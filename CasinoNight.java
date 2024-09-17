class CasinoNight {

	public static void main(String[] args) {
		Prizes p = new Prizes("Phillips brings Chocolate!");
		p.changePrize("Laser Tag with Barber", 1);
		p.changePrize("Lego Set", 3);
		Prizes p2 = new Prizes("Mingels science explosion!");

		System.out.println("Boen and Kanav find themselves at casino night with 10k");
		System.out.println("Xavier and Jerry offer them another 30k to go in on prize 1");
		System.out.println("They win the auction!");
		System.out.println("Congratulations you win " + p.getNextPrize());
		System.out.println("Ryan and Brian win the next prize." +
			" They got " + p.getNextPrize());
		for (int i = 0; i < 20; i++) {
			System.out.println(p.getNextPrize());
		}
		System.out.println("Boen and Kanav find themselves at casino night with 10k");
		System.out.println("Xavier and Jerry offer them another 30k to go in on prize 1");
		System.out.println("They win the auction!");
		System.out.println("Congratulations you win " + p2.getNextPrize());
		System.out.println("Ryan and Brian win the next prize." +
			" They got " + p2.getNextPrize());
		for (int i = 0; i < 20; i++) {
			System.out.println(p2.getNextPrize());
		}

		printPrizes();
	}
}