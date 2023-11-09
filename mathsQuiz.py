import random
import time
import threading

OPERATORS = ["+", "-", "*"]
MIN_OPERAND = 3
MAX_OPERAND = 12
TOTAL_PROBLEMS = 5


def generate_problem():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(OPERATORS)

    expr = str(left) + " " + operator + " " + str(right)
    answer = eval(expr)
    return expr, answer


def quiz_timer(time_limit, event):
    time.sleep(time_limit)
    if not event.is_set():
        print("Time's up!")
        event.set()



def main():
    wrong = 0
    correct = 0
    input("Press S to start the quiz!")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    start_time = time.time()
    for i in range(TOTAL_PROBLEMS):
        expr, answer = generate_problem()
        print("Problem #" + str(i + 1) + ": " + expr + " = ?")

        user_answer = None
        event = threading.Event()
        timer_thread = threading.Thread(target=quiz_timer, args=(5, event))
        timer_thread.start()

        while not event.is_set() and user_answer is None:
            user_answer = input("Your answer: ")
            if user_answer == str(answer):
                print("Correct!")
                correct += 1
            else:
                print("Incorrect. The correct answer is:", answer)
                wrong += 1
            timer_thread.join()  # Wait for the timer thread to finish

        if event.is_set():
            timer_thread.join()  # Make sure the timer thread has finished

    end_time = time.time()
    total_time = round(end_time - start_time, 2)

    print("********************************************")
    print("Quiz complete! You answered", correct, "out of", TOTAL_PROBLEMS, "questions correctly.")
    print("Total time taken:", total_time, "seconds")


if __name__ == "__main__":
    main()
