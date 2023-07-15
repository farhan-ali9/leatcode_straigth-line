class Solution(object):
    def checkStraightLine(self, coordinates):
        """
        :type coordinates: List[List[int]]
        :rtype: bool
        """
        ax,ay=coordinates[1][0]-coordinates[0][0],coordinates[1][1]-coordinates[0][1]
        for bx,by in coordinates[2:]:
            dx,dy=bx-coordinates[0][0],by-coordinates[0][1]
            if dx* ay!=dy*ax:
                return False
        return True
