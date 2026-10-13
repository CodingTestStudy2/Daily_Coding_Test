/**
 * @param {number[]} source
 * @param {number[]} target
 * @return {number}
 */

var minQueenMoves = function(source, target) {
    const rowDiff = Math.abs(source[0] - target[0])
    const colDiff = Math.abs(source[1] - target[1])

    if (rowDiff === 0 && colDiff === 0) return 0;
    if (rowDiff === colDiff || rowDiff === 0 || colDiff === 0) return 1;
    return 2;
};