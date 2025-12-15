//再帰メソッド解法
import java.util.*;
class Main{
    static int N, M, K;
    static int[][] a, c;
    static int ans;
    public static void main(String[] args) {
        // input
        var sc = new Scanner(System.in);
        N = sc.nextInt(); M = sc.nextInt();
        a = new int[M][2];
        for(int i=0;i<M;i++){
            a[i][0] = sc.nextInt() - 1;
            a[i][1] = sc.nextInt() - 1;
        }
        K = sc.nextInt();
        c = new int[K][2];
        for(int i=0;i<K;i++){
            c[i][0] = sc.nextInt() - 1;
            c[i][1] = sc.nextInt() - 1;
        }
        sc.close();
        
        // solve
        ans = 0;
        var s = new int[K];
        dfs(s, 0);
        System.out.println(ans);
    }
    
    static void dfs(int[] s, int i) {
        if(i == K-1) {
            var b = new boolean[N];
            for(int j=0;j<K;j++) {
                b[c[j][s[j]]] = true;
            }
            int cnt = 0;
            for(int j=0;j<M;j++) {
                if(b[a[j][0]] && b[a[j][1]]) cnt++;
            }
            ans = Math.max(ans, cnt);
            return;
        }
        for(int j=0;j<2;j++) {
            s[i] = j;
            dfs(s, i+1);
        }
    }
}