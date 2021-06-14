Object.assign(newObject, {key1[i]: vals[i]})

const keys1 = ["abc", 3, "yo"];
const vals1 = [42, "wassup", true];
const expected1 = {
abc: 42,
3: "wassup",
yo: true,
};

function zipArraysIntoObject(ary1, ary2) {
    newObject = {};
    for (var i = 0; i < ary1.length; i++) {
    var keys = ary1[i];
    newObject[ary1[i]] = keys[i]
    }
    for (var j = 0; j < ary2.length; j++) {
    var vals =(ary2[i]);   
    console.log(ary2[j])
    }
    console.log(newObject)

}
zipArraysIntoObject(keys1,vals1)