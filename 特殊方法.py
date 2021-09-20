'''
MyContentMgr实现了特殊方法_enter_(),_exit_()称为该类对象遵守了上下管理器协议
该类对象的实例对象，称为上下文管理
'''
class MyContentMgr(object): 
    def __enter__(self): 
        print('enter方法被调用执行了')
        return self
    
    def __exit__(self,exe_type,exe_val,exe_tb):
        print('exit方法被调用执行了')

    def show(self):
        print('show方法被调用执行了')

with MyContentMgr() as file:
    file.show()