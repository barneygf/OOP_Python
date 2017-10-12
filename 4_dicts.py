class LogNameDict(dict):
    def longest_key(self):
        'Return longest key in dictionary'
        longest = None
        for key in self:
            if not longest or len(key) > len(longest):
                longest = key
        return longest

longkeys = LogNameDict()
longkeys['hello'] = 1
longkeys['helloHello'] = 5
longkeys['hihi'] = 'world'

print(longkeys.longest_key())