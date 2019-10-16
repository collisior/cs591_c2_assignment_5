package cs591_c2_assignment_5;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

class FirstMissingPositiveIntegerTest {

	@BeforeEach
	void setUp() throws Exception {
	}

	@Test
	void testAllPositiveNums() {
		int[] nums = {1,2,0};

		Assertions.assertEquals(3, FirstMissingPositiveInteger.firstMissingPositiveInteger(nums));
	}
	
	@Test
	void TestBothPositiveAndNegativeNums() {
		int[] nums = {3,4,-1,1};
		Assertions.assertEquals(2, FirstMissingPositiveInteger.firstMissingPositiveInteger(nums));

	}
	
	@Test
	void testAllNegativeNums() {
		int[] nums = {-331,-11,-1};

		Assertions.assertEquals(1, FirstMissingPositiveInteger.firstMissingPositiveInteger(nums));
	}

}
