class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        """
        Ideally, the strings should differ by only two indices so that
        a single swap in one of the string makes both the strings equal. Now, we
        need to find those indices and make sure the letters also match. We do this
        by:-
        1. Finding the indices where they are different
        """
        if s1==s2:
            return True
        indexes = []
        for i in range(len(s1)):
            if s1[i]!=s2[i]:
                indexes.append(i)
            if len(indexes)>2:
                return False
        if len(indexes)==2:
            i,j = indexes
            return s1[i]==s2[j] and s2[i]==s1[j]
        return len(indexes)==0