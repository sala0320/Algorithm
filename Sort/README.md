### list 본체 정렬 → O(logn)

```python
a = [1, 10, 5, 7, 6] 
a.sort()
a >>> [1, 5, 6, 7, 10]
a = [1, 10, 5, 7, 6]
a.sort(reverse=True)
a >>> [10, 7, 6, 5, 1]
```

### liat 정렬된 결과 반환

```python
x = [1 ,11, 2, 3]
y = sorted(x)
z = reversed(x)
x >>> [1, 11, 2, 3]
y >>> [1, 2, 3, 11]
z >>> [11, 2, 3, 1]
```

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/f7303a8a-0baf-498b-ad5f-7ca9f3224dc1/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/f7303a8a-0baf-498b-ad5f-7ca9f3224dc1/Untitled.png)

### 1. 삽입 정렬

삽입 정렬(insertion sort)은 수열의 왼쪽부터 순서대로 정렬하는 방식입니다. 작업하다 보면 좌측에는 정렬이 끝난 숫자가 오게 되고 우측에는 아직 확인하지 않은 숫자가 남게 됩니다. 우측의 미탐색 영역에서 숫자를 하나 꺼내서 정렬이 끝난 영역의 적절한 위치에 삽입해 나가는 방식입니다.

[[정렬 알고리즘][파이썬] 삽입 정렬](https://serendipity24.tistory.com/16)

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/9ea85b95-8d67-4284-8a81-a996322c8b4f/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/9ea85b95-8d67-4284-8a81-a996322c8b4f/Untitled.png)

### 2. 병합 정렬

병합 정렬(merge sort)은 정렬하고 싶은 수열을 두 개의 수열(거의 같은 길이)로 분할해 갑니다. 더 이상 분할되지 않는 상태에 이르면(즉, 각 그룹이 한 개의 숫자가 된 경우) 그룹들을 병합(merge) 해 나갑니다. 병합할 때에는 정렬이 끝난 두 개의 수열을 병합해서 정렬이 끝난 하나의 수열로 만듭니다. 이것을 전체가 하나의 그룹이 될 때까지 반복합니다

[[정렬 알고리즘][파이썬] 병합 정렬](https://serendipity24.tistory.com/26)

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/246dbded-7a8f-4b95-bb08-d9a76e4f58cb/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/246dbded-7a8f-4b95-bb08-d9a76e4f58cb/Untitled.png)

### 3. 버블 정렬

버블 정렬(bubble sort)은 '오른쪽부터 왼쪽 방향으로 인접한 두 개의 숫자를 비교해서 교환하는 작업을 반복합니다.' 오른쪽부터 왼쪽으로 숫자를 옮겨가는 모양이 물속에서 거품이 올라오는 모양과 비슷하다고 해서 버블이라고 합니다.

[[정렬 알고리즘][파이썬] 버블 정렬](https://serendipity24.tistory.com/14)

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/dd9f9068-91cf-4cf2-8ea9-c2803125dd9a/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/dd9f9068-91cf-4cf2-8ea9-c2803125dd9a/Untitled.png)

### 4. 선택 정렬

선택 정렬(selection sort)에서는 '수열 중에서 최소값을 검색해서 왼쪽 끝에 있는 숫자와 교체하는 작업을 반복합니다. 수열 중에서 최소값을 찾을 때는 선형 탐색을 사용합니다.

[[정렬 알고리즘][파이썬] 선택 정렬](https://serendipity24.tistory.com/15)

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/f4f2d739-b38d-4c30-9199-5e7ec2644eaa/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/f4f2d739-b38d-4c30-9199-5e7ec2644eaa/Untitled.png)

### 5. 퀵 정렬

퀵 정렬(quick sort)에서는 기준이 되는 수(pivot)를 수열 안에서 임의로 하나를 선택합니다. 그리고 피봇 이외의 수를 '피봇보다 작은 수'와 '피봇 이상인 수'의 두 그룹으로 나누고 이것을 다음과 같이 배치합니다. '피봇보다 작은 수' < 피봇 < '피봇 이상인 수' 그리고 양쪽 그룹을 또 다시 퀵 정렬을 사용해 나누고 이것을 계속 반복하면 자연스럽게 정렬이 이루어집니다.

[[정렬 알고리즘][파이썬] 퀵 정렬](https://serendipity24.tistory.com/27)

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/3e504eaf-c3f3-4dff-bdc2-31f079842a4a/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/3e504eaf-c3f3-4dff-bdc2-31f079842a4a/Untitled.png)

### 6. 힙 정렬

힙(heap)은 그래프의 트리 구조 중 하나로, '우선순위 큐(priority queue)'를 구현할 때 사용됩니다. 우선순위 큐는 자료 구조의 하나로서 데이터를 자유롭게 추가할 수 있습니다. 반면, 데이터를 추출할 때는 최소값부터 순서대로 선택됩니다. 추가는 자유롭게 하고 추출할 때는 작은 값부터 꺼내는 것이 우선순위 큐입니다. 또한, 힙을 표현하는 트리 구조에서는 각 정점을 '노드(node)'라고 부릅니다. 힙에서는 각 노드에 데이터가 저장됩니다.

[[정렬 알고리즘][파이썬] 힙 정렬](https://serendipity24.tistory.com/17)

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/debaf2ea-d89a-4df2-a6a4-6abd606f8944/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/debaf2ea-d89a-4df2-a6a4-6abd606f8944/Untitled.png)

### 7. 기수 정렬(Radix Sort)

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/cb312005-af3a-4a0c-84f7-41b9149c9493/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/cb312005-af3a-4a0c-84f7-41b9149c9493/Untitled.png)

### 8. 카운팅 정렬

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/b6bc934d-cee4-44b8-9641-b66a14512681/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/b6bc934d-cee4-44b8-9641-b66a14512681/Untitled.png)
