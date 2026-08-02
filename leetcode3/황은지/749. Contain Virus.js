/**
 * @param {number[][]} isInfected
 * @return {number}
 */
var containVirus = function(isInfected) {
    const row=isInfected.length;
    const col=isInfected[0].length;
    const dir=[[0,1],[1,0],[0,-1],[-1,0]];
    let walls=0;
    const visited=Array.from({length:row},()=>Array(col).fill(false));

    for(let i=0;i<row;i++){
        for(let j=0;j<col;j++){
            if(isInfected[i][j]==1 && !visited[i][j]){
                // 아직 방문 안했으면 bfs돌리기
                const queue=[[i,j]];
                visited[i][j]=true;
                let head=0; 

                while(head<queue.length){
                    const [r,c]=queue[head++];
                    for(const [dr,dc] of dir){
                        const nr=r+dr;
                        const nc=c+dc;

                        if(nr>=0 && nr<row && nc>=0 && nc<col){
                            if(isInfected[nr][nc]===1 && !visited[nr][nc]){
                                visited[nr][nc]=true;
                                queue.push([nr,nc]);
                            }
                        }
                    }
                }
            }
        }
        // bfs로 진행하는건 알겠는데, 벽 갯수를 비교하는 방법을 모르겠다.. 계속 돌리면서 저장해야되는걸까?
    }

    return walls;
};