function twoSum(nums: number[], target: number): number[] {
    const dict: Record<number, number> = {};
    for (let i = 0; i < nums.length; i++) {
        const find  = target - nums[i];
        if (find in dict) {
            return [dict[find], i];
        }
        dict[nums[i]] = i;
    }
    return [];
};