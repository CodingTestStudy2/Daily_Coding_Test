/*
1. 아이디어:
   - 그래프 구조에서 특정 노드 기준 거리가 k인 노드들을 체크
   - 그 노드들의 비디오 자료를 확인 후 커스텀 정렬 (1. 빈도수 2. 알파벳)
   - 비디오 제목은 가짓수가 26^8이므로 hashmap 자료구조 사용
   - 또한 friends가 이미 그래프 구조이므로 별도 그래프 구조체를 만들지 않음

2. 시간복잡도: O(N + E + U log U) (N: 친구 수, E: 친구 관계 수, U: 고유 비디오 수)

3. 자료구조/알고리즘: BFS + 커스텀 정렬 + HashMap
*/
class Solution {

    private class Info {
        String title;
        int cnt;

        public Info (String title, int cnt) {
            this.title = title;
            this.cnt = cnt;
        }
    };

    public List<String> watchedVideosByFriends(List<List<String>> watchedVideos, int[][] friends, int id, int level) {

        List<Integer> friend = bfs(friends, id, level);

        Map<String, Integer> map = new HashMap<>();

        // 비디오 계산
        for(int i : friend) {
            for(String video : watchedVideos.get(i)) {
                if(!map.containsKey(video)) map.put(video, 1);
                else map.put(video,map.get(video)+1);
            }
        }

        List<Info> info = new ArrayList<>();

        // 구조체 삽입
        for(String key : map.keySet()) {
            info.add(new Info(key, map.get(key)));
        }

        Collections.sort(info, (a,b) ->{
            if(a.cnt == b.cnt) return a.title.compareTo(b.title);
            return a.cnt - b.cnt;
        });

        List<String> ans = new ArrayList<>();
        
        for(Info i : info) {
            ans.add(i.title);
        }

        return ans;
    }

    private List<Integer> bfs(int[][] friends, int id, int level){
        Deque<int[]> dq= new ArrayDeque<>();
        boolean[] visited= new boolean[friends.length];

        List<Integer> friend = new ArrayList<>();
        
        dq.add(new int[]{id, 0});
        visited[id] = true;

        while(!dq.isEmpty()) {
            int curr[] = dq.poll();

            int currId = curr[0];
            int depth = curr[1];

            if(depth == level) friend.add(currId);

            for(int next : friends[currId]) {

                if(visited[next] || depth>level) continue;

                dq.add(new int[]{next,depth+1});
                visited[next] = true;
            }
        }

        return friend;
    }
}