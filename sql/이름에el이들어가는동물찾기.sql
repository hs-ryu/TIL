-- LIKE : 조건 달기
-- %는 이 자리에 문자열이 있을 수도, 없을 수도 있다. 0개 이상이라는 뜻
-- _는 반드시 이 자리에 하나의 문자가 존재한다는 뜻.
-- 조합해서도 사용 가능.
SELECT ANIMAL_ID,NAME FROM ANIMAL_INS WHERE NAME LIKE "%EL%" AND ANIMAL_TYPE="Dog" ORDER BY NAME