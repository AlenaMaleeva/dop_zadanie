grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students_ = list (students)
print( students_)
students_ = sorted (students)
print( students_ )
a = dict (zip (students_, grades ))
print( a)
print(a ['Aaron'])
Aaron = sum( a ['Aaron']) / len (a ['Aaron'])
print( Aaron )
print( a ['Bilbo'])
Bilbo = sum(a ['Bilbo']) / len (a ['Bilbo'])
print(Bilbo)
print( a ['Johnny'])
Johnny = sum(a ['Johnny']) / len (a ['Johnny'])
print(Johnny)
print(a ['Khendrik'])
Khendrik = sum(a ['Khendrik']) / len (a ['Khendrik'])
print(Khendrik)
print(a['Steve'])
Steve = sum(a ['Steve']) / len (a ['Steve'])
print( Steve)

students_1 =  ( Aaron, Bilbo, Johnny, Khendrik, Steve )
grades = list (students_1)
print(grades)
a = dict (zip (students_, grades ))
print( a )
