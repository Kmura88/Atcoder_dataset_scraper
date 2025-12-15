import java.util.*;

public class Main {

  public static void main(String[] args) {
    int N = scanner.nextInt();
    int M = scanner.nextInt();
    int[][] conditions = new int[M][2];
    for (int i = 0; i < M; i++) {
      conditions[i][0] = scanner.nextInt() - 1;
      conditions[i][1] = scanner.nextInt() - 1;
    }
    int K = scanner.nextInt();
    int[][] people = new int[K][2];
    for (int i = 0; i < K; i++) {
      people[i][0] = scanner.nextInt() - 1;
      people[i][1] = scanner.nextInt() - 1;
    }
    int bound = 1 << K;
    int max = 0;
    for (int i = 0; i < bound; i++) {
      boolean[] b = new boolean[N];
      for (int j = 0; j < N; j++) {
        if ((i & (1 << j)) == 1) {
          b[j] = true;
        }
      }
      max = Math.max(max, getSatisfiedCount(b, conditions));
    }
    System.out.println(max);
  }

  private static int getSatisfiedCount(boolean[] vis, int[][] conditions) {
    int cnt = 0;
    for (int[] condition : conditions) {
      int c1 = condition[0];
      int c2 = condition[1];
      if (vis[c1] && vis[c2]) {
        cnt++;
      }
    }
    return cnt;
  }

  private static int[] readArray(int n) {
    int[] arr = new int[n];
    for (int i = 0; i < n; i++) {
      arr[i] = scanner.nextInt();
    }
    return arr;
  }

  private static final Scanner scanner = new Scanner(System.in);
}
