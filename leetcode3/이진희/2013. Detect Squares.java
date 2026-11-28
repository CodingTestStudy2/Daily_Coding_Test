/*

1. 아이디어 : 정사각형을 판별하고 만들 수 있는 개수를 구하는 문제
            두 점을 Key로 HashMap에 저장해 점의 개수를 카운트 한다
            이때 최대 좌표가 작으므로 String 보단 Integer형식으로 하면 빠르다
            
            정사각형이 되려면 1. 네 변의 길이가 같을 것 2. 두 대각선의 길이가 같을 것이다.
            여기선 주어진 점을 대각선으로 두고 x와 y길이가 같은 다른 대각선을 찾는다.
            찾았다면 (p,q) (p2,q2) 라는 두 대각선이 있을때 다른 점은 (p,q2) (p2,q) 로 고정된다.

2. 시간복잡도 : O(N)

3. 자료구조/알고리즘 : HashMap, 정사각형 판별 기준

 */

class DetectSquares {

    private HashMap<Integer, Integer> points;
    private int OFFSET = 1001;

    public DetectSquares() {
        points = new HashMap<>();
    }
    
    // 점 넣기
    public void add(int[] point) {
        int y = point[0];
        int x = point[1];

        int key = y*OFFSET + x;

        points.put(key, points.getOrDefault(key, 0) + 1);
    }
    
    public int count(int[] point) {
        int y = point[0];
        int x = point[1];

        int cnt = 0;

        int oKey = (y*OFFSET)+x;

        for(Integer key : points.keySet()) {
            int ty = key/OFFSET;
            int tx = key%OFFSET;

            if(ty == y && tx == x) continue;
            if(Math.abs(y-ty) != Math.abs(x-tx)) continue;

            int point1 = ty*OFFSET+x;
            int point2 = y*OFFSET+tx;

            if(points.containsKey(point1) && points.containsKey(point2)) {
                cnt+=points.get(point1)*points.get(point2)*points.get(ty*OFFSET+tx);
            }
        }
        return cnt;
    }
}

/**
 * Your DetectSquares object will be instantiated and called as such:
 * DetectSquares obj = new DetectSquares();
 * obj.add(point);
 * int param_2 = obj.count(point);
 */