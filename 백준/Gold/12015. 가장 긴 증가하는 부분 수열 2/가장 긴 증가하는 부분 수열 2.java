import java.util.*;
import java.io.*;

public class Main {
	public static void main(String[] args) throws Exception{
		// 입력
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		int arr[] = new int[N];
		int dp[] = new int[N];
		StringTokenizer st = new StringTokenizer(br.readLine());
		for(int i = 0; i < N; i++) {
			arr[i] = Integer.parseInt(st.nextToken());
		}
		
		// 로직
		dp[0] = arr[0];
		int length = 1;
		
		for(int i = 1; i < N; i++) {
			int key = arr[i];
			
			if(dp[length-1] < key) {
				length++;
				dp[length-1] = key;
			}else {
				int l = 0;
				int r = length;
				while(l < r) {
					int mid = (l+r) >>> 1;
					if(dp[mid] < key) {
						l = mid+1;
					}else {
						r = mid;
					}
				}
				dp[l] = key;
			}
		}
		System.out.println(length);
	}
}
