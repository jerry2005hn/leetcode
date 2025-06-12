import java.util.*;

class Solution {
    public int lengthOfLongestSubstring(String s) {
        List<Character> listChars = new ArrayList<>();
        int res = 0;
        for (char c : s.toCharArray()) {
            if (!listChars.contains(c)) {
                listChars.add(c);
                if (res < listChars.size()) {
                    res = listChars.size();
                }
            }
            else {
                int remove = listChars.indexOf(c);
                listChars.add(c);
                listChars = listChars.subList(remove+1,listChars.size());
            }
        }
        return res;
    }
}

/* Optimal
    public class Solution {
    public int lengthOfLongestSubstring(String s) {
        HashMap<Character, Integer> mp = new HashMap<>();
        int l = 0, res = 0;
        
        for (int r = 0; r < s.length(); r++) {
            if (mp.containsKey(s.charAt(r))) {
                l = Math.max(mp.get(s.charAt(r)) + 1, l);
            }
            mp.put(s.charAt(r), r);
            res = Math.max(res, r - l + 1);
        }
        return res;
    }
}
*/
