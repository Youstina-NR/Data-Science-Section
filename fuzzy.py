from fuzzylogic.classes import Domain
from fuzzylogic.functions import alpha, triangular
from fuzzylogic.hedges import plus, minus, very

numbers = Domain("numbers", 0, 20)

close_to_10 = alpha(floor=0.2, ceiling=0.8, func=triangular(0, 20))
close_to_5 = triangular(1, 10)

numbers.foo = plus(close_to_5)
numbers.bar = very(close_to_10)

numbers.bar.plot()
numbers.foo.plot()
numbers.baz = numbers.foo + numbers.bar
numbers.baz.plot()

print(numbers(8))

from matplotlib import pyplot
pyplot.rc("figure", figsize=(10, 10))
# pyplot.show()

from fuzzylogic.classes import Domain
from fuzzylogic.functions import bounded_sigmoid

T = Domain("temperature", 0, 100)
T.cold = bounded_sigmoid(5,15, inverse=True)
T.cold.plot()
T.hot = bounded_sigmoid(20, 40)
T.hot.plot()
T.warm = ~T.hot & ~T.cold
T.warm.plot()
print((T(10)))
print((T(18)))
print((T(30)))
print((T(90)))
pyplot.show()


from matplotlib import pyplot
pyplot.rc("figure", figsize=(10, 10))
from fuzzylogic.classes import Domain
from fuzzylogic.functions import R, S, alpha

T = Domain("test", 0, 30, res=0.1)

T.up = R(1,10)
T.up.plot()
pyplot.show()



from fuzzylogic.classes import Domain, Set, Rule
from fuzzylogic.hedges import very
from fuzzylogic.functions import R, S

temp = Domain("Temperature", -80, 80)
hum = Domain("Humidity", 0, 100)
motor = Domain("Speed", 0, 2000)

temp.cold = S(0,20)
temp.hot = R(15,30)

hum.dry = S(20,50)
hum.wet = R(40,70)

motor.fast = R(1000,1500)
motor.slow = ~motor.fast

R1 = Rule({(temp.hot, hum.dry): motor.fast})
R2 = Rule({(temp.cold, hum.dry): very(motor.slow)})
R3 = Rule({(temp.hot, hum.wet): very(motor.fast)})
R4 = Rule({(temp.cold, hum.wet): motor.slow})

from fuzzywuzzy import fuzz
from fuzzywuzzy import process

print(fuzz.ratio('fuzzywuzzy','wuzzy'))
print(fuzz.ratio('geeksforgeeks', 'geeksgeeks'))

print(fuzz.ratio('GeeksforGeeks', 'GeeksforGeeks')  )
  

print(fuzz.ratio('geeks for geeks', 'Geeks For Geeks ') )
print(fuzz.WRatio('geeks for geeks', 'Geeks For Geeks ') )
# # WRatio handles lower and upper cases and some other parameters too
print(fuzz.token_sort_ratio("geeks for geeks", "for geeks geeks"))
# 100
# fuzz.UQRatio
  
# # This gives 100 as every word is same, irrespective of the position 
  
# # Token Set Ratio
print(fuzz.token_sort_ratio("geeks for geeks", "geeks for for geeks"))
# 88
print(fuzz.token_set_ratio("geeks for geeks", "geeks for for geeks"))
# 100
# Score comes 100 in second case because token_set_ratio considers duplicate words as a single word.
query = 'geeks for geeks'
choices = ['geek for geek', 'geek geek', 'g for geeks'] 
   
# # Get a list of matches ordered by score, default limit to 5
matches = process.extract(query, choices)
print(matches)

# # If we want only the top one
ex = process.extractOne(query, choices)
print(ex)
# ('geeks geeks', 95)