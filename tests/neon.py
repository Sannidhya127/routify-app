from blessed import Terminal
import threading
import time

# Initialize Blessed terminal
term = Terminal()

def code_segment1():
    with term.location(x=0, y=0):
        print(term.center("Code Segment 1"))
    # Your code for segment 1 here
    time.sleep(2)  # Simulate some work

def code_segment2():
    with term.location(x=term.width // 2, y=0):
        print(term.center("Code Segment 2"))
    # Your code for segment 2 here
    time.sleep(2)  # Simulate some work

def run_in_segment(func):
    with term.cbreak(), term.hidden_cursor():
        func()

def main():
    with term.fullscreen():
        with term.location():
            print(term.clear())
            # Split the console into two segments
            thread1 = threading.Thread(target=run_in_segment, args=(code_segment1,))
            thread2 = threading.Thread(target=run_in_segment, args=(code_segment2,))
            thread1.start()
            thread2.start()
            thread1.join()
            thread2.join()

if __name__ == "__main__":
    main()
