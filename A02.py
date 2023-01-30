#N 個の整数 A1​ ,A2​ ,⋯,AN​ の中に整数Xが含まれるかどうかを判定するプログラム
#入力形式↓#####
#N X
#A1 A2 A3 A4...
##############

#map:リストの各要素に対して関数・処理を実行
N, X = map(int, input().split())
A = list(map(int, input().split()))

#if in リストAにXが含まれているか
if X in A:
    print("Yes")
else:
    print("No")
