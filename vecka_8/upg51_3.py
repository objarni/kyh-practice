
join_as_lambda = lambda strings, inbetween: inbetween.join(strings)


def join_as_def(strings, inbetween):
    return inbetween.join(strings)

print(join_as_def(['abc', 'def', 'ghi'], ':'))
print(join_as_lambda(['abc', 'def', 'ghi'], ':'))
