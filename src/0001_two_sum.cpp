class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> numMap;
        for (int i=0; i<nums.size(); i++){
            // if (numMap.count(nums[i])) {
            if (numMap.find(nums[i])!=numMap.end()) {
                return {numMap[nums[i]], i};
            } else {
                // numMap.insert({target-nums[i],i});
                numMap[target-nums[i]]=i;
            }
        }
        return {};
    }
};