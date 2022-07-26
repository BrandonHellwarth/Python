/* 
Recursively sum an arr of ints
*/

const nums1 = [1, 2, 3];
const expected1 = 6;

const nums2 = [1];
const expected2 = 1;

const nums3 = [];
const expected3 = 0;

/**
 * Add params if needed for recursion
 * Recursively sums the given array.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<number>} nums
 * @returns {number} The sum of the given nums.
 */
sum = 0;
function sumArr(nums, i=0) {
    sum = sum + nums[i];
    if(i == nums.length-1){
    console.log(sum);
    }
    // edge case (pri 1)
    if(nums.length == 0){
        console.log(0);
        return 0;
    }
    // base case (pri 0)
    if (i === nums.length){
        return 0;
    }
    // recursive call (pri 0)
    return nums[i] + sumArr(nums, i+=1);
}
// sumArr(nums3);

/*****************************************************************************/

/* 
Recursive Sigma
Input: integer
Output: sum of integers from 1 to Input integer
*/

const two_num1 = 5;
const two_expected1 = 15;
// Explanation: (1+2+3+4+5)

const two_num2 = 2.9;
const two_expected2 = 3;
// Explanation: (1+2)

const two_num3 = -1;
const two_expected3 = 0;

/**
 * Recursively sum the given int and every previous positive int.
 * - Time: O(?).
 * - Space: O(?).
 * @param {number} num
 * @returns {number}
 */
function checkForDecimal(num){
    if(num % 1 != 0){
        return true;
    }
    else{
        return false;
    }
}
sum = 0;
function recursiveSigma(num, i=1) {
    if(checkForDecimal(num)){
        num = Math.floor(num);
    }
    if(num < 0){
        console.log(0);
        return 0;
    }
    if(i == num + 1){
        return 0;
    }
    sum += i;
    if(i == num){
    console.log(sum);
    }
    return recursiveSigma(num, i+=1);
}
recursiveSigma(two_num3);