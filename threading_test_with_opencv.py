
import sys
import zmq
import cv2
import numpy as np
import threading

def publisher_setup():
	port = "5556"

	if len(sys.argv) != 2:
		raise Exception

	port =  sys.argv[1]
	int(port)
	   
	# Socket to talk to server
	context = zmq.Context()
	socket = context.socket(zmq.SUB)

	print("Collecting points from Openpose...")
	socket.connect ("tcp://localhost:%s" % port)

def output_video_frames():
	publisher_setup()
	cap = cv2.VideoCapture(0)
	while True:
		ret, frame = cap.read()
		cv2.imshow('frame', frame)
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break
	cap.release()
	cv2.destroyAllWindows()

t = threading.Thread(target=output_video_frames)
t.start()
