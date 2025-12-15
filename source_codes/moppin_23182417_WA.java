import java.util.Scanner;

/**
 * C - Bowls and Dishes
 * 2021/06/05
 *
 */
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = Integer.parseInt(sc.next());
        int M = Integer.parseInt(sc.next());
        int[] c = new int[M];
        for (int i = 0; i < M; i++) {
            int a = Integer.parseInt(sc.next()) - 1;
            int b = Integer.parseInt(sc.next()) - 1;
            c[i] = 1 << a;
            c[i] |= 1 << b;
        }
        int K = Integer.parseInt(sc.next());
        int[] C = new int[K];
        int[] D = new int[K];
        for (int i = 0; i < K; i++) {
            C[i] = Integer.parseInt(sc.next()) - 1;
            D[i] = Integer.parseInt(sc.next()) - 1;
        }
        sc.close();

        int max = 0;
        for (int mask = 0; mask < 1 << K; mask++) {
            int tempC = 0;
            for (int i = 0; i < K; i++) {
                if ((mask >> i & 1) == 1) {
                    tempC |= 1 << C[i];
                } else {
                    tempC |= 1 << D[i];
                }
            }

            int cnt = 0;
            for (int i = 0; i < M; i++) {
                if ((c[i] & tempC) == c[i]) cnt++;
            }

            max = Math.max(max, cnt);
        }

        System.out.println(max);
    }
}
