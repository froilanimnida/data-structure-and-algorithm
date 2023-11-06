public class ReverseString {
	public static void main(String[] args) {
		String str = "ABCD";
		String newStr = "";
		System.out.println(str);
		for (int y = str.length() - 1; y >= 0; --y) {
		    newStr = newStr + str.charAt(y);
		}
		System.out.println(newStr);
	}
}
