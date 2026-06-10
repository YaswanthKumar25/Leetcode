class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        hash={}
        maxi=float('-inf')
        for i in range(len(grid)):
            for j in range(len(grid)):
                maxi=max(maxi,grid[i][j])
                if grid[i][j] in hash:
                    hash[grid[i][j]]+=1
                else:
                    hash[grid[i][j]]=1
        notnum=maxi+1
        repeat=-1
        for i in range(1,maxi+1):
            if i not in hash.keys():
                notnum=i
            if i in hash.keys():
                if hash[i]>1:
                    repeat=i
        return [repeat,notnum]
                

            
        