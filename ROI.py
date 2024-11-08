import cv2

# 변수 초기화 (변수는 순서대로)
# 드래그 상태, 시작 좌표, 선택된 사각형 저장, ROI 선택 여부
drawing = False  
ix, iy = -1, -1  
rectangles = []  
roi_selected = False  

# 마우스 콜백 함수
def draw_rectangle(event, x, y, flags, param):
    global ix, iy, drawing, rectangles, roi_selected

    # 마우스 왼쪽 버튼이 눌렸을 때
    # 드래그 상태가 시작 및 시작 좌표로 설정
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True  
        ix, iy = x, y 

    # 마우스가 움직일 때
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:  
            img_copy = img.copy() 
            
            # 원본 이미지에서 드래그 중인 사각형을 그려지는 걸 보여줌
            # ix,iy는 시작 지점 / 다음 x,y는 늘어난 범위 / RGB는 사각형 색깔 / 사각형 두께
            cv2.rectangle(img_copy, (ix, iy), (x, y), (0, 255, 0), 2) 
            cv2.imshow('image', img_copy)  

    # 마우스 왼쪽 버튼이 놓였을 때
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False 
        
        # 선택된 영역에 사각형을 그리기 완료
        cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), 2)  
        
        # 선택한 범위를 저장 및 선택 완료
        rectangles.append((ix, iy, x, y)) 
        roi_selected = True 

        # 선택된 ROI 이미지 추출
        # 선택한 범위를 원본에서 잘라냄 / 선택된 범위를 새로운 창으로 보여줌
        roi = img[iy:y, ix:x] 
        if roi.size > 0: 
            cv2.imshow('Selected ROI', roi) 

# 이미지 로드
img = cv2.imread('babycat.jpg') 

# 초기 이미지 표시 및 마우스 콜백 함수 설정
cv2.imshow('image', img)
cv2.setMouseCallback('image', draw_rectangle)  

# 이미지를 계속 볼 수 있게 대기
cv2.waitKey(0)  

# 모든 OpenCV 닫기
cv2.destroyAllWindows()

# 선택된 범위 좌표를 출력
print("선택된 ROI:", rectangles) 