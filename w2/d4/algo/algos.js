/* 
Parens Valid
Given an str that has parenthesis in it
return whether the parenthesis are valid
*/

const str1 = "Y(3(p)p(3)r)s";
const expected1 = true;

const str2 = "N(0(p)3";
const expected2 = false;
// Explanation: not every parenthesis is closed.

const str3 = "N(0)t ) 0(k";
const expected3 = false;
// Explanation: because the second ")" is premature: there is nothing open for it to close.

const str4 = "a(b))(c";
const expected4 = false;
// Explanation: same number of opens and closes but the 2nd closing closes nothing.

/**
 * Determines whether the parenthesis in the given string are valid.
 * Each opening parenthesis must have exactly one closing parenthesis.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str
 * @returns {boolean} Whether the parenthesis are valid.
 */
function parensValid(str) {
    newstr = "";
    for(i=0;i<str.length;i++){
        if(str[i] == "(" || str[i] == ")"){
            newstr += str[i];
        }
    }
    for(i=0;i<newstr.length;i++){
        if(newstr[i] == "("){
            if(newstr[i+1] == ")" || newstr[i+3] == ")" || newstr[newstr.length-1] == ")"){
                
            }
            else{
                console.log("False");
                return false;
            }
        }
    }
    console.log("True");
    return true;
}
parensValid(str4);
/*****************************************************************************/

/* 
Braces Valid
Given a string sequence of parentheses, braces and brackets, determine whether it is valid. 
*/

const two_str1 = "W(a{t}s[o(n{ c}o)m]e )h[e{r}e]!";
const two_expected1 = true;

const two_str2 = "D(i{a}l[ t]o)n{e";
const two_expected2 = false;

const two_str3 = "A(1)s[O (n]0{t) 0}k";
const two_expected3 = false;

/**
 * Determines whether the string's braces, brackets, and parenthesis are valid
 * based on the order and amount of opening and closing pairs.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str
 * @returns {boolean} Whether the given strings braces are valid.
 */
function bracesValid(str) {
    newstrpar = "";
    newstrbrace = "";
    newstrbrak = "";
    newstr = "";
    for(i=0;i<str.length;i++){
        if(str[i] == "(" || str[i] == ")" || str[i] == "{" || str[i] == "}" || str[i] == "[" || str[i] == "]"){
            newstr += str[i];
        }
    }
    for(i=0;i<str.length;i++){
        if(str[i] == "(" || str[i] == ")"){
            newstrpar += str[i];
        }
        if(str[i] == "{" || str[i] == "}"){
            newstrbrak += str[i];
        }
        if(str[i] == "[" || str[i] == "]"){
            newstrbrace += str[i];
        }
    }
    console.log(newstr);
    console.log(newstrpar);
    console.log(newstrbrace);
    console.log(newstrbrak);
    for(i=0;i<newstr.length;i++){
        if(newstr[i] == "("){
            if(newstr[i+1] == ")" || newstr[i+3] == ")" || newstr[newstr.length-1] == ")"){
                
            }
            else{
                console.log("False");
                return false;
            }
        }
        if(newstr[i] == "{"){
            if(newstr[i+1] == "}" || newstr[i+3] == "}" || newstr[newstr.length-1] == "}"){
                
            }
            else{
                console.log("False");
                return false;
            }
        }
        if(newstr[i] == "["){
            if(newstr[i+1] == "]" || newstr[i+3] == "]" || newstr[newstr.length-1] == "]"){
                
            }
            else{
                console.log("False");
                return false;
            }
        }
    }
    for(i=0;i<newstrpar.length;i++){
        if(newstrpar[i] == "("){
            if(newstrpar[i+1] == ")" || newstrpar[i+3] == ")" || newstrpar[newstrpar.length-1] == ")"){
                
            }
            else{
                console.log("False");
                return false;
            }
        }
    }
    for(i=0;i<newstrbrace.length;i++){
        if(newstrbrace[i] == "["){
            if(newstrbrace[i+1] == "]" || newstrbrace[i+3] == "]" || newstrbrace[newstrbrace.length-1] == "]"){
                
            }
            else{
                console.log("False");
                return false;
            }
        }
    }
    for(i=0;i<newstrbrak.length;i++){
        if(newstrbrak[i] == "{"){
            if(newstrbrak[i+1] == "}" || newstrbrak[i+3] == "}" || newstrbrak[newstrbrak.length-1] == "}"){
                
            }
            else{
                console.log("False");
                return false;
            }
        }
    }
    console.log("True");
    return true;
}
bracesValid(two_str1);