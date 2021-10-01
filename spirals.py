def setup():
    size(800,800)
    noFill()
    noStroke()
    background(0,0,0,0) 
def draw():
   q = 1 
   colormin = 255
   x = mouseX
   y = mouseY
   c1 = width/2
   c2 = height/2
   d = max(mouseX, 80)
   p = max(mouseY, c1)
   z = min(mouseY,c1)
   g = min(mouseX,z)
   v = min(random(q), mouseY*mouseX)
   q = q* .001 
   
   
    
   for k in range(1,10):
       stroke(255-k,255-k,255-k,colormin)
       #ellipse(c1,c2,y,x/k)
      # stroke(255-k,255-k,255-k,colormin)
      # square(p,p,p)
       
       colormin = colormin - 25
       #square(z,z,z)
       ellipse(width,height,mouseX/k,mouseY/k)
       square(q,q*mouseY,q*k)
       
       
       #rectMode(RADIUS)
       translate(mouseX,k)
       
      
     
      
       colormin = colormin - 2
