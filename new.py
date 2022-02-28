import os




class demo:
    d=100
    def __init__(self):
        self.a = None
        self.b = None
        
    def setup(self):
        self.a = 10
        print(self.d)

    def run(self):
        print("in run ",self.a)
        self.b=20
        self.c=40
        
    def demo(self,tt):
        print("===",tt)
        print(self.ab)
 
    def teardown(self):
        self.ab = 200
        print("in teardown",self.b)
        print("in tear",self.c)
        self.demo("bb")
        
    def test(self,path=None,mode=8,timeout=20):
        print(path,mode,timeout)
        return path,mode,timeout
        
    def call_test(self):
        path,mode,out=self.test("C:\\Users\\")
        print("==================")
        print(path,mode,out)
        
    def main(self):
        self.setup()
        self.run()
        self.teardown()
        self.test()
        self.call_test()
       # self.execute_1min()

    def execute_1min(self):
        import time
        t_end = time.time() + 60 * 0.5
        while(time.time() < t_end ):
            print("Hello")
            time.sleep(1)
    
if __name__ == '__main__':
    obj_demo = demo()
    obj_demo.main()
    
    
    