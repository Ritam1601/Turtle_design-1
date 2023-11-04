import turtle as t
import colorsys as c
t.pensize(2)
t.color('white')
t.bgcolor('black')
t.speed('fastest')
t.lt(45)
for j in range(1,51):
	if j<=12:
		t.pencolor(c.hsv_to_rgb(1,1/2,1))
	else:
		t.pencolor(c.hsv_to_rgb(1,1/(j-11),1))
	for i in range (2):
		t.circle(300-j*4,90)
		t.lt(90)
t.rt(45)

for j in range(1,54):
	if j<=12:
		t.pencolor(c.hsv_to_rgb(1,1/2,1))
	else:
		t.pencolor(c.hsv_to_rgb(1,1/(j-11),1))
	for i in range(2):
		t.circle(250-j*4,90)
		t.fd(100)
		t.lt(90)
	t.lt(90)
	for i in range(2):
		t.fd(100)
		t.circle(250-j*4,90)
		t.lt(90)
	t.rt(90)
t.rt(25)

for j in range(1,55):
	if j<=12:
		t.pencolor(c.hsv_to_rgb(1,1/2,1))
	else:
		t.pencolor(c.hsv_to_rgb(1,1/(j-11),1))
	for i in range(2):
		t.circle(230-j*4,90)
		t.fd(100)
		t.lt(90)
	t.lt(140)
	for i in range(2):
		t.fd(100)
		t.circle(230-j*4,90)
		t.lt(90)
	t.rt(140)
t.lt(180)

for j in range(1,58):
	if j<=12:
		t.pencolor(c.hsv_to_rgb(1,1/2,1))
	else:
		t.pencolor(c.hsv_to_rgb(1,1/(j-11),1))
	for i in range(2):
		t.circle(230-j*4,90)
		t.fd(100)
		t.lt(90)
	t.lt(140)
	for i in range (2):
		t.fd(100)
		t.circle(230-j*4,90)
		t.lt(90)
	t.rt(140)
t.lt(90)

t.pencolor('green')
for i in range(8):
	t.lt(90)
	t.fd(1)
	t.rt(90)
	t.circle(300,90)
	t.lt(90)
	t.fd(1)
	t.rt(90)
	t.circle(300,-90)
	
t.exitonclick()