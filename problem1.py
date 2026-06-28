from graphics import *
import time


def main():
    height = float(input("Enter the starting height in meters: "))

    win = GraphWin("Three Bouncing Balls", 500, 500)
    win.setCoords(0, 0, 10, height + 1)

    ground = Line(Point(0, 0), Point(10, 0))
    ground.draw(win)

    balls = []

    ball1 = Circle(Point(3, height), 0.2)
    ball2 = Circle(Point(5, height), 0.2)
    ball3 = Circle(Point(7, height), 0.2)

    ball1.draw(win)
    ball2.draw(win)
    ball3.draw(win)

    balls.append([ball1, height * 0.60, 0])
    balls.append([ball2, height * 0.50, 0])
    balls.append([ball3, height * 0.40, 0])

    still_bouncing = True

    while still_bouncing:
        still_bouncing = False

        for ball in balls:
            circle = ball[0]
            bounce_height = ball[1]

            if bounce_height >= 0.001:
                circle.move(0, -circle.getCenter().getY() + 0.2)
                time.sleep(0.1)

                circle.move(0, bounce_height - circle.getCenter().getY())
                time.sleep(0.1)

                ball[1] = bounce_height * 0.60
                ball[2] = ball[2] + 1
                still_bouncing = True

    message = Text(Point(5, height / 2), "All three balls finished bouncing.")
    message.draw(win)

    count_message = Text(Point(5, height / 2 - 0.5),
                         "Bounces: " + str(balls[0][2]) + ", " +
                         str(balls[1][2]) + ", " +
                         str(balls[2][2]))
    count_message.draw(win)

    win.getMouse()
    win.close()


main()
