/* 
Given a string containing space separated words
Reverse each word in the string.
If you need to, use .split to start, then try to do it without.
*/

const str1 = "hello";
const expected1 = "olleh";

const str2 = "hello world";
const expected2 = "olleh dlrow";

const str3 = "abc def ghi";
const expected3 = "cba fed ihg";

/**
 * Reverses the letters in each words in the given space separated
 * string of words. Does NOT reverse the order of the words themselves.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str Contains space separated words.
 * @returns {string} The given string with each word's letters reversed.
 */
function reverseWords(str) {
    arr = [[]];
    num = 0;
    for(i=str.length-1;i>=0;i--){
        if(str[i] == " "){
            num++;
            arr.push([]);
        }
        else{
        arr[num].push(str[i]);
        }
    }
    newstr = "";
    for(i=arr.length-1;i>=0;i--){
        for(a=0;a<arr[i].length;a++){
            newstr += arr[i][a]
        }
        newstr += " ";
    }
    console.log(newstr);
}
reverseWords(str1);

// *************************************************

/* 
Reverse Word Order
Given a string of words (with spaces)
return a new string with words in reverse sequence.
*/

const two_str1 = "This is a test";
const two_expected1 = "test a is This";

const two_str2 = "hello";
const two_expected2 = "hello";

const two_str3 = "   This  is a   test  ";
const two_expected3 = "test a is This";

/**
 * Reverses the order of the words but not the words themselves form the given
 * string of space separated words.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} wordsStr A string containing space separated words.
 * @returns {string} The given string with the word order reversed but the words
 *    themselves are not reversed.
 */
function reverseWordOrder(wordsStr) {
    arr = [[]];
    num = 0;
    for(i=0;i<wordsStr.length;i++){
        if(wordsStr[i] == " "){
            num++;
            arr.push([]);
        }
        else{
        arr[num].push(wordsStr[i]);
        }
    }
    newstr = "";
    console.log(arr);
    for(i=arr.length-1;i>=0;i--){
        console.log(i);
        if(arr[i].length == 0){
            arr.splice(i,1);//.pop can only remove the last element in an array, where as splice can remove an element at a specific index
            console.log(i);
        }
    }
    console.log(arr);
    for(i=arr.length-1;i>=0;i--){
        for(a=0;a<arr[i].length;a++){
            newstr += arr[i][a]
        }
        newstr += " ";
    }
    console.log(newstr);
}
reverseWordOrder(two_str3)