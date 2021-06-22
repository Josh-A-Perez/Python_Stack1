const arrA1 = [1, 2, 3];
const arrB1 = ["a", "b", "c"];
const expected1 = [1, "a", 2, "b", 3, "c"];

const arrA2 = [1, 3];
const arrB2 = [2, 4, 6, 8];
const expected2 = [1, 2, 3, 4, 6, 8];

const arrA3 = [1, 3, 5, 7];
const arrB3 = [2, 4];
const expected3 = [1, 2, 3, 4, 5, 7];
[42, 0, 6];
const expected4 = [42, 0, 6];
const arrA4 = [];
const arrB4 =

function interleaveArrays(arr1, arr2) {
    console.log(arr1, arr2)
    var arr3 = [];
    for(i = 0 ; i < arr1.length; i++){
    arr3.push(arr1[i], arr2[i])
    console.log(arr3)
    }

}
interleaveArrays(arrA1, arrB1)