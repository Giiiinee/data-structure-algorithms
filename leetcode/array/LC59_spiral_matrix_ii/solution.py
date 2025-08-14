#螺旋矩阵
class Solution(object):
    def generateMatrix(self, n):
      left,right,top,bottom=0,n-1,0,n-1      #将矩阵放在一个边长为n的正方形中，上边界看作top，行索引为0{填完最上面一行 -> top+=1(上边界往下移)},以此类推。
      num=1
      mat=[[0]*n for _ in range(n)]
      while left<=right and top<=bottom:     #表示只要当前的矩形区域还存在，就继续画螺旋。
        for j in range(left,right+1):
          mat[top][j]=num
          num+=1
        top+=1                               #注意是在for循环完成后，即一整行完成填数。
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
