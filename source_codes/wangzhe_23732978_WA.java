


import java.util.*;

public class Main {
    public static int max;
    public static void dfs(int[]a,int[]b,int[]c,int[]d,boolean[]choose,int m,int k,int current){
        if (current==k){
            int sum=0;

            for (int i=0;i<m;i++){
                if (choose[a[i]]&&choose[b[i]]){
                    sum++;
                }
            }
            if (sum>max){
                max = sum;
            }
            return;
        }
        if (!choose[c[current]]){
            choose[c[current]] = true;
            dfs(a,b,c,d,choose,m,k,current+1);
            choose[c[current]] = false;
        }
        choose[d[current]] = true;
        dfs(a,b,c,d,choose,m,k,current+1);

    }


    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int m = scanner.nextInt();
        int[]a = new int[m];
        int[]b = new int[m];
        for (int i=0;i<m;i++){
            a[i] = scanner.nextInt();
            b[i] = scanner.nextInt();
        }
        int k =scanner.nextInt();
        int[]c = new int[k];
        int[]d = new int[k];
        for (int i=0;i<k;i++){
            c[i] = scanner.nextInt();
            d[i] = scanner.nextInt();
        }
        boolean[]choose = new boolean[n+1];
        max = Integer.MIN_VALUE;
        dfs(a,b,c,d,choose,m,k,0);
        System.out.println(max);





    }
}
