def setup():
    size(800,800)
    noFill()
    noStroke()
    background(0,0,0,0) 
def draw():
    
   for k in range(2,1080):
       if k == mouseX or k == mouseY:
           noFill()
          # ellipse(mouseX+(k), mouseY+k, 10*k,-10*k)
           ellipse(mouseX+(k/10), mouseY+(k/10), k,-1*k)
           stroke(255, 200, 100, 100)
           #line((-1*k), k, mouseX,mouseY)
           noStroke()
           #line((-1*k+1), k+1, mouseX+1,mouseY+1)
           stroke(255, 255, 255, 255)
           arc(k, 20+k, k, k, 0, PI+QUARTER_PI, OPEN)
           #ellipse(mouseX-(k)*5, (mouseY-k)*1/k, mouseX*1/k,-1*mouseY*1/k)
           
