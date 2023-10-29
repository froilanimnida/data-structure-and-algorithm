public class Main {
  public static void main(String args[]) {
    // instantiate with a value to be passed on array length
    Array arr = new Array(3);
    // inserting a value
    arr.insert(25);
    // inserting a value
    arr.insert(50);
    // inserting a value
    arr.insert(55);
    // printing all the contents
    arr.print();
    // should be index 2
    System.out.println(arr.indexOf(55));
    // should be -1 since it doesn't exist
    System.out.println(arr.indexOf(75));
    arr.insert(85);
    arr.insert(100);
    arr.print();
    arr.removeAt(0);
    arr.print();
  }
} 