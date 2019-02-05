class Solution {
	private static final int MAX = 1000;

	public static void main(String[] args) {
		System.out.println(helper());
	}

	private static int helper() {
		int sum = 0;
		for (int i = 0; i < MAX; i++) {
			if (isDivisibleBy3Or5(i)) {
				sum += i;
			}
		}
		return sum;
	}

	private static boolean isDivisibleBy3Or5(int n) {
		return n % 3 == 0 || n % 5 == 0;
	}
}
