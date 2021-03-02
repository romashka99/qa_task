from abc import ABC, abstractmethod
import time
import os
import random
from psutil import virtual_memory

class Test(ABC):
    def __init__(self, tc_id, name):
        self.tc_id = tc_id
        self.name = name

    @abstractmethod
    def prep(self):
        pass

    @abstractmethod
    def run(self):
        pass

    @abstractmethod
    def clean_up(self):
        pass

    @abstractmethod
    def execute(self):
        pass

class Test1(Test):
    def __init__(self):
        super().__init__(1, 'Список файлов')

    def prep(self):
        print('Этап подготовки.\n')
        seconds = int(time.time())
        if seconds % 2 == 0:
            return True
        return False

    def run(self):
        print('Этап выполнения.\n')
        homepath = os.getenv('USERPROFILE')
        for root, dirs, files in os.walk('homepath'):  
            for filename in files:
                print(filename)

    def clean_up(self):
        print('Этап завершения.\n')
        return

    def execute(self):
        print('Выполнение тест-кейса{0}: {1}\n'.format(self.tc_id, self.name))
        try:
            if self.prep() == True:
                self.run()
                self.clean_up()
            else:
                return
        except Exception as err:
            print(err)

class Test2(Test):
    def __init__(self):
        super().__init__(2, 'Случайный файл')

    def prep(self):
        print('Этап подготовки.\n')
        if virtual_memory().total / 1073741824 < 1:
            return False
        return True

    def run(self):
       print('Этап выполнения.\n')
       file = open('test.txt', 'w')
       file.truncate(1048576)
       n = random.randint(1, 10)
       for i in range(n):
           file.write('{0}\n'.format(i))

    def clean_up(self):
        print('Этап завершения.\n')
        os.remove('test.txt')

    def execute(self):
        print('Выполнение тест-кейса{0}: {1}\n'.format(self.tc_id, self.name))
        try:
            if self.prep() == True:
                self.run()
                self.clean_up()
            else:
                return
        except Exception as err:
            print(err)

test_1 = Test1()
test_2 = Test2()

test_1.execute()
test_2.execute()