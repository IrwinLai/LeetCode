class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        if N == 1 or not dislikes:
            return True
        
        def helper( person_id, color ):
            # Draw person_id as color
            color_table[person_id] = color
            # Draw the_other, with opposite color, in dislike table of current person_id
            for the_other in dislike_table[ person_id ]:
                if color_table[the_other] == color:
                    # the_other has the same color of current person_id
                    return False
                if color_table[the_other] == 0 and (not helper( the_other, -color)):
                    return False
            return True
        
        # each person maintain a list of dislike
        dislike_table = collections.defaultdict( list )
        color_table = [ 0 for _ in range(N+1) ]
        
        for p1, p2 in dislikes:
            dislike_table[p1].append( p2 )
            dislike_table[p2].append( p1 )
            
        # Try to draw dislike pair with different colors in DFS
        for person_id in range(1, N+1):
            if color_table[person_id] == 0 and (not helper( person_id, 1)):
                return False 
        
        return True