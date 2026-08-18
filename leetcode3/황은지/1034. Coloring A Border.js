/**
 * @param {number[][]} grid
 * @param {number} row
 * @param {number} col
 * @param {number} color
 * @return {number[][]}
 */
var colorBorder = function(grid, row, col, color) {
    function doBFS(r,c,color,prevColor){
        const visited=Array.from({length:grid.length},Array(grid[0].length).fill(false);)
        const queue=[[row,col]];
        if(prevColor===grid[r][c]){
            visited[r][c]=true;

        }
    }
    doBFS(row,col,color)
};