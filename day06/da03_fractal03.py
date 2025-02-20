import turtle

def draw_branch(t, length, level):
    if level == 0:
        return
    
    t.forward(length)
    t.left(30)
    draw_branch(t, length * 0.6, level - 1)
    t.right(60)
    draw_branch(t, length * 0.6, level - 1)
    t.left(30)
    t.backward(length)

def draw_snowflake():
    screen = turtle.Screen()
    screen.bgcolor("white")
    
    t = turtle.Turtle()
    t.speed(0)
    t.color("blue")
    t.width(2)
    
    for _ in range(6):
        draw_branch(t, 50, 7)
        t.right(60)
    
    screen.mainloop()

draw_snowflake()