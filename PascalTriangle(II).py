class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        pas=[[1],[1,1]]
        if rowIndex>1:
            for i in range(rowIndex-1):
                curr=[1]    #curr means current row
                last=pas[-1]  # last means previous row
                for i in range(len(last)-1):
                    curr.append(last[i]+last[i+1])
                curr.append(1)
                pas.append(curr)
        return pas[rowIndex]


"""
Example 1:
Input: rowIndex = 3
Output: [1,3,3,1]

Example 2:
Input: rowIndex = 0
Output: [1]

Example 3:
Input: rowIndex = 1
Output: [1,1]
"""