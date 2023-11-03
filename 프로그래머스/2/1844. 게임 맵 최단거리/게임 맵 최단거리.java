import java.util.*;

class Solution {
    static int n, m, answer;
    static int dist[][];
    static int dir[][] = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
    
    static class Node{
        int x, y;
        public Node(int x, int y){
            this.x = x;
            this.y = y;
        }
    }
    public int solution(int[][] maps) {
        n = maps.length;
        m = maps[0].length;
        dist = new int[n][m];
        dist[0][0] = 1;
        bfs(0, 0, maps);
        if(dist[n-1][m-1] == 0){
            return -1;
        }
        return dist[n-1][m-1];
    }
    static void bfs(int x, int y, int maps[][]){
        Queue<Node> q = new LinkedList<>();
        q.add(new Node(x, y));
        while(!q.isEmpty()){
            Node now = q.poll();
            int now_x = now.x;
            int now_y = now.y;
            if(now_x == n && now_y == m){
                return;
            }
            for(int i = 0; i < 4; i++){
                int nx = now_x + dir[i][0];
                int ny = now_y + dir[i][1];
                if(0 <= nx && nx < n && 0 <= ny && ny < m && maps[nx][ny] == 1 && dist[nx][ny] == 0){
                    dist[nx][ny] = dist[now_x][now_y] + 1;
                    q.add(new Node(nx, ny));
                }
            }
        }
    }
}