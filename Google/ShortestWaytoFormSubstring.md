## Shortest Way to Form Substring

Given 2 strings `target` and `source`, find the minimum number of steps to make `target` a substring of `source`. In 1 step you can take a substring of `source` and append it at the end of `source`.

**Example 1:**
```aidl
Input: target = "abcd", source = "dbcfda"
Output: 2
Explanation:
The target string can be constracted as follow "dbcfda" + "bc" + "d" = "dbcfdabcd"
So the minimum number of steps is 2.
```

**Example 2:**
```aidl
Input: target = "abc", source = "abdabb"
Output: -1
```

**Example 3:**
```aidl
Input: target = "abcd", source = "fabcda"
Output: 0
```