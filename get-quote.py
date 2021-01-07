import random
def primary():
  #print("Keep it logically awesome.")

  f = open("quotes.txt")  #打开quotes.txt文件
  quotes = f.readlines()  #将文件里每一行内容存入数组
  f.close()               #关闭文件
  last = 13
  rnd = random.randint(0,last) #随机抽取一个数字（0，13）
  print(quotes[rnd])

if __name__== "__main__":
  primary()
