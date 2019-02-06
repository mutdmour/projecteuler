import java.util.ArrayList;
import java.util.List;

class Solution {
    private final static long num = 600851475143L;

	public static void main(String[] args) {
		System.out.println(helper(num));
	}

	private static long helper(long n) {
        List<Long> primes = new ArrayList<>();
        primes.add(new Long(2));
        long res = 1;
        for (long i = 3; i <= n; i+=2) {
            if (isPrime(i, primes)) {
                primes.add(i);
                if (n % i == 0) {
                    res = i;
                    n = n / i;
                }
            }
        }
		return res;
	}

    private static boolean isPrime(long n, List<Long> primes) {
        for (int i = 0; i < primes.size(); i++) {
            if (n % primes.get(i) == 0) {
                return false;
            }
        }
        return true;
    }
}
