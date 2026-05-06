public class Day6 {
    public int countCommas(int n) {
        int answer = 0;
        for (int i = 1000; i <= n; i++) {
            answer++;
        }
        return answer;
    }
}
