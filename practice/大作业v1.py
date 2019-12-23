"""
Title : 五子棋
author:YL
date:
"""
import pygame
import sys
from pygame import *
import time

#  棋子类型 1是黑棋, 2是白棋
chessType = 1

# 定义一个空棋盘
chess_arr = []

resultFlag = 0


# 定义棋子类
class ChessPoint:
    def __init__(self, x, y, value):
        '''
        定义棋子的坐标和值
        :param x:  棋子的X轴坐标
        :param y:  棋子的 Y轴 坐标
        :param value:  value的值为0代表为空 为1代表黑棋 为2 代表白棋
        '''
        self.x = x
        self.y = y
        self.value = value


# 定义初始化棋盘
def chessList(x, y):
    for i in range(15):
        pointList = []
        for j in range(15):
            pointX = x + i * 40
            pointY = y + j * 40
            cp = ChessPoint(pointX, pointY, 0)  # 棋子落点
            pointList.append(cp)
        chess_arr.append(pointList)


# 定义事件类
def eventHander():
    for event in pygame.event.get():
        global chessType
        # 事件类型为退出时
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        # 当点击鼠标时
        if event.type == MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            i = 0
            j = 0
            for temp in chess_arr:
                for point in temp:
                    if x >= point.x - 10 and x <= point.x + 10 and y >= point.y - 10 and y <= point.y + 10:
                        # 当棋盘位置为空,棋子类型为黑棋
                        if point.value == 0 and chessType == 1:
                            # 鼠标点击时, 棋子为黑棋
                            point.value = 1
                            estimate(i, j, 1)
                            # 切换角色
                            chessType = 2

                        # 当棋盘位置为空时, 棋子类型为白棋
                        elif point.value == 0 and chessType == 2:
                            # 鼠标点击时, 棋子为白棋
                            point.value = 2
                            estimate(i, j, 2)
                            # 切换角色
                            chessType = 1
                        break
                    j += 1
                i += 1
                j = 0


#  判断五子是否连珠
def estimate(i, j, value):
    global resultFlag
    # 先将判断条件改为False
    flag = False
    # 判断横向是否出现五连( 判断5个棋子类型是否一致)
    for x in range(i - 4, i + 5):
        if x >= 0 and x + 4 < 15:  # x 是需要在棋盘范围内的
            if chess_arr[x][j].value == value and \
                    chess_arr[x + 1][j].value == value and \
                    chess_arr[x + 2][j].value == value and \
                    chess_arr[x + 3][j].value == value and \
                    chess_arr[x + 4][j].value == value:
                flag = True
                break

    #  判断纵向是否出现五连( 判断5个棋子类型是否一致)
    for x in range(j - 4, j + 5):
        if x >= 0 and x + 4 < 15:
            if chess_arr[i][x].value == value and \
                    chess_arr[i][x + 1].value == value and \
                    chess_arr[i][x + 2].value == value and \
                    chess_arr[i][x + 3].value == value and \
                    chess_arr[i][x + 4].value == value:
                flag = True
                break

    # 判断东北方向的对角下输赢 x 列轴， y是行轴 ， i 是行 j 是列（右斜向）（在边缘依次逐一遍历，是否五个棋子的类型一样）
    for x, y in zip(range(j + 4, j - 5, -1), range(i - 4, i + 5)):
        if x >= 0 and x + 4 < 15 and y + 4 >= 0 and y < 15:
            if chess_arr[y][x].value == value and \
                    chess_arr[y - 1][x + 1].value == value and \
                    chess_arr[y - 2][x + 2].value == value and \
                    chess_arr[y - 3][x + 3].value == value and \
                    chess_arr[y - 4][x + 4].value == value:
                flag = True
                break

    # 2、判断西北方向的对角下输赢 x 列轴， y是行轴 ， i 是行 j 是列（左斜向）（在边缘依次逐一遍历，是否五个棋子的类型一样）
    for x, y in zip(range(j - 4, j + 5), range(i - 4, i + 5)):
        if x >= 0 and x + 4 < 15 and y >= 0 and y + 4 < 15:
            if chess_arr[y][x].value == value and \
                    chess_arr[y + 1][x + 1].value == value and \
                    chess_arr[y + 2][x + 2].value == value and \
                    chess_arr[y + 3][x + 3].value == value and \
                    chess_arr[y + 4][x + 4].value == value:
                flag = True
                break

    # 当判断条件成立时, 五子棋成立
    if flag:
        resultFlag = value
        print('黑棋胜' if value == 1 else '白棋胜')


#  将游戏基本配置放在main函数中
def main():
    global chess_arr, resultFlag
    chessList(27, 27)
    # 初始化pygame
    pygame.init()
    # 创建游戏窗口
    screen = pygame.display.set_mode((620, 620))
    # 设置游戏标题
    pygame.display.set_caption('程序猿五子棋')
    # 载入背景图片
    backdrop = pygame.image.load('images/bg.png')
    # 载入黑棋图片
    blackChess = pygame.image.load('images/blackChess.png')
    #  载入白棋图片
    whiteChess = pygame.image.load('images/whiteChess.png')
    # 载入 胜利时的图片
    resultWin = pygame.image.load('images/resultChess.jpg')
    rect = blackChess.get_rect()

    while True:
        screen.blit(backdrop, (0, 0))
        for temp in chess_arr:
            for point in temp:
                # 当棋子类型为1时候绘制黑棋
                if point.value == 1:
                    screen.blit(blackChess, (point.x - 18, point.y - 18))
                # 当棋子类型为2时绘制白棋
                elif point.value == 2:
                    screen.blit(whiteChess, (point.x - 18, point.y - 18))
                else:
                    pass
        if resultFlag > 0:
            # 清空棋盘
            chess_arr = []
            # 重新初始化棋盘
            chessList(27, 27)
            # 弹出获胜时的图片
            screen.blit(resultWin, (300, 300))
            # 加载音乐
            pygame.mixer_music.load('传奇.mp3')
            pygame.mixer_music.play(-1) # 重复播放

            # 更新界面
        pygame.display.update()

        if resultFlag > 0:
            time.sleep(10)
            # 刷新获胜结果
            resultFlag = 0
            # 调用定义事件函数
        eventHander()


if __name__ == '__main__':
    main()
