# While you can pass multiple arguments to the Exception constructor
# And that these would be available through the args tuple
# In practice you should only pass in a single string argument
# However, specific exception classes may provide additional specific named attributes (e.g. UnicodeError)

def main():

    try:
        b'\x81'.decode('utf-8')
    except UnicodeError as e:
        print(e)

        # As args should only have a single string entry, further data is stored in other attributes
        # UnicodeError has 5 additional named attributes
        print("Encoding:", e.encoding)
        print("Reason:", e.reason)
        print("Object:", e.object)
        print("Start:", e.start)
        print("End:", e.end)


main()
