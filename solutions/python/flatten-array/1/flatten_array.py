import array
def flatten(iterable:list):
    result = []
    def flat(elements:list):
        for element in elements:
            if type(element) == list:
                flat(element)
            elif element != None:
                result.append(element)
    flat(iterable)
    return result