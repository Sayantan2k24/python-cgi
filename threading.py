import threading

def a():
  while True:
    print("aaaaaaa")

def b():
  while True:
    print("bbbbbbbbbbbbb")
x1 = threading.Thread( target=a )
x2 = threading.Thread( target=b )

x1.start()
x2.start()

# 1 thread from "__main__" namespace
# 2 extra threads a and b
# total 3 threads
