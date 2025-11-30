import cv2
from PIL import Image

from chat import read_img
from api import answer_qustion

global img
global point1,point2
global cut_img
# global draw_img

def on_mouse(event,x,y,flags,param):
    global img,point1,point2
    global cut_img
    # global draw_img

    img2=img.copy()
    if event==cv2.EVENT_LBUTTONDOWN:#左键点击
        # draw_img = img.copy()
        point1=(x,y)
        cv2.circle(img2,point1,10,(0,255,0),3)
        cv2.imshow('image',img2)

    elif event==cv2.EVENT_MOUSEMOVE and (flags&cv2.EVENT_FLAG_LBUTTON):#移动鼠标，左键拖拽
        cv2.rectangle(img2,point1,(x,y),(255,0,0),5)#需要确定的就是矩形的两个点（左上角与右下角），颜色红色，线的类型（不设置就默认）。
        cv2.imshow('image',img2)

    elif event==cv2.EVENT_LBUTTONUP:#左键释放
        point2=(x,y)
        cv2.rectangle(img2,point1,point2,(0,0,255),3)#需要确定的就是矩形的两个点（左上角与右下角），颜色蓝色，线的类型（不设置就默认）。
        cv2.imshow('image',img2)
        min_x=min(point1[0],point2[0])
        min_y=min(point1[1],point2[1])
        width=abs(point1[0]-point2[0])
        height=abs(point1[1]-point2[1])
        # cut_img_=img[min_y:min_y+height,min_x:min_x+width]
        cut_img_=img2[min_y:min_y+height,min_x:min_x+width]
        cut_img = cut_img_.copy()
        # cv2.imwrite('IMG.jpg',cut_img)


def main():

    # catch the img
    global img
    global cut_img
    cut_img = None
    cap = cv2.VideoCapture("/dev/video2")
    while True:
        _, img = cap.read()
        cv2.namedWindow('image')
        cv2.setMouseCallback('image',on_mouse)
        # print(type(img))
        cv2.imshow('image',img)
        key = cv2.waitKey(1)
        if key == ord('q'):
            # cap.release()
            # cv2.destroyAllWindows()
            break
    # print("Hello")

    if cut_img is not None:
        cut_img = Image.fromarray(cv2.cvtColor(cut_img,cv2.COLOR_BGR2RGB))
        # print(type(cut_img))
        context = read_img(cut_img)
        # print(a)
        print(context)
    else:
        print("No image selected")

    # context = "智能投顾能够提供⾼效便捷的⼴泛投资咨询服务，还可以克服投资主观情绪化，实现投资客观、理性和分散化。对 错"

    answer = answer_qustion(context)
    print(answer)

if __name__=='__main__':
    main()



