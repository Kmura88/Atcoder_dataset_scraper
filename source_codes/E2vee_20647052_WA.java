import java.util.*;

class Main{
  
  public static void main(String[] args){
  
    Scanner sc = new Scanner(System.in);
    
    //とりあえずN,Mを読みとっろっか..
    int n = sc.nextInt();
    int m = sc.nextInt();
    
    //解
    int ans = 0;
      
    //条件iを保存する配列を作る。
    int[] a = new int[m];
    int[] b = new int[m];
    
    //条件i 皿A,Bの両方にボールが置かれていると満たされる
    for(int i=0; i<m; i++){
      //条件を読み取る
      a[i] = sc.nextInt();
      b[i] = sc.nextInt();
    }
    
    //Kの読み取り
    int k = sc.nextInt();
    
    //C,Dのどちらかにボールを置ける
    int[] c = new int[k];
    int[] d = new int[k];
    
    //K人の人が、C or Dの皿にボールを置く
    for(int i=0; i<k; i++){
      //条件を読み取る
      c[i] = sc.nextInt();
      d[i] = sc.nextInt();
    }
    
    //再現できるボールの置き方（皿）
    int plate[] = new int[n+1];//番号が1からなので
    
    //C or Dのbit全探索で2^k通り
    for(int i=0; i<Math.pow(2,k); i++){
      //bit全探索の全通りのloop
      //皿の初期化
      Arrays.fill(plate, 0);
      
      for(int j=0; j<k; j++){
        //1loop毎にどの皿にボールを置くのかを判定
        
        ////ボールを置く皿の対象
        if((1&i>>j)==1){
          plate[c[j]]=1;
        }else{
          plate[d[j]]=1;
        }
        
      }
      
      //条件と確認
      int r = 0;
      for(int j=0; j<m; j++){
        if(plate[a[j]]==1 && plate[b[j]]==1){
          r++;
        }
      }
      
      //ans = Math.max(ans, r);
      ans = r;
    }
    
    //解の出力！
    System.out.println(ans);
  
  }
}