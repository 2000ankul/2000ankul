#User function Template for python3

class Solution:
    def sum_of_middle_elements(self, arr1, arr2):
    # Ensure arr1 is the smaller array
        if len(arr1) > len(arr2):
            arr1, arr2 = arr2, arr1
        
        n1, n2 = len(arr1), len(arr2)
        
        low, high = 0, n1
        while low <= high:
            partition1 = (low + high) // 2
            partition2 = (n1 + n2 + 1) // 2 - partition1
            
            # Calculate maxLeft1, minRight1, maxLeft2, minRight2
            maxLeft1 = arr1[partition1 - 1] if partition1 > 0 else float('-inf')
            minRight1 = arr1[partition1] if partition1 < n1 else float('inf')
            
            maxLeft2 = arr2[partition2 - 1] if partition2 > 0 else float('-inf')
            minRight2 = arr2[partition2] if partition2 < n2 else float('inf')
            
            # Check if we found the correct partition
            if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:
                # If total number of elements is odd, return max of left halves
                if (n1 + n2) % 2 == 1:
                    return max(maxLeft1, maxLeft2)
                # If total number of elements is even, return average of max of left halves and min of right halves
                else:
                    return (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) 
            
            # If maxLeft1 is greater than minRight2, move the partition left in arr1
            elif maxLeft1 > minRight2:
                high = partition1 - 1
            # If maxLeft2 is greater than minRight1, move the partition right in arr1
            else:
                low = partition1 + 1
            # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys

input = sys.stdin.read


def main():
    input_lines = input().strip().split("\n")
    t = int(input_lines[0])

    index = 1
    results = []
    while t > 0:
        arr = list(map(int, input_lines[index].strip().split()))
        brr = list(map(int, input_lines[index + 1].strip().split()))
        index += 2

        solution = Solution()
        res = solution.sum_of_middle_elements(arr, brr)
        results.append(res)

        t -= 1

    for result in results:
        print(result)


if __name__ == "__main__":
    main()

# } Driver Code Ends