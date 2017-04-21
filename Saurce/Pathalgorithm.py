class Point:
    def __init__(self,x = 0,y = 0):
        self.x = x
        self.y = y
        self.prePoint = None

    def serialize(self):
        return str((self.x,self.y))

class Array(list):
    def append(self, p_object):
        list.append(self,p_object)

    def lastObject(self):
        if len(self) < 1:
            return None
        else:
            return self[len(self)-1]

    def firstObject(self):
        if len(self):
            return None
        else:
            return self[0]


mylist = [['#', 'S', '#', '#', '#', '#', '#', '#', '.', '#'],
          ['.', '.', '.', '.', '.', '.', '#', '.', '.', '#'],
          ['.',	'#', '.', '#', '#', '.', '#', '#', '.', '#'],
          ['.', '#', '.', '.', '.', '.', '.', '.', '.', '.'],
          ['#',	'#', '.', '#', '#', '.', '#', '#', '#', '#'],
          ['.',	'.', '.', '.', '#', '.', '.', '.', '.', '#'],
          ['.',	'#', '#', '#', '#', '#', '#', '#', '.', '#'],
          ['.',	'.', '.', '.', '#', '.', '.', '.', '.', '.'],
          ['.', '#', '#', '#', '#', '.', '#', '#', '#',	'.'],
          ['.', '.', '.', '.', '#', '.', '.', '.', 'G',	'#']]
startX = startY = 0
endX = endY = 0
for row in range(len(mylist)):
    for index in range(len(mylist[row])):
        if mylist[row][index] == 'S':
            startX = index
            startY = row
        if mylist[row][index] == 'G':
            endX = index
            endY = row

print(endX,endY)
Queue = Array()
Startp = Point(x=startX, y=startY)
Queue.append(Startp)
# X 和 Y轴位移 每次只能在一种方向上移动
deltaX = [1, 0, -1, 0]
deltaY = [0, 1, 0, -1]

str1 = str(startX)+str(startY)
pointSet = [str1]
Queue = []
def LogPoint(point):
    # print(point.serialize())
    if point.prePoint != None:
        LogPoint(point.prePoint)
    Queue.append(point)


def bfsCurrent(point):
    if point.x == endX and point.y == endY:
        print('===============>找到路线了',point.serialize())
        LogPoint(point)
        return point
    for i in range(4):
        nx = point.x + deltaX[i]
        ny = point.y + deltaY[i]
        key = str(nx) + str(ny)
        if checkthisPoint(x = nx, y = ny):
            if key not in pointSet:
                pointSet.append(key)
                # print('当前点(%d,%d)====>To(%d,%d)'%(point.x,point.y,nx,ny))
                currentPoint = Point(nx,ny)
                currentPoint.prePoint = point
                bfsCurrent(currentPoint)


def checkthisPoint(x,y):
    if x > 0 and x < 10 and y < 10 and y > 0:
        if mylist[y][x] != '#':
            return Point(x,y)
        else:
            return None
    else:
        return None

# bfs()

bfsCurrent(point=Point(startX,startY))
pointstr = ''
for i in  range(len(Queue)):
    point = Queue[i]
    if i % 4 == 0:
        pointstr = pointstr + '\n'
    pointstr = pointstr + '=>' + point.serialize()

print(pointstr)