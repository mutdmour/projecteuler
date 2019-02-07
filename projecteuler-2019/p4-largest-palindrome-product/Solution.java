class Solution {

    private static final int MIN = 100;
    private static final int MAX = 1000;

	public static void main(String[] args) {
		System.out.println(helper());
	}

	private static int helper() {
        int res = 0;
        for (int i = MAX - 1; i >= MIN; i--) {
            for (int j = MAX - 1; j >= MIN; j--) {
                if (isPalindrome(i * j) && i * j > res) {
                    res = i * j;
                }
            }
        }

		return res;
	}

    private static boolean isPalindrome(int n) {
        String s = Integer.toString(n);
        for (int i = 0; i < s.length() / 2; i++) {
            if (s.charAt(i) != s.charAt(s.length() - i - 1)) {
                return false;
            }
        }
        return true;
    }
}
