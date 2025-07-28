from dotenv import load_dotenv
from ai import get_personality_analysis

load_dotenv

print("# AI 관상가입니다. 얼굴특징을 입력해주시면 성격과 미래를 전망해드릴게요.")
line = input("얼굴 특징: ").strip()

if not line: 
    #참거짓을 해야함 : 빈칸이면 거짓. 뭐라고 써있으면 참
    print("에러: 얼굴 특징을 입력하지 않으셨습니다.")
else: 
    print("입력하신 얼굴 특징",line)
    print("분석중 ...")
    result = get_personality_analysis(line)
    print("분석완료!")
    print(result)

#print(repr(line))

#get_personality_analysis()