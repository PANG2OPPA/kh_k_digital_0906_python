# 파일쓰기 : 파일을 읽거나 쓰기 위해서는 반드시 open() 해야 함
# 파일객체 = open(파일명, 파일모드, 인코딩)
# 파일명 : 파일경로 + 파일명 (파일경로를 입력하지 않으면 현재 위치에 저장
# 파일모드 : r(읽기), w(쓰기), a(추가, 파일이 없으면 생성하고 추가, 있으면 파일의 마지막에 추가)
score_file = open("score.txt", "a", encoding="utf-8")
print("수확 : 50", file=score_file)
print("영어 : 90", file=score_file)
score_file.write("국어 : 98" + "\n")
score_file.write("과학 : 45" + "\n")
score_file.close()

# 파일읽기
# read() : 파일내의 모든 내용을 읽어 하나의 문자열로 반환
# readline() : 해당 파일의 내용을 한 라인씩 읽어 들여 문자열로 변환, 더 이상 읽을 내용이 없으면 None 반환
# readLines() : 해당 파일의 모든 순서대로 읽어 각각의 라인의 하나의 요소로 저장하는 리스트를 반환
score_file = open("score.txt", "r", encoding="utf-8")
# print(score_file.read())
# score_file.closee