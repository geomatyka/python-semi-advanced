from functional.optional import Optional

def return_sth_or_not():
    # return Optional('Ala ma kota')
    return Optional(None)

if __name__ == '__main__':
    optional = return_sth_or_not()

    optional.map(lambda x: x.upper())
    optional.filter(lambda x: len(x) >=  5)

    optional.if_present(print)

    s = None
    s = s.upper()
    s = s if len(s) >= 5 else None
    if s is not None:
        print(s)