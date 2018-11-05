import threading

#
# lock = threading.Lock()
# ticket = 1000
#
#
# def buy():
#     global lock
#     global ticket
#     while ticket > 0:
#         lock.acquire()
#         ticket -= 1
#         print 'ticker num is %d,this is %s' % (ticket, threading.current_thread().name)
#         lock.release()
#
#
# a_thread = threading.Thread(target=buy,  name='a_thread')
# b_thread = threading.Thread(target=buy, name='b_thread')
# c_thread = threading.Thread(target=buy, name='c_thread')
#
# a_thread.start()
# b_thread.start()
# c_thread.start()

map1 = {'a': 1, 'b': 2, 'c': 3}

map2 = {'c': 4, 'd': 5, 'e': 7}

map3 = {'c': 9}

map4 = {}

map1.update(map2)
map1.update(map3)
map1.update(map4)
print map1

