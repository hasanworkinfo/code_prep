
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