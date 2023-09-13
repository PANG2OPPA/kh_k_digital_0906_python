DESC EMP;
DESC DEPT;
DESC EMP;
DESC SALGRADE;
-----------------------------------------------------------
-- �⺻ SELECT * (���� �ǹ�) FROM EMP(���̺� �̸�); �����ݷ����� ����
SELECT * FROM EMP;
-- EMP ���̺����� �����ȣ, ����̸�, ����� ���� �μ���ȣ�� ��ȸ
SELECT EMPNO, ENAME, DEPTNO
FROM EMP;
-- SQL�� �ۼ� �� ���ǻ���
-- SQL���� ��ҹ��ڸ� �������� ����
-- SQL������ ���� �Ǵ� ���� �ٿ� �Է� �� �� ����
-- �Ϲ������� Ű����� �빮�ڷ� �Է��Ѵ�.
-- �Ϲ������� �̸�, �� �̸� ���� �ҹ��ڷ� �ۼ��Ѵ�.
-- SQL���� ������ ���� ;�� ������.
-- �����ȣ�� �μ���ȣ�� �������� EMP ���̺� ��ȸ�ϱ�.
SELECT EMPNO, DEPTNO FROM EMP;
-- ��Ī �����ϱ� : AS, ���̸� �Ǵ� �÷��� ��Ī���� ǥ�� �� �� ����
SELECT ENAME AS �̸�, SAL AS �޿�, SAL*12+COMM AS ����, COMM AS ������
FROM EMP;

-- �ߺ� �����ϱ� : DISTINCT, �����͸� ��ȸ�� �� ���� �ߺ��Ǵ� ���� ������ ��ȸ�Ǵ� ���, ���� �ߺ��� ���� �Ѱ����� �����ϰ��� �ϴ� ��� ���
SELECT DISTINCT JOB, DEPTNO FROM EMP;
-- �÷����� ����ϴ� ��������� : +, -, *, /
SELECT ENAME, SAL, SAL + 12
FROM EMP;
-- WHERE ���� : �����͸� ��ȸ�� �� ����ڰ� ���ϴ� ���ǿ� �´� �����͸� ��ȸ�ϰ� ���� �� ��� (���� ����)
-- ���� �����ڿ� �Բ� �����
SELECT * FROM EMP
WHERE DEPTNO = 10; -- �����ͺ��̽������� = ���ٶ�� �ǹ̷� ���

SELECT * FROM EMP
WHERE EMPNO = 7369;
-- �޿��� 2500 �ʰ��� �����ȣ, �̸�, ����, �޿� ��� �غ���
SELECT EMPNO, ENAME, JOB, SAL 
FROM EMP
WHERE SAL > 2500;

SELECT *
FROM EMP
WHERE SAL * 12 = 36000;

-- �������� 500 �ʰ��� ��� ���
SELECT * FROM EMP
WHERE COMM > 500;

-- �Ի����� 81�� 1��1�� ������ �����͸� ��ȸ�ϴ� ����
-- ��¥�� ���� ��� ��¥ ���Ŀ� ���缭 ���ϸ� ��
SELECT * FROM EMP
WHERE HIREDATE < '81/01/01';

-- ���� ������ ǥ���ϴ� ����� ���������� ���� <>, !=, ^=, NOT
SELECT * FROM EMP
WHERE NOT DEPTNO = 30;

-- �޿��� 3000�̻��̰�, �μ��� 20���� ��� ��ȸ
SELECT * 
FROM EMP
WHERE SAL >= 3000 AND DEPTNO = 20;

-- �޿��� 3000 �̻��̰�, �μ��� 20���̰�, �Ի����� 82/01/01 ���� ���
SELECT * 
FROM EMP
WHERE SAL >= 3000 AND DEPTNO = 20 AND HIREDATE < '82/01/01';

-- �޿��� 3000 �̻��̰� �μ��� 20���̰ų� �Ի����� 82�� 1�� 1�� ������ ��� ��ȸ
SELECT * 
FROM EMP
WHERE SAL >= 3000 AND (DEPTNO = 20 OR HIREDATE < '82/01/01');

-- �޿��� 2500 �̻��̰� ������ MANAGER�� ��������� ���
SELECT * 
FROM EMP
WHERE SAL >= 2500 AND JOB = 'MANAGER';

-- IN ������
SELECT *
FROM EMP
WHERE JOB = 'MANAGER'
    OR JOB = 'SALESMAN'
    OR JOB = 'CLERK';
    
SELECT *
FROM EMP
WHERE JOB IN('MANAGER', 'SALESMAN', 'CLERK');

SELECT *
FROM EMP
WHERE DEPTNO NOT IN(20, 30);

-- BETWEEN A AND B ������ : ������ ������ ��ȸ�� �� ����ϴ� ������
-- �޿��� 2000�̻� 3000������ ��� ��ȸ
SELECT *
FROM EMP
WHERE SAL >= 2000 AND SAL <= 3000;

SELECT *
FROM EMP
WHERE SAL BETWEEN 2000 AND 3000;

-- �����ȣ�� 7689 ~ 9702 ������ ��� ��ȸ
SELECT *
FROM EMP
WHERE EMPNO BETWEEN 7689 AND 9702

-- 1980�⿡ �Ի����� ���� ��� ��ȸ
SELECT *
FROM EMP
WHERE NOT HIREDATE '1980/01/01' AND '1980/12/31';

-- LIKE, NOT LIKE ������ : �Ϻι��ڿ��� ���ԵǾ� �ִ��� ���θ� Ȯ���ϴ� ������, �ַ� �˻����� ���
-- % : ���̿� ������� ��� ���ڸ� �ǹ�
--_ :���� 1�ڸ� �ǹ�
SELECT EMPNO, ENAME
FROM EMP
WHERE ENAME LIKE '%K%';

SELECT *
FROM EMP
WHERE ENAME LIKE '_L%';

-- ��� �̸��� AM�� ���ԵǾ� �ִ� ��������� ���
-- ��� �̸��� AM�� ���ԵǾ� ���� ���� ��������� ���
SELECT *
FROM EMP
WHERE ENAME LIKE '%AM%';

SELECT *
FROM EMP
WHERE ENAME NOT LIKE '%AM%';
-- ����̸��� AM�� ���ԵǾ� ���� ���� ��������� ���

-- NULL : ��Ȯ�� �Ǵ� �˼� ���� ���� �ǹ���, �׷��� ����, �Ҵ�, �� �Ұ�( = , N)
SELECT SAL*12+COMM AS ����, COMM
FROM EMP;

SELECT *
FROM EMP
WHERE COMM = NULL;

SELECT *
FROM EMP
WHERE ename LIKE '%\%P' ESCAPE '\';

SELECT ename, sal, sal*12+comm as annsal, comm
FROM EMP;