brothers = ['tyler', 'curtis', 'joe'];
for(const brother of brothers){
    console.log(brother);
}

function randomizeArray(arr){
    returnarr = [];
    for(i=0;i<brothers.length;i++){
        randomnum = Math.floor(math.random() * brothers.length);
        item = arr[randomnum];
        returnarr.push(item);
    }
    return returnarr;
}
console.log(randomizeArray(brothers));