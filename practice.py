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