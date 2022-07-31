import time
# 初始值
IV = [0X7380166f, 0X4914b2b9, 0X172442d7, 0Xda8a0600, 0Xa96f30bc, 0X163138aa, 0Xe38dee4d, 0Xb0fb0e4e]

# 常量
def Tj(j):
    if 0 <= j <= 15:
        return 0x79cc4519
    elif 16 <= j <= 63:
        return 0x7a879d8a

# 布尔函数
def FFj(X, Y, Z, j):
    if 0 <= j <= 15:
        return X ^ Y ^ Z
    elif 16 <= j <= 63:
        return (X & Y) | (X & Z) | (Y & Z)

def GGj(X, Y, Z, j):
    if 0 <= j <= 15:
        return X ^ Y ^ Z
    elif 16 <= j <= 63:
        return (X & Y) | (~X & Z)

# 循环k比特左移
def Rol(X, k):
    n = k % 32
    return ((X << n) & 0xFFFFFFFF) ^ ((X >> (32 - n)) & 0xFFFFFFFF)

# 置换函数
def P0(X):  # 压缩函数中的置换函数
    return X ^ (Rol(X, 9)) ^ (Rol(X, 17))

def P1(X):  # 消息扩展中的置换函数
    return X ^ (Rol(X, 15)) ^ (Rol(X, 23))

# 填充
def Fill(M):  # 输入十六进制
    m = bin(int(M, 16))[2:].zfill(len(M) * 4)  # 消息M的二进制表示并补0
    l = len(m)  # l代表消息的二进制长度
    l64 = '0' * (64 - len(bin(l)[2:])) + bin(l)[2:]  # 长度l的64位二进制表示
    l1 = l + 1 + 64
    k = 512 - l1 % 512
    m1 = m + '1' + k * '0' + l64  # 消息的二进制表示
    m1 = hex(int(m1, 2))[2:]  # 消息的十六进制表示
    return m1

# 迭代过程  分组和迭代需要分为两个函数
def Grouping(m1):
    n = int(len(m1) / 128)  # 将填充后的消息m′按512比特(128个十六进制数)进行分组,n=(l+k+65)/512
    B = [0] * n
    for i in range(n):
        B[i] = m1[128 * i:128 * (i + 1)]
    return B

def Iterative(B):
    n = len(B)
    V=[]
    V.append(IV)
    for i in range(n):
        V.append(CF(V,B,i))
    return V[n]

# 消息扩展
def Extension(B, i):
    W = [0] * 68
    w = [0] * 64
    for I in range(16):
        W[I] = int(B[i][8 * I:8 * (I + 1)],16) # 将消息分组B划分为16个字，一个字32bit 8个十六进制数,异或需int类型，故提前转换
    for j in range(16, 68):
        W[j] = P1(W[j - 16] ^ W[j - 9] ^ Rol(W[j - 3], 15))^ Rol(W[j - 13], 7) ^ W[j - 6]
    for j in range(64):
        w[j] = W[j] ^ W[j + 4]
    return W, w

# 压缩函数
def CF(V, B, i):
    W, w = Extension(B, i)
    A=V[i][0]
    B=V[i][1]
    C=V[i][2]
    D=V[i][3]
    E=V[i][4]
    F=V[i][5]
    G=V[i][6]
    H=V[i][7]
    A, B, C, D, E, F, G, H = V[i]
    for j in range(64):
        SS1 = Rol((Rol(A, 12) + E + Rol(Tj(j), j) & 0xFFFFFFFF), 7)  # mod2^32算术加运算
        SS2 = SS1 ^ (Rol(A, 12))
        TT1 = (FFj(A, B, C, j) + D + SS2 + w[j]) & 0xFFFFFFFF  # mod2^32算术加运算
        TT2 = (GGj(E, F, G, j) + H + SS1 + W[j]) & 0xFFFFFFFF  # mod2^32算术加运算
        D = C
        C = Rol(B, 9)
        B = A
        A = TT1
        H = G
        G = Rol(F, 19)
        F = E
        E = P0(TT2)

    Vi_1 = A^V[i][0], B^V[i][1], C^V[i][2], D^V[i][3], E^V[i][4], F^V[i][5], G^V[i][6], H^V[i][7]   #元组和列表不能异或，V[i+1]报错
    return Vi_1

def SM3(M):
#M = input("请输入十六进制字符串：")
    m1 = Fill(M)  #将消息M进行填充，填充后的消息m1 的比特长度为512的倍数。
    B = Grouping(m1)   #将填充后的消息m1按512比特进行分组：m′ = B(0)B(1)· · · B(n−1）
    Vn = Iterative(B)  #对m1进行迭代：
    #Vn是二进制，转换成16进制
    result = ''
    for i in Vn:
        result += hex(i)[2:].zfill(8)#+' '  #补充0
    return(result)

t0=time.time()
for i in range (1000):
    SM3('61626364'*16)
t1 = time.time()
print('python代码运行时间为：',(t1-t0)/1000,'s')
