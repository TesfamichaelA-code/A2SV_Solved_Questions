class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        value_groups = defaultdict(list)

        for i, num in enumerate(nums):
            value_groups[num].append(i)
        
        result = 0
        
        for indices in value_groups.values():
            gcd_count = defaultdict(int)
            
            for i in indices:
                g = gcd(i, k)

                for prev_g in gcd_count:
                    if (g * prev_g) % k == 0:
                        result += gcd_count[prev_g]
                
                gcd_count[g] += 1
        
        return result
        