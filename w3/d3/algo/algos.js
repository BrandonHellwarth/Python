/* 
Given a SORTED array of integers, dedupe the array 
Because array elements are already in order, all duplicate values will be grouped together.
Ok to use a new array
*/

const nums1 = [1, 1, 1, 1];
const expected1 = [1];

const nums2 = [1, 1, 2, 2, 3, 3];
const expected2 = [1, 2, 3];

const nums3 = [1, 1, 2, 3, 3, 4];
const expected3 = [1, 2, 3, 4];

const nums4 = [1, 1];
const expected4 = [1];

/**
 * De-dupes the given sorted array.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<number>} nums
 * @returns {Array<number>} The given array deduped.
 */
function dedupeSorted(sortedNums) {
    newarr = [0];
    for(i=0;i<sortedNums.length;i++){
        for(a=0;a<newarr.length;a++){
            if(sortedNums[i] != newarr[a]){
                if(a == newarr.length - 1){
                    newarr.push(sortedNums[i]);
                }
            }
            else{
                break;
            }
        }
    }
    newarr.splice(0,1);
    console.log(newarr);
}

// dedupeSorted(nums4);

/* 
Given an array of integers
return the first integer from the array that is not repeated anywhere else
If there are multiple non-repeated integers in the array,
the "first" one will be the one with the lowest index.
*/

const numsA = [3, 5, 4, 3, 4, 6, 5];
const expectedA = 6;

const numsB = [3, 5, 5];
const expectedB = 3;

const numsC = [3, 3, 5];
const expectedC = 5;

const numsD = [5];
const expectedD = 5;

const numsE = [];
const expectedE = null;

const numsF = [1,4,5,5,6,6]
const expectedF = 1;

/**
 * Finds the first int from the given array that has no duplicates. I.e., the
 *    item at the lowest index that doesn't appear again in the given array.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<number>} nums
 * @returns {number|null} The first int value from the given array that has no
 *    dupes or null if there is none.
 */
function firstNonRepeated(nums) {
    if(nums.length == 0){
        console.log("null");
        return null;
    }
    newarr = [0];
    for(i=0;i<nums.length;i++){
        for(a=0;a<newarr.length;a++){
            if(nums[i] != newarr[a]){
                if(a == newarr.length - 1){
                    newarr.push(nums[i]);
                }
            }
            else{
                break;
            }
        }
    }
    newarr.splice(0,1);
    console.log(newarr);
    for(i=0;i<newarr.length;i++){
        num = 0;
        for(a=0;a<nums.length;a++){
            if(newarr[i] == nums[a]){
                num++;
            }
            if(num > 1){
                break;
            }
            if(num == 1 && a == nums.length - 1){
                console.log(newarr[i]);
                return newarr[i];
            }
        }
    }
}
firstNonRepeated(numsF);