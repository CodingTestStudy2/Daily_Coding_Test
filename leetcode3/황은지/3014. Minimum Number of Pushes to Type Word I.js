/**
 * @param {string} word
 * @return {number}
 */
var minimumPushes = function(word) {
    // 최대한 한번만 누르게 -> 그래도 부족한건 2개, 3개짜리로..
    let cost=0;
    let click=1;
    let left=word.length;

    while(left>0){
        if(left<=8){
            cost+=(left*(click++))
            break;
        }else{
            left-=8;
            cost+=(8*(click++));
        }
    }

    return cost;
};