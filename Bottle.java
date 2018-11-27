public class Bottle {
	
	//Test here!
	public static void main(String[] args) {
		System.out.println(calculate(3, 4, 5));
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
	
	
}