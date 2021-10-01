def setup():
    size(700,700)
    noFill()
    noStroke()
    background(0,0,0,0) 
    stroke(255,255,255,255)
def draw():
   xoff = 0.1
   t = mouseX % 100 + 1
   g = mouseY % 25
   for i in range(10):
       if mouseX < 50:
        xoff = xoff + .01
        k = 0.5
        n = noise(xoff) *width + k
        line(250, 100, -1*(5+k),-1*width+k)
        k = 0.5*2*k + k
        translate(-1*k, t*k*g)
        ellipse(k, g, 5, 8)
       if mouseX > 50: 
          line(250, 100, 0,-1*width+t)
          ellipse(t*g,i*t,10,10)
          translate(t+80, g+60)
          
          r = random(50)
          stroke(255)
          line(5+g, i*t, height, width)
          translate(-1*t,-1*g)
