/**
 * @param {number[]} boxes
 * @return {number}
 */
var removeBoxes = function(boxes) {
    const stack=[];
    // 괄호 스택문자랑 비슷한 느낌이지만, 괄호랑 다르게 쌍이 없음..=> 어떻게 푸는지 잘모르겠다..

    // 찾아보니 dp로 해야된다.. 메모이제이션 때문에 3차원이 좋다.

    // const n = boxes.length;
    // if (n === 0) return 0;
    
    // // 3차원 메모이제이션 배열 생성 (n x n x n)
    // // 계산되지 않은 상태는 0으로 초기화합니다.
    // const memo = new Array(n).fill(0).map(() => 
    //     new Array(n).fill(0).map(() => 
    //         new Array(n).fill(0)
    //     )
    // );
    
    // function dp(l, r, k) {
    //     // 구간이 교차하면 0 반환
    //     if (l > r) return 0;
        
    //     // 최적화: 오른쪽 끝에 연속된 같은 색깔의 박스가 있으면 묶어서 처리
    //     // 예: [..., 3, 3] 이라면 r을 하나 줄이고 대기 중인 k를 늘림
    //     while (l < r && boxes[r] === boxes[r - 1]) {
    //         r--;
    //         k++;
    //     }
        
    //     // 이미 계산된 값이 있다면 바로 반환 (캐싱)
    //     if (memo[l][r][k] > 0) {
    //         return memo[l][r][k];
    //     }
        
    //     // 선택 A: 오른쪽 끝에 있는 박스와 대기 중인 k개의 박스를 바로 터뜨림
    //     let res = dp(l, r - 1, 0) + (k + 1) * (k + 1);
        
    //     // 선택 B: l과 r-1 사이에서 boxes[r]과 같은 색깔을 찾아 중간 부분을 먼저 터뜨림
    //     for (let i = l; i < r; i++) {
    //         if (boxes[i] === boxes[r]) {
    //             // dp(i + 1, r - 1, 0): 중간에 끼어있는 다른 색깔들을 먼저 터뜨림
    //             // dp(l, i, k + 1): 왼쪽 남은 부분과 오른쪽의 박스들을 연결해서 마저 풂
    //             res = Math.max(res, dp(i + 1, r - 1, 0) + dp(l, i, k + 1));
    //         }
    //     }
        
    //     // 계산 결과를 기록하고 반환
    //     memo[l][r][k] = res;
    //     return res;
    // }
    
    // // 처음부터 끝까지, 뒤에 대기 중인 박스는 0개인 상태로 시작
    // return dp(0, n - 1, 0);
};