# 빼는 수가 클수록 작은 수가 된다 -> 빼기를 나중에

# n = "55-50+40"
# n = "10+20+30+40"
# n = "00009-00009"
n = input()

terms = n.split('-') # 우선 '-'를 기준으로 문자열 분할

# '-'를 기준으로 나누어진 원소 중 '+'가 있는 원소의 덧셈을 진행
for i, term in enumerate(terms):
    if '+' in term:
        tmp_list = list(map(int, term.split('+')))
        tmp_result = 0
        for j in tmp_list:
            tmp_result += j
        terms[i] = tmp_result

# 연산자가 이제 없으니 정수화
for i, term in enumerate(terms):
    terms[i] = int(term)

# 첫 값을 제외한 나머지 값은 모두 음수이므로 뺄셈을 진행
result = terms[0]
for i in range(1, len(terms)):
    result -= terms[i]
    
print(result)