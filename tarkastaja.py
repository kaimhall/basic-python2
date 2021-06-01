
def testaa(testattava):

        if len(testattava) < 5:
            return False

        elif testattava.isdigit():
            return False

        elif testattava.isalpha():
            return False

        else:
            return True
            
            


