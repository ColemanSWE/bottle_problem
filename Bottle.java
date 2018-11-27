public class Bottle {
	
	//Test here!
	public static void main(String[] args) {
		comparison(3, 4, 5);
	}
	
	static int calculate(int target, int bottle1Vol, int bottle2Vol) {
		
		int step = 1;
		int bottle1 = bottle1Vol;
		int bottle2 = 0;
		
		while (bottle1 != target && bottle2 != target){
			int pour = Math.min(bottle1, bottle2Vol - bottle2);
			
			bottle2 = bottle2 + pour;
			
			if (bottle1 - pour < 0){
				bottle1 = 0;
			}
			
			else {
				bottle1 = bottle1 - pour;
			}
			
			step++;
			
			
			if (bottle1 == target || bottle2 == target) {
				return step;
			}
			
			if (bottle1 == 0){
				bottle1 = bottle1Vol;
				step++;
			}
			
			if (bottle2 == bottle2Vol){
				bottle2 = 0;
				step++;
			}
			}
		return step;
		}
	
	static void comparison(int target, int bottle1Vol, int bottle2Vol){
		int solution1 = calculate(target, bottle1Vol, bottle2Vol);
		int solution2 = calculate(target, bottle2Vol, bottle1Vol);
		
		if (solution1 < solution2){
			System.out.println("Solution 1 is quicker and it takes " + solution1 +  " steps.");
		}
		else if (solution2 < solution1) {
			System.out.println("Solution 2 is quicker and it takes " + solution2 +  " steps.");
		}
		else {
			System.out.println("They're equal.");	
			}
		
	}
}
