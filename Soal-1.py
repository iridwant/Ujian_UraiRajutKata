class uraiRajutKata:

    def urai(self, kata):
        result = ''

        for index in range(len(kata)+1):
            result += kata[:index]
        return result

    def rajut(self, kata):
        counter     = 2
        charLength  = len(kata)
        index       = 0
        result      = ''
        while index < charLength:
            result  += kata[index]
            index   += counter
            counter += 1
        return result

x = uraiRajutKata()

print(x.urai('Code'))
print(x.urai('Python'))
print(x.urai('Purwadhika'))

print(x.rajut('CCoCodCode'))
print(x.rajut('PPyPytPythPythoPython'))
print(x.rajut('PPuPurPurwPurwaPurwadPurwadhPurwadhiPurwadhikPurwadhika'))

