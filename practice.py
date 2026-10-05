
                                            # Two Sum    1

# class Solution:
#     def twoSum(self,num,target):
#         for i in range(len(num)):
#             for j in range(i+1,len(num)):
#                 if num[i]+num[j]==target:
#                     return[i,j]



                                                    # remove Element
                                                        
# class Solution:
#     def removeElement(self,arr,target):
#         i=0
#         for j in range(len(arr)):
#             if arr[j]!=target:
#                 arr[i]=arr[j]
#                 i+=1
#         return i                    


                                                #  Reverse String
# class Solution:
#     def reverseString(self,arr):
#         left=0
#         right=len(arr)-1
#         while left<right:
#             arr[left],arr[right]=arr[right],arr[left]
#             left+=1
#             right-=1            


                                                    # Move Zeroes
# class Solution:
#     def moveZeroes(self,arr):
#         left=0
#         for right in range(len(arr)):
#             if arr[right]!=0:
#                 arr[left],arr[right]=arr[right],arr[left]
#                 left+=1
#         return arr 

                                                            
                                                    # Two Sum II - Input Array Is Sorted
# class Solution:
#     def twoSum(self,arr,target):
#         left=0
#         right=len(arr)-1
#         while left<right:
#             sum = arr[left] + arr[right]
#             if sum==target:
#                 return [left+1,right+1]
#             elif sum<target:
#                 left+=1
#             else:
#                 right-=1
                                                      
                                             # Container With Most Water
# class Solution:
#     def maxArea(self,arr):
#         left=0
#         right=len(arr)-1
#         maxarea=0
#         while left<right:
#             area=min(arr[left], arr[right]) * (right-left)
#             maxarea=max(maxarea,area)
#             if arr[left] < arr[right]:
#                 left+=1
#             else:
#                 right-=1
#         return maxarea

                                            # Remove Duplicates from Sorted Array
# class Solution:
#     def removeDuplicates(self,arr):
#         i=0
#         for j in range(len(arr)):
#             if arr[i]!=arr[j]:
#                 i+=1
#                 arr[i]=arr[j]
#         return i+1

                                                # Contains Duplicate
# class Solution:
#     def containsDuplicate(self,arr):
#         num=set()
#         for n in arr:
#             if n in num:
#                 return True
#             num.add(n)
#         return False

  
                                                    # 3Sum

# class Solution:
#     def threeSum(self, nums):
#         ans = []
#         n = len(nums)
#         nums.sort()
#         for i in range(n):
#             if i!=0 and nums[i]==nums[i-1]:
#                 continue
#             j=i+1
#             k=n-1
#             while j<k:
#                 total_sum=nums[i]+nums[j]+nums[k]
#                 if total_sum<0:
#                     j+=1
#                 elif total_sum >0:
#                     k-=1
#                 else:
#                     temp=[nums[i],nums[j],nums[k]]
#                     ans.append(temp)
#                     j+=1
#                     k-=1
#                     while j<k and nums[j]==nums[j-1]:
#                         j+=1
#                     while j<k and nums[k]==nums[k+1]:
#                         k-=1
#         return ans

                                                            
                                             # Maximum Average Subarray I  in JAVA CODE
# class Solution {
#     public double findMaxAverage(int[] nums, int k) {
#         int currentSum = 0;
#         for (int i = 0; i < k; i++) {
#             currentSum += nums[i];
#         }
#         int maxSum = currentSum;
#         for (int i = k; i < nums.length; i++) {
#             currentSum = currentSum - nums[i - k] + nums[i];
#             if (currentSum > maxSum) {
#                 maxSum = currentSum;
#             }
#         }
#         return (double) maxSum / k;
#     }
# }



                                                 # Minimum Size Subarray Sum
# class Solution:
#     def minSubArrayLen(self, target, nums):
#         l, total = 0, 0
#         res = float("inf")
#         for r in range(len(nums)):
#             total += nums[r]
#             while total >= target:
#                 res = min(r - l + 1, res)
#                 total -= nums[l]
#                 l += 1

#         return 0 if res == float("inf") else res


                                            # Maximum Number of Vowels in a Substring of Given Length
# class Solution:
#     def maxVowels(self, s, k):
#         vowels = "aeiou"
#         count = 0
#         for i in range(k):
#             if s[i] in vowels:
#                 count += 1
#         max_count = count
#         for i in range(k, len(s)):
#             if s[i] in vowels:
#                 count += 1
#             if s[i - k] in vowels:
#                 count -= 1
#             max_count = max(max_count, count)
#         return max_count


                                     # Longest Substring Without Repeating Characters

# class Solution:
#     def lengthOfLongestSubstring(self, s):
#         left = 0
#         char_set = set()
#         max_length = 0
#         for right in range(len(s)):
#             while s[right] in char_set:
#                 char_set.remove(s[left])
#                 left += 1
#             char_set.add(s[right])
#             max_length = max(max_length, right - left + 1)
#         return max_length


                                        # Max Consecutive Ones III    

# class Solution:
#     def longestOnes(self, nums, k):
#         left = 0
#         zeros = 0
#         max_length = 0
#         for right in range(len(nums)):
#             if nums[right] == 0:
#                 zeros += 1
#             while zeros > k:
#                 if nums[left] == 0:
#                     zeros -= 1
#                 left += 1
#             max_length = max(max_length, right - left + 1)
#         return max_length


                                                # Fruit Into Baskets

# class Solution:
#     def totalFruit(self, fruits):
#         left = 0
#         count = {}
#         max_length = 0
#         for right in range(len(fruits)):
#             count[fruits[right]] = count.get(fruits[right], 0) + 1
#             while len(count) > 2:
#                 count[fruits[left]] -= 1
#                 if count[fruits[left]] == 0:
#                     del count[fruits[left]]
#                 left += 1
#             max_length = max(max_length, right - left + 1)
#         return max_length


                            # Longest Repeating Character Replacement

# class Solution:
#     def characterReplacement(self, s, k):
#         left = 0
#         count = {}
#         max_freq = 0
#         max_length = 0
#         for right in range(len(s)):
#             count[s[right]] = count.get(s[right], 0) + 1
#             max_freq = max(max_freq, count[s[right]])
#             while (right - left + 1) - max_freq > k:
#                 count[s[left]] -= 1
#                 left += 1
#             max_length = max(max_length, right - left + 1)
#         return max_length


                                # Minimum Window Substring
 

# class Solution:
#     def minWindow(self, s, t):
#         if not s or not t:
#             return ""
#         need = {}
#         for ch in t:
#             need[ch] = need.get(ch, 0) + 1
#         window = {}
#         left = 0
#         have = 0
#         need_count = len(need)
#         result = ""
#         result_length = float("inf")
#         for right in range(len(s)):
#             ch = s[right]
#             window[ch] = window.get(ch, 0) + 1
#             if ch in need and window[ch] == need[ch]:
#                 have += 1
#             while have == need_count:
#                 if right - left + 1 < result_length:
#                     result = s[left:right + 1]
#                     result_length = right - left + 1
#                 left_ch = s[left]
#                 window[left_ch] -= 1
#                 if left_ch in need and window[left_ch] < need[left_ch]:
#                     have -= 1
#                 left += 1
#         return result



                             # LeetCode 1 — Two Sum ka HashMap solution

# class Solution:
#     def twoSum(self, nums, target):
#         seen = {}

#         for i in range(len(nums)):
#             complement = target - nums[i]

#             if complement in seen:
#                 return [seen[complement], i]

#             seen[nums[i]] = i


                             # Contains Duplicate ka simple HashSet solution


# class Solution:
#     def containsDuplicate(self, nums):
#         seen = set()
#         for num in nums:
#             if num in seen:
#                 return True
#             seen.add(num)
#         return False

                                              # Valid Anagram
# class Solution:
#     def isAnagram(self, s, t):
#         if len(s) != len(t):
#             return False
#         count = {}
#         for ch in s:
#             count[ch] = count.get(ch, 0) + 1
#         for ch in t:
#             if ch not in count:
#                 return False
#             count[ch] -= 1
#             if count[ch] < 0:
#                 return False
#         return True


                                    # 387. First Unique Character in a String
# class Solution:
#     def firstUniqChar(self, s):
#         count = {}
#         for ch in s:
#             count[ch] = count.get(ch, 0) + 1
#         for i in range(len(s)):
#             if count[s[i]] == 1:
#                 return i
#         return -1







        









