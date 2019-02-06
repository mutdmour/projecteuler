class Solution {
    private final static int MAX = 4000000;

	public static void main(String[] args) {
		System.out.println(helper());
	}

	private static int helper() {
        int i = 1;
        int j = 1;
        int sum = 0;
        while (j < MAX) {
            if (j % 2 == 0) {
                sum += j;
            }
            int temp = j;
            j = i + j;
            i = temp;
        }
		return sum;
	}
}
