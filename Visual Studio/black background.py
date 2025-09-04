import turtle
import random
import colorsys

# إعداد النافذة
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("خلفية جميلة متحركة")
screen.tracer(0)

# إنشاء متغيرات للرسم
pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()
pen.width(2)

# دالة لإنشاء أشكال عشوائية ملونة
def draw_shapes():
    for _ in range(50):
        # توليد لون عشوائي باستخدام نظام ألوان HSV
        h = random.random()
        s = 0.7 + random.random() * 0.3
        v = 0.8 + random.random() * 0.2
        r, g, b = colorsys.hsv_to_rgb(h, s, v)
        
        pen.color(r, g, b)
        pen.penup()
        x = random.randint(-300, 300)
        y = random.randint(-300, 300)
        pen.goto(x, y)
        pen.pendown()
        
        shape = random.choice(["circle", "square", "triangle", "star"])
        size = random.randint(10, 50)
        
        if shape == "circle":
            pen.circle(size)
        elif shape == "square":
            for _ in range(4):
                pen.forward(size)
                pen.left(90)
        elif shape == "triangle":
            for _ in range(3):
                pen.forward(size)
                pen.left(120)
        elif shape == "star":
            for _ in range(5):
                pen.forward(size)
                pen.right(144)

# دالة لإنشاء خطوط متحركة
def draw_moving_lines():
    pen.clear()
    for _ in range(20):
        h = random.random()
        r, g, b = colorsys.hsv_to_rgb(h, 0.8, 0.9)
        pen.color(r, g, b)
        
        x1 = random.randint(-350, 350)
        y1 = random.randint(-350, 350)
        x2 = random.randint(-350, 350)
        y2 = random.randint(-350, 350)
        
        pen.penup()
        pen.goto(x1, y1)
        pen.pendown()
        pen.goto(x2, y2)
    
    screen.update()
    screen.ontimer(draw_moving_lines, 100)

# اختيار نوع الخلفية
choice = input("اختر نوع الخلفية (1-أشكال عشوائية / 2-خطوط متحركة): ")

if choice == "1":
    draw_shapes()
elif choice == "2":
    draw_moving_lines()
else:
    print("اختيار غير صحيح، سيتم عرض الأشكال العشوائية")
    draw_shapes()

screen.mainloop()