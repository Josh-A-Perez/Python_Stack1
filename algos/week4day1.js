const nums1 = [1, 2, 3];
const expected1 = 6;


function sumArr(nums) {
  var add = 0;
    if(nums.length <= 0){
      return 0;
    }
    console.log(nums[0])
    add = add + nums[0]
    sumArr(nums.slice(1));
    // console.log(add)
    return add

}

console.log(sumArr(nums1))