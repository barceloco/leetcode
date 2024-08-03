class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_set<char> seen;
        int maxLength = 0;
        int left = 0;
        for (int right=0; right<s.length(); right++){
            while (seen.count(s[right]) > 0) {
                seen.erase(s[left]);
                left++;
            }
            seen.insert(s[right]);
            maxLength = max(right - left + 1, maxLength);
        }
        return maxLength;
    }
};