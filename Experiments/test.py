import matplotlib.pyplot as plt

def close_event():
    plt.close() #timer calls this function after 3 seconds and closes the window

fig = plt.figure()
timer = fig.canvas.new_timer(interval = 3000) #creating a timer object and setting an interval of 3000 milliseconds
timer.add_callback(close_event)

plt.plot([1,2,3,4])
plt.ylabel('some numbers')

timer.start()
plt.show()
print ("Am doing something else")