/*
    Given a sorted array of page numbers where a term appears,
    produce an index string.

    Consecutive pages should form ranges separated by a hyphen.

    EXAMPLE:

    var input = [1, 5, 6, 7, 8, 9, 10, 14, 22, 23, 24, 25, 27];

    var output = "1, 5-10, 14, 22-25, 27";
*/

function bookIndex(pages){
    //cantocate nums
    var output = ""
    var startIndex = 0
    var nextIndex = 0
    //loop
    for(var i = o; i < pages.length; i++){
      if(i = 0){
        output += pages[i] //all starting index of pages go to output
        console.log(output);
      }
      if(pages[i] - 1 != pages[i-1]){
        output += ',' + pages[i]
        console.log(output)
      }
    }
        // if/else ck if only +1 than prev
            // push 1st num + "-" + last num
        // if not push into output
    return output;
}
console.log(bookIndex(input))