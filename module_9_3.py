first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']


first_result=(len(a)-len(b) for a, b, in zip(first,second) if len(a) != len(b))
print(list(first_result))

second_result=(len(c)==len(d) for i in range(len(first)) for c,d in [(first[i],second[i])])
print(list(second_result))