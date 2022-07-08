// const keys1 = ["abc", 3, "yo"];
// const vals1 = [42, "wassup", true];
// const expected1 = {
//     yo: true,   
//     abc: 42,
//     3: "wassup",
// };

// const keys2 = [];
// const vals2 = [];
// const expected2 = {};

// const keys3 = ["abc", 3, "yo"];
// const vals3 = [42, "wassup", true, "something"];

// const keys4 = ["abc", 3, "yo", "something"];
// const vals4 = [42, "wassup", true];
// const expected4 = {
//     yo: true,   
//     abc: 42,
//     3: "wassup",
//     something: ""
// };
// function zipArraysIntoMap(keys, values) {
//     newobj = {};
//     if(keys.length > values.length){
//         for(i=0;i<keys.length;i++){
//             if(i >= values.length){
//                 newobj[keys[i]] = 'empty value';
//             }
//             else{
//                 newobj[keys[i]] = values[i];
//             }
//         }
//     }
//     else if(keys.length == values.length){
//         for(i=0;i<values.length;i++){
//             newobj[keys[i]] = values[i]
//         }
//     }
//     else{
//         for(i=0;i<values.length;i++){
//             if(i >= keys.length){
//                 newobj.empty_key = values[i];
//             }
//             else{
//                 newobj[keys[i]] = values[i];
//             }
//         }
//     }
//     console.log(newobj);
//     return newobj;
// }
// zipArraysIntoMap(keys2, vals2);

const two_obj1 = { name: "Zaphod", charm: "high", morals: "dicey" };
const two_expected1 = { Zaphod: "name", high: "charm", dicey: "morals" };

const two_obj2 = { name: "Zaphod", charm: "high", morals: "dicey", something:1 };
const two_expected2 = { Zaphod: "name", high: "charm", dicey: "morals", 1:"something" };

const two_obj3 = { name: "Zaphod", charm: "high", morals: "dicey", something:"dicey" };
const two_expected3 = { Zaphod: "name", high: "charm", dicey: ["morals", "something"] };

function invertObj(obj) {
    objkeys = Object.keys(obj);
    console.log(objkeys);
    newobj = {};
    for(i=0;i<objkeys.length;i++){
        invkey = obj[objkeys[i]];
        invval = objkeys[i];
        if(i > 0){
            if(invkey == obj[objkeys[i - 1]]){
                newobj[invkey] = [newobj[invkey], invval];
            }
            else{
                newobj[invkey] = invval;
            }
        }
        else{
            newobj[invkey] = invval;
        }
    }
    console.log(newobj);
    return newobj;
}
invertObj(two_obj1);