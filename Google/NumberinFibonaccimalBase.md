## Number in Fibonaccimal Base

Fibonacci sequence is obtained by adding the two last numbers to get the next one e.g. 1, 2, 3, 5, 8, 13, ...

The sequence appears on many things in our life, in nature, and has a great significance. Among other things, do you know that all positive integer numbers can be represented as a sum of numbers in the Fibonacci sequence? More than that, all positive integers can be represented as a sum of a set of Fibonacci numbers, that is, numbers from the sequence, without repetition. For example: 13 can be the sum of the sets `{13}, {5, 8}` or `{2, 3, 8}` and 17 is represented by `{1, 3, 13}` or `{1, 3, 5, 8}`. Since all numbers have this property this set could be a nice way to use as a "base" to represent the number.

Now that we know all this we can prepare a nice way to represent any positive integer. We will use a binary sequence (just zeros and ones) to do that. For example,
- 17 = 1 + 3 + 13. Let’s write a zero for each Fibonacci number that is not used and one for each one that is used, starting at the right. Then, 17 = 100101.

    ```aidl
    17 =	        1	0	0	1	0	1
    13 + 3 + 1 =	13	8	5	3	2	1
    ```
    
- 10 can be written as 8 + 2 ==> 10010

    ```aidl
    10 =	    1	0	0	1	0
    8 + 2 =	    8	5	3	2	1
    ```

In this representation we should not have zeros at the left, this is, we should only write starting with the first one. When we use this representation for a number we say that we are using the Fibonaccimal base. Given an int `n`, return all possible representations of `n` in Fibonaccimal base.  

**Example:**
```aidl
Input: 10
Output: [10010, 1110]
Explanation:
10 = 8 + 2 ==> 10010
10 = 5 + 3 + 2 ==> 1110
```

Original Post: https://leetcode.com/discuss/interview-question/363898/google-number-in-fibonaccimal-base 