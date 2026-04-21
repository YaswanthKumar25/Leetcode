class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        neg=operations.count("--X")
        neg2=operations.count("X--")
        finalneg=neg2+neg
        pos=operations.count("++X")
        pos2=operations.count("X++")
        finalpos=pos+pos2
        return finalpos-finalneg
        