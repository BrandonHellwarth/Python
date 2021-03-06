/* 
  String: Reverse
  Given a string,
  return a new string that is the given string reversed
*/

const str1 = "creature";
const expected1 = "erutaerc";

const str2 = "dog";
const expected2 = "god";

const str3 = "hello";
const expected3 = "olleh";

const str4 = "";
const expected4 = "";

/**
 * Reverses the given str.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str String to be reversed.
 * @returns {string} The given str reversed.
 * 
 * pseudo code
 * - create a function that takes in a string
 * - create a newString variable
 * - loop through the given string
 *      - add each letter to a newString variable
 * - return newString
 */
function reverseString(str){
    newstring = [];
    for(i=str.length;i>0;i--){
        newstring.push(str[i - 1]);
    }
    return newstring;
}
console.log(reverseString(str3));

// **************************************************************************

/* 
  Acronyms
  Create a function that, given a string, returns the string’s acronym 
  (first letter of each word capitalized). 
  Do it with .split first if you need to, then try to do it without
*/

const two_str1 = "object oriented programming";
const two_expected1 = "OOP";

// The 4 pillars of OOP
const two_str2 = "abstraction polymorphism inheritance encapsulation";
const two_expected2 = "APIE";

const two_str3 = "software development life cycle";
const two_expected3 = "SDLC";

// Bonus: ignore extra spaces
const two_str4 = "  global   information tracker    ";
const two_expected4 = "GIT";

/**
 * Turns the given str into an acronym.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str A string to be turned into an acronym.
 * @returns {string} The acronym.
 */
function acronymize(str){
    arr = [[]]; //arr[num] needs to be initialy defined
    num = 0;
    for(i=0;i<str.length;i++){ //adds all characters in the string to a nested array and creates a new nested array for each word at a space character
        if(str[i] == " "){
            num++;
            arr.push([]); //need to define a new arr[num] for each space(new word)
        }
        else{
            arr[num].push(str[i]);
        }
    }
    for(i=0;i<arr.length;i++){//checks for empty arrays and removes them
        if(arr[i] == "cda"){
            arr.pop(arr[i]);
        }
    }
    console.log(arr);
    arr1 = [];
    for(i=0;i<arr.length;i++){//adds each nested arrays first index place to a new array and changes it to uppercase
        arr1.push(arr[i][0].toUpperCase());
    }
    return arr1;
}
console.log(acronymize(two_str4));