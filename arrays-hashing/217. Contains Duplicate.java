import java.util.*;

class Solution {
    public boolean containsDuplicate(int[] nums) {
        Set<Integer> seen = new HashSet<>();
        for (Integer i : nums) {
            if (seen.contains(i)) {
                return true;
            }
            seen.add(i);
        }
        return false;
    }
}
