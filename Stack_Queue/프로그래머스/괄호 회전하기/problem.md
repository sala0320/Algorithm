## Level 2 - 월간 코드 챌린지
### 나의 풀이
1. 문자열 왼쪽으로 shift
```{.python}
new[:str_len-i] = string[i:]
new[str_len-i:] = string[:i]
```

2. 괄호 판단 -> stack
