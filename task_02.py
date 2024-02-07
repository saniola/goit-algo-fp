import turtle


def draw_pifagor_tree(branch_len, level):
    if level <= 0:
        return

    turtle.forward(branch_len)
    turtle.right(45)
    draw_pifagor_tree(0.7 * branch_len, level - 1)
    turtle.left(90)
    draw_pifagor_tree(0.7 * branch_len, level - 1)
    turtle.right(45)
    turtle.backward(branch_len)


level = int(
    input("Enter the recursion level for building the Pythagoras tree fractal: ")
)

turtle.speed(0)
turtle.left(90)
turtle.penup()
turtle.goto(0, -200)
turtle.pendown()
draw_pifagor_tree(100, level)
turtle.exitonclick()
