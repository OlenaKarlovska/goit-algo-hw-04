import turtle
import argparse

def koch_curve(t, length, level):
    if level == 0:
        t.forward(length)
    else:
        length /= 3.0
        koch_curve(t, length, level - 1)
        t.left(60)
        koch_curve(t, length, level - 1)
        t.right(120)
        koch_curve(t, length, level - 1)
        t.left(60)
        koch_curve(t, length, level - 1)
def koch_snowflake(t, length, level):
    for _ in range(3):
        koch_curve(t, length, level)
        t.right(120)
def main():
    parser = argparse.ArgumentParser(description="Фрактал: Сніжинка Коха")
    parser.add_argument(
    "level",
    type=int,
    nargs="?",
    default=2,
    help="Рівень рекурсії (за замовчуванням 2)"
)
    args = parser.parse_args()
    wn = turtle.Screen()
    wn.title("Сніжинка Коха")
    t = turtle.Turtle()
    t.speed(0)
    t.color("blue")
    t.penup()
    t.goto(-150, 100)
    t.pendown()
    koch_snowflake(t, 300, args.level)
    wn.mainloop()
if __name__ == "__main__":
    main()
