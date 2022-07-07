const str1 = "aaaabbcdddaa";
const expected1 = "a4b2c1d3a2";

const str2 = "";
const expected2 = "";

const str3 = "a";
const expected3 = "a";

const str4 = "bbcc";
const expected4 = "bbcc";

function encodeStr(str){
    arr = [];
    num = -1;
    for(i=0;i<str.length;i++){
        if(str[i] != str[i - 1]){
            num++;
            arr.push([]);
        }
        arr[num].push(str[i]);
    }
    newstr = "";
    for(i=0;i<arr.length;i++){
        newstr += arr[i][0] += arr[i].length;
    }
    console.log(newstr);
}
encodeStr(str1);

const two_str1 = "a3b2c1d3";
const two_expected1 = "aaabbcddd";

const two_str2 = "a3b2c12d10";
const two_expected2 = "aaabbccccccccccccdddddddddd";

function decodeStr(str){
    arr = [[]];
    num = 0;
    for(i=0;i<str.length;i++){
        if(isNaN(str[i])){
            if(isNaN(str[i + 2])){
                arr[num].push(str[i], str[i+1]);
                num++;
                arr.push([]);
            }
            else{
                arr[num].push(str[i], str[i+1], str[i+2]);
                num++;
                arr.push([]);
            }
        }
    }
    arr.pop();
    newstr = "";
    for(i=0;i<arr.length;i++){
        if(arr[i].length > 2){
            newint = "" + arr[i][1] + arr[i][2];
            for(a=0;a<newint;a++){
                newstr += arr[i][0];
            }
        }
        else{
            for(a=0;a<arr[i][1];a++){
                newstr += arr[i][0];
            }
        }
    }
    console.log(newstr);
}
decodeStr(two_str2);