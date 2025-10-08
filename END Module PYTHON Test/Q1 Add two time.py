class Time:
    def __init__(self,hours,minutes,seconds):
        self.hours= hours
        self.minutes= minutes
        self.seconds= seconds
    
    def __add__(self,other):
        total_seconds = self.seconds + other.seconds 
        total_minutes = self.minutes + other.minutes  + total_seconds // 60
        total_hours = self.hours + other.hours + total_minutes // 60

        total_seconds = total_seconds % 60
        total_minutes =  total_minutes %60
        total_hours =   total_hours %24

        return Time(  total_hours,  total_minutes,   total_seconds)
    
    def __str__(self):
        return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"
    
    print("Enter first time:")
    h1 = int(input("Hours:"))
    m1 = int(input("Minutes:"))
    s1 = int(input("Seconds:"))
    
    print("Enter second time:")
    h2 = int(input("Hours:"))
    m2 = int(input("Minutes:"))
    s3 = int(input("Seconds:"))
    
    t1 = Time(h1,m1,s1)
    t2 = Time(h2,m2,s3)

    t3 = t1 +t2

    print("\nSum of times:",t3)

