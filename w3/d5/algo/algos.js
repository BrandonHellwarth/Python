/* 
Array: Mode
Create a function that, given an array of ints,
returns the int that occurs most frequently in the array.
What if there are multiple items that occur the same number of time?
    - return all of them (in an array)
    - what if all items occur the same number of times?
    - return empty array
*/

const nums1 = [];
const expected1 = [];

const nums2 = [1];
const expected2 = [1];

const nums3 = [5, 1, 4];
const expected3 = [];

const nums4 = [5, 1, 4, 1];
const expected4 = [1];

const nums5 = [5, 1, 4, 1, 5];
const expected5 = [5, 1];

const nums6 = [5, 1, 4, 1, 5, 4];
const expected6 = [];
//  - order doesn't matter

/**
 * Finds the mode or all modes if there are more than one. The mode is the
 *    value which occurs the most times in the given array.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<number>} nums Test
 * @returns {Array<number>} Mode or modes in any order.
 */
function mode(nums) {
    if(nums.length == 0){
        console.log(nums);
        return nums;
    }
    newarr = [nums[0]];
    if(nums.length == 1){
        console.log(newarr);
        return newarr;
    }
    num = 0;
    for(i=1;i<nums.length;i++){
        for(a=0;a<newarr.length;a++){
            if(nums[i] == newarr[a]){
                num++;
            }
        }
        if(num == 0){
            newarr.push(nums[i]);
        }
    }
    console.log(newarr);
    length = newarr.length;
    for(i=0;i<length;i++){ //needs work
        num1 = 0;
        for(a=0;a<nums.length;a++){
            if(newarr[i] == nums[a]){
                num1++;
            }
        }
        console.log(num1);
        if(num1 < 2){
            newarr.splice(i,1);
        }
    }
    console.log(newarr)
}
mode(nums3);