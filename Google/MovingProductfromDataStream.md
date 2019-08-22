## Moving Product from Data Stream

Design a data structure to calculate the moving product of all elements in a sliding window of size `k`.

```aidl
class SlidingWindow {

    public SlidingWindow(int k) {
    }
    
    public void add(int val) {
    }
    
    public int getProduct() {
    }
    
}
```

All methods should work in O(1) time.

**Example:**
```aidl
SlidingWindow window = new SlidingWindow(3);
window.add(1); // [1]
window.add(2); // [1, 2]
window.getProduct(); // 2
window.add(3); // [1, 2, 3]
window.getProduct(); // 6
window.add(4); // [2, 3, 4]
window.getProduct(); // 24
```

You can assume that a product will fit into a single 32-bit integer without overflowing.