class Time:
    # Конструктор, принимающий четыре целых числа: часы, минуты, секунды и миллисекунды.
    # В случае, если передан отрицательный параметр, вызвать исключение ValueError.
    # После конструирования, значения параметров времени должны быть корректными:
    # 0 <= GetHour() <= 23
    # 0 <= GetMinute() <= 59
    # 0 <= GetSecond() <= 59
    # 0 <= GetMillisecond() <= 999
    def __init__(self, hours=0, minutes=0, seconds=0, milliseconds=0):
        if (hours < 0) or (minutes < 0) or (seconds < 0) or (milliseconds < 0):
            raise ValueError('Wrong init')
        else:
            self.hours = hours
            self.minutes = minutes
            self.seconds = seconds
            self.milliseconds = milliseconds
    def GetHour(self):
        return self.hours
    def GetMinute(self):
        return self.minutes
    def GetSecond(self):
        return self.seconds
    def GetMillisecond(self):
        return self.milliseconds
    # Прибавляет указанное количество времени к текущему объекту.
    # После выполнения этой операции параметры времени должны остаться корректными.
    def Add(self, time):
        self.milliseconds += time.GetMillisecond()
        seconds = 0
        if self.milliseconds > 999:
            seconds = int(self.milliseconds / 1000)
            self.milliseconds %= 1000
        
        self.seconds += time.GetSecond() + seconds
        minutes = 0
        if self.seconds > 59:
            minutes = int(self.seconds / 60)
            self.seconds %= 60

        self.minutes += time.GetMinute() + minutes
        hours = 0
        if self.minutes > 59:
            hours = int(self.minutes / 60)
            self.minutes %= 60
        
        self.hours += time.GetHour() + hours
        self.hours %= 24
    # Операторы str и repr должны представлять время в формате
    # HH:MM:SS.ms
    def __str__(self):
        return (str(self.GetHour())).zfill(2) + ':' + (str(self.GetMinute())).zfill(2) + ':' + (str(self.GetSecond()).zfill(2)) + '.' + str(self.GetMillisecond())