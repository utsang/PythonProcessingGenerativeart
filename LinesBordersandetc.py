def setup():
    size(800,800)
    noFill()
    noStroke()
    background(0,0,0,0) 
def draw():
   colormin = 255
    
   for k in range(2,1080):
       if k == mouseX or k == mouseY:
           noFill()
           
          
           stroke(255, 200, 100, 100)
           #line((-1*k), k, mouseX,mouseY)
           noStroke()
           #line((-1*k+1), k+1, mouseX+1,mouseY+1)
           stroke(255, 255, 255, 255)
        #   arc(k*2+mouseY*height/2, k*2+mouseX+width/2, 20+k, 20-k, 0, PI+QUARTER_PI, OPEN)
           point(k+5*mouseX, k-5*mouseX)
           point(k-5*mouseY, k+5*mouseY)
           ellipse(mouseX-(k)*5, (mouseY-k)*1/k, mouseX*1/k,-1*mouseY*1/k)
       if mouseX > 20:
           ellipse(height/2, width/2, mouseX/k, mouseY/k)
           fill(colormin,colormin,colormin,colormin)
           colormin = colormin - 100

