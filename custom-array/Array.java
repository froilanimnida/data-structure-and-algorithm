public class Array {
    // instance variables
    private int[] arr;
    // count variable
    private int count;
    // constructor
    public Array(int length) {
        arr = new int[length];
    }

    public void print() {
    // printing out all the array content to console but only up to the count
        for (int j = 0; j < count; j++) {
            // printing out the array content
            System.out.println(arr[j]);
        }
    }

    public void insert(int item) {
        if (arr.length == count) {
            // Create a new array with extra slot for moving items and prevent out of bounds
            int[] copy = new int[count * 2];
            // Copy elements from the old array to the new array
            for (int i = 0; i < count; i++) {
                copy[i] = arr[i];
            }
            arr = copy; // Update the reference to the new array
        }
        // Add the new item at the end by getting and incrementing the count because the count is the next available index
        arr[count++] = item;
    }

    public void removeAt(int index) {
        // Validate the index
        if (index < 0 || index >= count){
            throw new IllegalArgumentException();
        }
        // Shift the items to the left to fill the hole
        // 
        for (int i = index; i < count; i++) {
            arr[i] = arr[i + 1];
        }
        // Decrement the count to indicate that an item has been removed
        count--;
    }

    public int indexOf(int item) {
        // best case is O(1) if the item is at the first index
        // worst case is O(n) if the item is at the last index
        for (int x = 0; x < arr.length; x++) {
            if (arr[x] == item) {
                return x;
            }
        }
        return -1;
    }
}
