import datetime


def create_function(span):

    if span == 'm':
        sec = 60
    elif span == 'h':
        sec = 3600
    elif span == 'd':
        sec = 86400

    source = '''
def f(start, end):
    span = end - start
    span_in_s = span.total_seconds()
    return divmod(span_in_s, {})[0]
    '''.format(sec)

    exec(source, globals())
    return f


start = datetime.date(2004, 3, 23)
end = datetime.datetime.now().date()


minu = create_function('m')
hour = create_function('h')
days = create_function('d')

print(minu(start, end))
print(hour(start, end))
print(days(start, end))
