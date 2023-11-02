"""
Uzrakstiet programmu definējot klasi,lai veselu skaitli pārveidotu par romiešu ciparu.

kas ir klase?
Klase sastāv no konsruktora/desstruktora un metodem







"""

class AAA:
    def __init__(self):
        self.roma_sk={
            1: 'I',
            4: 'IV',
            5: 'V',
            9: 'IX',
            10: 'X',
            40: 'XL',
            50: 'L',
            90: 'XC',
            100: 'C',
            400: 'CD',
            500: 'D',
            900: 'CM',
            1000: 'M'
        }
    def to_roman(self, num):
          result = " "
          for value, numeral in sorted(self.roman_numeral.items(), key=lambda x: x[0], reverse=True):
           while num >= value:
              result += numeral
              num -= value
           return result
    
#piemērs
skaitlis=2023
#definējam objektu
KK=AAA()
# jaunajam objekta jāizsauc
print=f"šis {skaitlis} ir romiešu cipariem {}"