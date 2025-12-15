import java.util.Scanner;

public class Main {

    static int N;            // # of dishes
    static int M;            // # of conditions
    static int[][] Condition;        //   list of conditions [M][2]
    static int K;            // # of people
    static int [][] People;    //         [K][2]

    static int Count;

    public static void input() {
        Scanner sc = new Scanner(System.in);

        N = sc.nextInt();
        M = sc.nextInt();
        sc.nextLine();

        Condition = new int[M][2];
        for (int m = 0; m < M; ++m) {
            Condition[m][0] = sc.nextInt();
            Condition[m][1] = sc.nextInt();
            sc.nextLine();
        }

        K = sc.nextInt();
        sc.nextLine();

        People = new int[K][2];
        for (int i = 0; i < K; ++i) {
            People[i][0] = sc.nextInt();
            People[i][1] = sc.nextInt();
            sc.nextLine();
        }

        sc.close();
    }

    public static int count(int[] list) {
        int count = 0;
        for (int i = 0; i < M; ++i) {
            if (list[Condition[i][0]] > 0 && list[Condition[i][1]] > 0) {
                count++;
            }
        }
        return count;
    }

    public static void test(int index, int[] list) {

        if (index >= K) {
            Count = Math.max(Count, count(list));
            return;
        }

        int C = People[index][0];
        list[C]++;
        test(index + 1, list);

        list[C]--;
        int D = People[index][1];
        list[D]++;
        test(index + 1, list);
    }

    public static void main(String[] args) {
        input();

        test(0, new int[N + 1]);
        System.out.println(Count);
    }

}
