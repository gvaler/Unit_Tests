
import pytest

class Date:

    def __init__(self, day: int, month: int, year: int):
        """
        Constructor
        """
        self.day = day
        self.month = month
        self.year = year
        try:
            self.isValid()
        except:
            raise ValueError("the date is not correct")

    def __str__(self):
        """
        This Date to str
        :return: str date
        """
        res = f"Day : {self.day}, Month : {self.month}, Year : {self.year} "
        return res

    def __eq__(self, other)-> bool:
        """
        Check if dates is equals
        :param other: Date
        :return: True/Falce
        """
        if self.day == other.day and \
            self.month == other.month and \
            self.year == other.year :
            return True
        return False

    def __gt__(self, other) -> bool:
        """
        Check if this date before input date
        :param other: input date
        :return: True/False
        """
        if self.year < other.year:
            return False
        if self.year > other.year:
            return True
        elif self.month > other.month:
            return True
        elif self.day > other.day:
            return True
        return False

    def __lt__(self, other) -> bool:
        """
        Check if this date after input date
        :param other: input date
        :return: True/False
        """
        if self.year < other.year:
            return True
        elif self.month < other.month:
            return True
        elif self.day < other.day:
            return True
        return False

    def __le__(self, other)-> bool:
        """
        Check if this date before/equal to input date
        :param other: Date
        :return: True/False
        """
        if self < other or \
            self == other:
            return True
        return False

    def __ne__(self, other)-> bool:
        """
        Check if this date not equal to other
        :param other: Date
        :return: True/Falce
        """
        if self.year!=other.year :
            if self.month!=other.month:
                if self.day!=other.day:
                    return True
        return False

    def __ge__(self, other) -> bool:
        """
        Check if this date after/equal to input date
        :param other: Date
        :return: True/False
        """
        if self > other or \
            self == other:
            return True
        return False

    def __sub__(self, other)-> int:
        """
        Return date difference
        if this date before return a negative number
        :param other:input date
        :return:difference
        """
        year = self.year-other.year
        month = self.month-other.month
        day = self.day-other.day
        res = int (abs(year*365.25) + abs(month*30.4) + abs(day))
        return res

    def isValid(self) -> ValueError:
        """
        Check if date is Valid
        :return: Type/Value Error of nothing if date is ok
        """
        days = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28,
                29, 30, 31]
        months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        m30 = [5,9,11]

        dict = {'day' : self.day, 'month' : self.month, 'year' : self.year }
        for k,v in dict.items():
            if not isinstance(v,int):
                raise TypeError (k + " must been int ")

        if self.day not in days:
                 raise ValueError ("Day mus be between 1-31")

        if self.month not in months:
                 raise ValueError ("Month mus bee between 1-12")

        if self.year < 0 or self.year > 9999 :
            raise ValueError ("Year must be between 0-9999")

        if self.month in m30 :
            if self.day >30 :
                raise ValueError (f"In month {self.month} the days mus been between 1-30 ")

        if self.month == 2 :
            if(self.year%4==0 and self.day>29):
                raise ValueError("In month 2 the days must been between 1-29")
            else:
                if self.day>28:
                    raise ValueError("In month 2 the days must been between 1-28")

    def getNextDay(self):
        """
        Add day to this date
        :return: Date +1
        """
        d = Date(self.day , self.month, self.year)
        try :
            d.day+=1
            d.isValid()
        except :
            d.day = 1
            d.month += 1
        if d.month > 12 :
            d.month -= 12
            d.year += 1

        d.isValid()
        return d

    def getNextDays(self,daysToAdd:int):
        """
        Add days to Date
        :param daysToAdd: int
        :return: date + days to add
        """
        d = self
        for i in range(daysToAdd):
            d = d.getNextDay()
        return d
