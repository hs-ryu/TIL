-- IF 문 사용. IF 문 내에서 LIKE를 통한 조건 처리가 가능함.
-- SELECT IF(500<1000, "YES", "NO") 에서, 앞이 참이면 YES, 거짓이면 NO 출력하는 IF문
-- IF(condition, value_if_true, value_if_false) 참고.

SELECT ANIMAL_ID,NAME,
IF (SEX_UPON_INTAKE LIKE "%Neutered%" OR SEX_UPON_INTAKE LIKE "%Spayed%","O","X") AS "중성화"
FROM ANIMAL_INS