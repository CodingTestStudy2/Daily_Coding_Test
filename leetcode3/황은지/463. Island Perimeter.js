/**
 * @param {number[][]} grid
 * @return {number}
 */
var islandPerimeter = function(grid) {

    const ROW=grid.length;
    const COL=grid[0].length;

    //BFS
    function doBFS(startR,startC){
        const DIR=[[-1,0],[0,1],[1,0],[0,-1]]
        const visited=Array.from({length:ROW},()=>Array(COL));
        let count=0;

        visited[startR][startC]=true;
        
        const queue=[[startR,startC]];
        let head=0;

        while(head<queue.length){
            const [curR,curC]=queue[head++];

            for(let i=0;i<4;i++){
                const [nextR,nextC]=[curR+DIR[i][0],curC+DIR[i][1]];
                if(nextR<0 || nextR>=ROW || nextC<0 || nextC>=COL
                || grid[nextR][nextC]===0){
                    count++;
                    continue;
                }
                if(visited[nextR][nextC]) continue;
                visited[nextR][nextC]=true;
                queue.push([nextR,nextC]);
            }
        }
        return count;

    }


    // 실행부
    for(let i=0;i<ROW;i++){
        for(let j=0;j<COL;j++){
            if(grid[i][j]===1) return doBFS(i,j);
        }
    }

    
};