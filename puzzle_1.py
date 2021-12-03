import urllib.request


input_url: str = 'https://adventofcode.com/2021/day/1/input'
request: urllib.request.Request = urllib.request.Request(input_url)

with urllib.request.urlopen(request) as response:
    input_data: str = response.read().decode('utf-8')
