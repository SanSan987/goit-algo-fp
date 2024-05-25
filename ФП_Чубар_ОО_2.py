import turtle
import math

# Функція для малювання дерева
def draw_tree(branch_len, t, level):
    if level > 0:
        angle = 45
        t.forward(branch_len)
        new_branch_len = branch_len * math.cos(math.radians(angle))
        
        t.left(angle)
        draw_tree(new_branch_len, t, level - 1)
        
        t.right(2 * angle)
        draw_tree(new_branch_len, t, level - 1)
        
        t.left(angle)
        t.backward(branch_len)

# Головна функція рекурсії
def main(level):
    screen = turtle.Screen()
    screen.bgcolor("white")
    t = turtle.Turtle()
    t.color("brown")
    t.left(90)
    t.up()
    t.backward(200)
    t.down()
    t.speed(0)

    draw_tree(100, t, level)
    screen.mainloop()

if __name__ == "__main__":
    level = int(input("Введіть рівень рекурсії: "))
    main(level)
