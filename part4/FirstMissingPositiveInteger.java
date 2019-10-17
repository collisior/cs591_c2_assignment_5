

import java.util.Hashtable;

public class FirstMissingPositiveInteger {
	
	public static int firstMissingPositiveInteger(int[] array) {//assumes input is a list of integers
		Hashtable<Integer, Integer> h = 
                new Hashtable<Integer, Integer>();
		for (int i=0;i<array.length;i++) {
			h.put(array[i], 0);
		}
		
		int min =1;
		while (true) {//assumes input does not contain numbers that exceed the maximum value for an integer in java
			if (!h.containsKey(min)) {
				return min;
			}
			min++;
		}
		
		
	}



public static void main(String[] args) {
	int[] nums = {3,4,-1,1};
	System.out.println(FirstMissingPositiveInteger.firstMissingPositiveInteger(nums));
}
}
