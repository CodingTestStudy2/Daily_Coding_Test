/**
 * @param {string} order
 * @param {string} s
 * @return {string}
 */
var customSortString = function(order, s) {
    const map=new Map()
    let result=""

    for(const alpha of order){
        map.set(alpha,0);
    }

    const rest=[];
    for(const alpha of s){
        if(map.has(alpha)) map.set(alpha,map.get(alpha)+1);
        else rest.push(alpha)
    }

    for (const [key, value] of map) {
        if(value!==0) result+=(key.repeat(value));    
    }

    return result+rest.join("");
};