#螺旋矩阵
class Solution(object):
    def generateMatrix(self, n):
      left,right,top,bottom=0,n-1,0,n-1
      num=1
      mat=[[0]*n for _ in range(n)]
      while left<=right and top<=bottom:
        for j in range(left,right+1):
          mat[top][j]=num
          num+=1
        top+=1
        for i in range(top,bottom+1):
          mat[i][right]=num
          num+=1
        right-=1
        if top<=bottom:
          for j in range(right,left-1,-1):
            mat[bottom][j]=num
            num+=1
          bottom-=1
        if left<=right:
          for i in range(bottom,top-1,-1):
            mat[i][left]=num
            num+=1
          left+=1
      return mat 
