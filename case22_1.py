# Дан список со строками. 
# Оставьте в этом списке только те строки, которые начинаются на http://.

def starts_with_http(strings):
    result = []
    for s in strings:
        if s.startswith('http://'):
            result.append(s)
    return result

strings = ['http://example.com', 'https://example.com', 'http://test.com', 'ftp://example.com']
filtered_strings = starts_with_http(strings)

print(filtered_strings)
