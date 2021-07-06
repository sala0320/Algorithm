#include <iostream>
#include <queue>

#define max_int 51
using namespace std;

//시간 복잡도: O(nm)
//공간 복잡도: O(nm)
//사용한 알고리즘: BFS
//사용한 자료구조: 배열

int n, m, start_i, start_j, end_i, end_j;
// 지도 정보를 저장할 배열
char a[max_int][max_int];
// 물이 차오르는 날을 저장할 배열
int water_day[max_int][max_int];
// 이동하는데 걸리는 시간을 저장할 배열
int check[max_int][max_int];
int dx[] = {0, 0, 1, -1};
int dy[] = {-1, 1, 0, 0};

queue<pair<int, int>> water;

// i, j에 대해 물이 언제 차는지를 BFS로 계산
void water_bfs() {
    while(!water.empty()){
        int x = water.front().first;
        int y = water.front().second;
        water.pop();

        for(int i=0; i<4; i++){
            int nx = x + dx[i];
            int ny = y + dy[i];
            if(nx>=0 && nx<n && ny>=0 && ny<m){
                if(water_day[nx][ny] == 0 && a[nx][ny] == '.'){
                    water_day[nx][ny] = water_day[x][y] + 1;
                    water.push(make_pair(nx, ny));
                }
            }
        }
    }
}

// 최소 이동 시간 계산 BFS
void bfs() {
    queue<pair<int, int>> q;
    q.push(make_pair(start_i, start_j));
    while(!q.empty()){
        int x = q.front().first;
        int y = q.front().second;
        q.pop();

        for(int i=0; i<4; i++){
            int nx = x + dx[i];
            int ny = y + dy[i];
            if(nx>=0 && nx<n && ny>=0 && ny<m){
                if(check[nx][ny] == 0 && (a[nx][ny] == '.' || a[nx][ny] == 'D')){
                    // 도착점은 바로 큐에 넣어줍니다.
                    if(water_day[nx][ny] == 0){
                        check[nx][ny] = check[x][y] + 1;
                        q.push(make_pair(nx, ny));
                    }else{
                        // 이동하려는 칸이 다음날 물이 차오르지 않는다면 큐에 넣어줍니다.
                        if(water_day[nx][ny] > check[x][y] + 1){
                            check[nx][ny] = check[x][y] + 1;
                            q.push(make_pair(nx, ny));
                        }
                    }
                }
            }
        }
    }
}

int main(){
    // 1. 입력
    scanf("%d %d", &n, &m);

    // 지도 정보를 받습니다.
    for(int i=0; i<n; i++){
        scanf("%s", a[i]);
        // 1) 시작점의 i, j를 저장합니다.
        for(int j=0; j<m; j++){
            if(a[i][j] == 'S'){
                start_i = i;
                start_j = j;
            }
            // 2) 도착점의 i, j를 저장합니다.
            else if(a[i][j] == 'D'){
                end_i = i;
                end_j = j;
            }
            // 3) 물을 큐에 넣어줍니다.
            else if(a[i][j] == '*'){
                water.push(make_pair(i, j));
            }
        }
    }

    // 2. 물에 대해 BFS를 수행합니다.
    water_bfs();

    // 3. 고슴도치가 비버굴로 도달하는 BFS를 수행합니다.
    bfs();

    // 4. 출력
    // 만약 도달할 수 있다면 거리 출력
    if(check[end_i][end_j] != 0){
        printf("%d\n", check[end_i][end_j]);
    }
    // 도달 할 수 없다면 KAKTUS 출력
    else{
        printf("KAKTUS\n");
    }
}