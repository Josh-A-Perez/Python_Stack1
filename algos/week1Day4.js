/* 
String: Is Palindrome
Create a function that returns a boolean whether the string is a strict palindrome. 
    - palindrome = string that is same forwards and backwards

Do not ignore spaces, punctuation and capitalization
 */

const str1 = "a x a";
const expected1 = true;

const str2 = "racecar";
const expected2 = true;

const str3 = "Dud";
const expected3 = false;

const str4 = "oho!";
const expected4 = false;

function isPalindrome(str) {
  
    for(let i = 0; i < str.length; i++){
      let leftChar = str[i]
      let rightChar = str[str.length - 1 - i]
      if leftChar == rightChar{
      console.log(true)
      }
    }  
}

isPalindrome(str3)




/**
   * Determines if the given str is a palindrome (same forwards and backwards).
   * - Time: O(?).
   * - Space: O(?).
   * @param {string} str
   * @returns {boolean} Whether the given str is a palindrome or not.
   */


  // ******************************************************************************
  // ******************************************************************************
  // ******************************************************************************

/* 
    Longest Palindrome
    For this challenge, we will look not only at the entire string provided, but also at the substrings within it. Return the longest palindromic substring. 
    Strings longer or shorter than complete words are OK.
    All the substrings of "abc" are:
    a, ab, abc, b, bc, c
  */


///const str1 = "what up, daddy-o?";
//const expected1 = "dad";

// const str2 = "uh, not much";
// const expected2 = "u";

// const str3 = "Yikes! my favorite racecar erupted!";
// const expected3 = "e racecar e";

// const str4 = "";
// const expected4 = false;

/**
   * Finds the longest palindromic substring in the given string.
   * - Time: O(?).
   * - Space: O(?).
   * @param {string} str
   * @returns {string} The longest palindromic substring from the given string.
   */
function longestPalindromicSubstring(str) {}

///1. create funtiion that loops strings
///2. check if pal indrome is there
///3. see wich pal indrome has the longest length
///4. .length -1 to see length of each string
///5. console.log longest pal  indrome
