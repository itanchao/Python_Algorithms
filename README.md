# Python_Algorithms
Python算法题

* 对以下一组数据进行降序排序（冒泡排序）。

  24，17，85，13，9，54，76，45，5，63

  ```python
  def bubbleSort(array):
      '''
      	思路：从0开始，每一次比较临近的两个元素大小，进行位置互换 
      '''
      num = len(array)
      for i in range(0, num):
          for j in range(0, (num - i - 1)):
              if array[j] < array[j + 1]:
                  tmp = array[j]
                  array[j] = array[j + 1]
                  array[j + 1] = tmp
      return array

  array = [24, 17, 85, 13, 9, 54, 76, 45, 5, 63]
  list1 = bubbleSort(array)
  print(list1)
  ```

  运行结果

  ![运行结果](./image/bubbleSort.png)

* 对以下一组数据进行升序排序（选择排序）。

  86, 37, 56, 29, 92, 73, 15, 63, 30, 8 

  ```python
  def selectSort(array):
      '''
      	思路：每一次查找最小的一个数字转移到第一位 
      '''
      num = len(array)
      for i in range(0, num - 1):
          index = i
          for j in range(i + 1, num):
              if array[index] > array[j]:
                  index = j
          if index != i:
              tmp = array[i]
              array[i] = array[index]
              array[index] = tmp
      return array
  # 对以下一组数据进行升序排序（选择排序）。“86, 37, 56, 29, 92, 73, 15, 63, 30, 8”
  array = [24, 17, 85, 13, 9, 54, 76, 45, 5, 63]
  selectSort(array)
  print(array)
  ```

  运行结果：

  ![运行结果](./image/selectSort.png)

* 二分法查找

  从数组[1,2,3,4,5,6,7,9,20,99,108,120,369,598] 找出108

  ```python
  def binSort(array, goalNum , lowerlimit, toplimit):
      '''
      思想：每一次取中间元素去和目标值进行比较，确定上下限
      :param array: 数组
      :param goalNum: 目标元素
      :param lowerlimit: 下限
      :param toplimit: 上限
      :return: 目标元素的下标
      '''
      if lowerlimit < toplimit:
          mid = int((toplimit + lowerlimit)/2)
          if goalNum == array[mid]:
              return mid + 1
          else:
              return binSort(array,goalNum,mid+1,toplimit) if (goalNum > array[mid]) else binSort(array,goalNum,lowerlimit,mid-1)

  array = [1,2,3,4,5,6,7,9,20,99,108,120,369,598]
  index = binSort(array,goalNum= 108, lowerlimit = 0, toplimit= len(array)-1)
  print(index)
  ```

  运行结果：

  ![运行结果](./image/binarychop.png)

* 路径搜索

  S为开始点，G为终点，从S点出发前往G点，‘#’ 是不能通过的点

  |  #   |  S   |  #   |  #   |  #   |  #   |  #   |  #   |  .   |  #   |
  | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
  |  .   |  .   |  .   |  .   |  .   |  .   |  #   |  .   |  .   |  #   |
  |  .   |  #   |  .   |  #   |  #   |  .   |  #   |  #   |  .   |  #   |
  |  .   |  #   |  .   |  .   |  .   |  .   |  .   |  .   |  .   |  .   |
  |  #   |  #   |  .   |  #   |  #   |  .   |  #   |  #   |  #   |  #   |
  |  .   |  .   |  .   |  .   |  #   |  .   |  .   |  .   |  .   |  #   |
  |  .   |  #   |  #   |  #   |  #   |  #   |  #   |  #   |  .   |  #   |
  |  .   |  .   |  .   |  .   |  #   |  .   |  .   |  .   |  .   |  .   |
  |  .   |  #   |  #   |  #   |  #   |  .   |  #   |  #   |  #   |  .   |
  |  .   |  .   |  .   |  .   |  #   |  .   |  .   |  .   |  G   |  #   |

~~~python
# X 和 Y轴位移 每次只能在一种方向上移动
deltaX = [1, 0, -1, 0]
deltaY = [0, 1, 0, -1]
# 遍历当前点
def bfsCurrent(point):
    # 判断是否是终点
    if point.x == endX and point.y == endY:
        print('===============>找到路线了',point.serialize())
        LogPoint(point)
        return point
    for i in range(4):
        # 计算移动后的点坐标
        nx = point.x + deltaX[i]
        ny = point.y + deltaY[i]
        key = str(nx) + str(ny)
        # 判断该点坐标是否超过范围，以及该坐标上是否可以通过
        if checkthisPoint(x = nx, y = ny):
            if key not in pointSet:
                pointSet.append(key)
                # print('当前点(%d,%d)====>To(%d,%d)'%(point.x,point.y,nx,ny))
                currentPoint = Point(nx,ny)
                currentPoint.prePoint = point
                bfsCurrent(currentPoint)

# 判断该坐标是否为可经过点
def checkthisPoint(x,y):
    if x > 0 and x < 10 and y < 10 and y > 0:
        if mylist[y][x] != '#':
            return Point(x,y)
        else:
            return None
    else:
        return None
~~~

运行结果:

![运行结果](./image/pathalgorithm.png)