import cv2
img = cv2.imread("solar-system.jpg")

cv2.imshow("output",img)
cv2.waitKey(0)

cv2.putText(img,"Sun",(15,50),cv2.FONT_HERSHEY_COMPLEX_SMALL,2,(255,255,255),6)
cv2.putText(img,"Mercury",(80,165),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(255,255,255),2)
cv2.putText(img,"Venus",(180,280),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(255,255,255),2)
cv2.putText(img,"Earth",(280,165),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(255,255,255),2)
cv2.putText(img,"Mars",(380,280),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(255,255,255),2)
cv2.putText(img,"Jupiter",(500,50),cv2.FONT_HERSHEY_COMPLEX_SMALL,2,(255,255,255),6)
cv2.putText(img,"Saturn",(775,110),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(255,255,255),2)
cv2.putText(img,"Uranus",(950,110),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(255,255,255),2)
cv2.putText(img,"Neptune",(1110,110),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(255,255,255),2)


cv2.imwrite("solar-system-copy.jpg",img)