class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        arr=[]
        for i,j in enumerate(words):
            if x in j:
                arr.append(i)
        return arr

            
        