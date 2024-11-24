calls = 0
def count_calls():
    global calls
    calls += 1

def string_info(string):
    count_calls()
    string = (len(string), string.upper(), string.lower())
    string_ = tuple(string)
    print(string_)

def is_contains(string, list_to_search):
    count_calls()
    string_lower = string.lower()
    result = any(item in string_lower for item in list_to_search)
    if result:
        print(True)
    else:
        print(False)

string_info("Baraban")
string_info("Tomattina")
string_info("Sun and Moon")
is_contains('PytonProjekts', ['pyton', 'sistema', 'pytonprojekts'])
is_contains('Sistem', ['sister', 'sisoniya'])
is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])
print(calls)