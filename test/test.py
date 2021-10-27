#051
movie_rank =['닥터 스트레인지', '스플릿','럭키']

#052
movie_rank.append("배트맨")

#0523
movie_rank.insert(1,"슈퍼맨")

#054
movie_rank.remove("럭키")

#055
movie_rank.remove("스플릿")
movie_rank.remove("배트맨")

#056
lang1 = set(["C","C++","JAVA"])
lang2 = set(["Python","Go","C#"])
langs = lang1 | lang2

#057
nums = [1,2,3,4,5,6,7]
print(max(nums))
print(min(nums))

#058
nums=[1,2,3,4,5]
sum =0
for n in nums:
  sum +=n
print(sum)

#059
cook =["피자","김밥","만두","양념치킨","족발","김치만두","쫄면","쏘세지","라면","팥빙수","김치전"]
print(len(cook))

#060
nums=[1,2,3,4,5]
sum =0
for n in nums:
  sum +=n
print(sum/len(nums))

#121
ch = input()
if ch.islower():
  print(ch.upper())
 
else:
  print(ch.lower())

#122
score = int(input())
if score>100:
  print("0과 100사이의 점수를 입력하십시오.")
elif score >=81:
  print('A')
elif score >=61:
  print('B')
elif score >=41:
  print('C')
elif score >=21:
  print('D')
elif score >=0:
  print('E')
else:
  print("0과 100사이의 점수를 입력하십시오.")

#123
money = '100 달러'
print(money[money.find(" ")+1:])


#126
print("우편번호: ")
postNumber = int(input())
seoul = postNumber[:3]
if seoul>=0 and seoul<3:
  print('강북구')
