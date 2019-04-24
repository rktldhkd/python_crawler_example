import time, threading

StartTime=time.time()

#비즈니스 로직이 돌아가는 함수
def action() :
    print('action ! -> time : {:.1f}s'.format(time.time()-StartTime))

def hello():
    print("hello")

#interval 정의
class setInterval :
    def __init__(self,interval,action) :
        self.interval=interval
        self.action=action
        self.stopEvent=threading.Event()
        thread=threading.Thread(target=self.__setInterval)
        thread.start()

    def __setInterval(self) :
        nextTime=time.time()+self.interval
        while not self.stopEvent.wait(nextTime-time.time()) :
            nextTime+=self.interval
            self.action()

    def cancel(self) :
        self.stopEvent.set()


# start action every 0.6s
# setInterval 첫 번째 인자 : interval의 텀을 설정.
# setInterval 두 번째 인자 : 비즈니스로직 정의한 함수의 이름부분만 넘기면 된다.
#inter=setInterval(0.6,action)
# inter=setInterval(2,hello)
# print('just after setInterval -> time : {:.1f}s'.format(time.time()-StartTime))
#
# # will stop interval in 5s
# t=threading.Timer(10,inter.cancel) #timer. 지정한 초 후 interval 종료
#
# t.start()