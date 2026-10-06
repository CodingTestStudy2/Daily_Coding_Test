/**
 * @param {number[][]} points
 * @return {number}
 */
 // 한 점 i 를 기준으로 j와 k까지의 거리가 같으면 부메랑이고, (i, j, k)와 (i, k, j)는 서로 다른 것으로 센다.

 // 기준점 하나 선택 - 나머지 모든 점과의 거리 계산 - 같은 거리인 점들이 있는지 확인

var numberOfBoomerangs = function(points) {
    if(points.length < 3) {
        return 0;
    }
    for (let i =0; i<points.length; i++) {

        for (let j=0; j<points.length; j++) {
            if (i===j) continue;

            let dx = points[i][0] - points[j][0];
            let dy = points[i][1] - points[i][1];

            let distance = dx * dx + dy * dy;

        }
    }
};