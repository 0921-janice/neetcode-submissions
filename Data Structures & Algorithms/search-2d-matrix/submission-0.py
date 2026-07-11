class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top_r, bottom_r = 0, len(matrix) - 1

        while top_r <= bottom_r: 
            mid_r = top_r + (bottom_r - top_r)//2
            print(top_r, bottom_r, mid_r)
            print(matrix[mid_r])
            if target >= matrix[mid_r][0] and target <= matrix[mid_r][-1]:
                left, right = 0, len(matrix[0]) - 1

                while left <= right:
                    mid = left + (right - left)

                    if matrix[mid_r][mid] == target:
                        return True
                    
                    elif matrix[mid_r][mid] < target:
                        left = mid + 1

                    else:
                        right = mid - 1

                return False


            elif target < matrix[mid_r][0]:               
                bottom_r = mid_r - 1

            else:
                top_r = mid_r + 1
            
        return False
