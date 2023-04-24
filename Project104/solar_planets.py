import cv2
#reading image
solar=cv2.imread("solar-system.jpg")

#Putting text
cv2.putText(solar,"sun",(20,300),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(solar,"mercury",(100,250),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(solar,"venus",(190,270),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(solar,"earth",(290,280),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(solar,"mars",(390,280),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(solar,"jupiter",(500,350),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(solar,"saturn",(750,300),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(solar,"uranus",(950,300),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(solar,"neptune",(1150,300),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))

#showing image
cv2.imshow("solar system",solar)
cv2.waitKey(3000)
