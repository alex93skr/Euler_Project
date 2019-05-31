print(f'------------------------1--')

# arr = []
# nn = 0

# for i in range(1000):
#     if i % 3 == 0 or i % 5 == 0:
#         arr.append(i)
#
# # print(arr)
# for i in arr:
#     nn += i
# print('>>>', nn)


print(f'-----------------------2--')

# sum = 2
#
# fb1 = 1
# fb2 = 2
# i = 3
# nn1, nn2 = 0, 0

# while i <= 4_000_000:
#     # print(i, end='')
#     if i % 2 == 0:
#         # print(' shet')
#         sum += i
#     fb1 = fb2
#     fb2 = i
#     i = fb1 + fb2
#
# print('>>>', sum)


print(f'-----------------------3--')



n = 600851475143
i = 2
while i * i <= n:
    while n % i == 0:
        n = n / i
    i = i + 1
print(n)

# def prost(a):
#     return all(a % i for i in range(2, int(a)))


# print(prost(3))
# print(prost(4))

#
# i = 2
# while True:
#     if i < 60085147514 and 600851475143 % i == 0:
#         print('600851475143 /', i, '=', 600851475143 / i, prost(600851475143 / i))
#     i += 1


print(f'-----------------------4--')

def is_palindrome(string):          # палиндром
    reversed_string = string[::-1]
    return string == reversed_string


nn = 100

for i in range(99, 1001):
    for n in range(100, 1000):
        if is_palindrome(str(i*n)):
            print(i, '*', n, '=', i*n)

print(f'-----------------------5--')

def euler5(limit):
  hasNumberFound = False
  iterator = 1

  while not hasNumberFound:
    num = limit * iterator

    for divider in range(2, limit):
      if num % divider != 0:
        break
    else:
      hasNumberFound = True
      return num
    iterator += 1

print( euler5(20) )

print(f'-----------------------6--')

# # (1 + 2 + ... + 10)2 = 552 = 3025
zz1 = 0
for i in range(1, 101):
    zz1 += i
    # print(i, zz1)
print('>>', zz1 ** 2)

# 12 + 22 + ... + 102 = 385
zz2 = 0
for ttt in range(1, 101):
    zz2 += ttt ** 2
    # print(ttt, zz2)
print('>>', zz2)

# # 3025 − 385 = 2640.

zz3 = zz1 ** 2 - zz2

print(zz1 ** 2, zz2, zz3)
print(f'-----------------------7--')


def prost(a):
    return all(a % i for i in range(2, a))


i = 1
z = 0

while True:
    i += 1
    if prost(i):
        z += 1
        print(z, i)
    if z == 10001:
        print(z, i)
        break

print(f'----------------------8--')

sss = '7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450'

print('>', sss, '<')

lng = 13
max = 0

print('>', len(sss))

for i in range(len(sss) - lng + 1):
    print(i)
    tmp = 1
    for n in range(i, i + lng):
        tmp *= int(sss[n])
        print(i, sss[n], tmp)
    if tmp > max:
        max = tmp

print('>>', max)

print(f'----------------------9--')

a, b, c = 1, 2, 3

for a in range(1, 1000):
    print(a)
    b = a + 1
    while b < c and b < 1000:
        b += 1
        # print(a, b, c)
        c = b + 1
        while a < b and c < 1000:
            c += 1
            # print(a, b, c)
            if (a ** 2 + b ** 2 == c ** 2) and (a + b + c == 1000):
                print('>>>', a, b, c)
                quit()

print(f'----------------------10--')


def isPrime(n):
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n and n % d != 0:
        d += 2
    return d * d > n


n = 0
for i in range(2, 2_000_000):
    if isPrime(i):
        n += i
        print(i, n)

print(f'----------------------11--')

arr = [
    '08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08',
    '49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00',
    '81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65',
    '52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91',
    '22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80',
    '24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50',
    '32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70',
    '67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21',
    '24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72',
    '21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95',
    '78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92',
    '16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57',
    '86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58',
    '19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40',
    '04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66',
    '88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69',
    '04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36',
    '20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16',
    '20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54',
    '01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48']

max = 0


def diag_back():
    global max
    for i in range(0, 17):
        # print(arr[i])
        for n in range(9, 58, 3):
            # print(arr[i][n:n+2], arr[i+1][n-3:n-1], arr[i+2][n-6:n-4], arr[i+3][n-9:n-7])
            tmp = int(arr[i][n:n + 2]) \
                  * int(arr[i + 1][n - 3:n - 1]) \
                  * int(arr[i + 2][n - 6:n - 4]) \
                  * int(arr[i + 3][n - 9:n - 7])
            if tmp > max:
                max = tmp
    return max


def diag():
    global max
    for i in range(17):
        # print(arr[i])
        for n in range(0, 50, 3):
            # print(arr[i][n:n+2],
            #       arr[i+1][n+3:n+5],
            #       arr[i+2][n+6:n+8],
            #       arr[i+3][n+9:n+11])
            tmp = int(arr[i][n:n + 2]) \
                  * int(arr[i + 1][n + 3:n + 5]) \
                  * int(arr[i + 2][n + 6:n + 8]) \
                  * int(arr[i + 3][n + 9:n + 11])
            if tmp > max:
                max = tmp
    return max


def down():
    global max
    for i in range(0, 58, 4):  # вниз
        # print('--')
        for n in range(17):
            # print(arr[n][i + 0:i + 2],
            #       arr[n + 1][i + 0:i + 2],
            #       arr[n + 2][i + 0:i + 2],
            #       arr[n + 3][i + 0:i + 2])
            tmp = int(arr[n][i + 0:i + 2]) * \
                  int(arr[n + 1][i + 0:i + 2]) * \
                  int(arr[n + 2][i + 0:i + 2]) * \
                  int(arr[n + 3][i + 0:i + 2])
            if tmp > max:
                max = tmp
    return max


def right():
    global max
    for i in arr:  # вправо
        # print(i)
        for n in range(0, 49, 3):
            # print(i[n:n + 2],
            #       i[n + 3:n + 5],
            #       i[n + 6:n + 8],
            #       i[n + 9:n + 11])
            tmp = int(i[n:n + 2]) * \
                  int(i[n + 3:n + 5]) * \
                  int(i[n + 6:n + 8]) * \
                  int(i[n + 9:n + 11])
            if tmp > max:
                max = tmp
    return max


# diag()
# down()
# right()


print(diag_back())
print(down())
print(diag())
print(right())

# вверх, вниз, вправо, влево

print(f'----------------------12--')

from collections import Counter


def get_ls(n):  # ДЕЛИТЕЛИ
    """Разложить число на множители"""
    # result = [1]
    result = []
    i = 2
    while i < n:
        if n % i == 0:
            n /= i
            result.append(i)
        else:
            i += 1
    result.append(int(n))
    return result


def delitel_max(zzz):
    ls = get_ls(zzz)
    kkk = dict(Counter(ls)).items()
    d = [k for k, _ in kkk]
    m = [v for _, v in kkk]
    k = [0 for _ in range(len(set(ls)))]

    ln = range(len(m))

    max = 0

    try:
        while True:
            r = 1
            for i1, i2 in zip(d, k):
                r *= i1 ** i2
            # print(r)
            max += 1

            k[0] += 1
            for i in ln:
                if k[i] > m[i]:
                    k[i] = 0
                    k[i + 1] += 1  # IndexError
    except IndexError:
        pass

    return max


for n in range(1, 10000000000):

    print('>>>', n - 1, '-e TREUG: ', end='')

    treug = 0
    for i in range(0, n):
        treug += i

    print(treug, end='')

    tmp = delitel_max(treug)

    print(' deliteley:', tmp)
    # print(n - 1, '-e teyg 4islo:', zz, 'deliteley:', delitel)

    if tmp >= 500:
        print('>>>', treug)
        quit()

print(f'----------------------13--')

data = (37107287533902102798797998220837590246510135740250,
        46376937677490009712648124896970078050417018260538,
        74324986199524741059474233309513058123726617309629,
        91942213363574161572522430563301811072406154908250,
        23067588207539346171171980310421047513778063246676,
        89261670696623633820136378418383684178734361726757,
        28112879812849979408065481931592621691275889832738,
        44274228917432520321923589422876796487670272189318,
        47451445736001306439091167216856844588711603153276,
        70386486105843025439939619828917593665686757934951,
        62176457141856560629502157223196586755079324193331,
        64906352462741904929101432445813822663347944758178,
        92575867718337217661963751590579239728245598838407,
        58203565325359399008402633568948830189458628227828,
        80181199384826282014278194139940567587151170094390,
        35398664372827112653829987240784473053190104293586,
        86515506006295864861532075273371959191420517255829,
        71693888707715466499115593487603532921714970056938,
        54370070576826684624621495650076471787294438377604,
        53282654108756828443191190634694037855217779295145,
        36123272525000296071075082563815656710885258350721,
        45876576172410976447339110607218265236877223636045,
        17423706905851860660448207621209813287860733969412,
        81142660418086830619328460811191061556940512689692,
        51934325451728388641918047049293215058642563049483,
        62467221648435076201727918039944693004732956340691,
        15732444386908125794514089057706229429197107928209,
        55037687525678773091862540744969844508330393682126,
        18336384825330154686196124348767681297534375946515,
        80386287592878490201521685554828717201219257766954,
        78182833757993103614740356856449095527097864797581,
        16726320100436897842553539920931837441497806860984,
        48403098129077791799088218795327364475675590848030,
        87086987551392711854517078544161852424320693150332,
        59959406895756536782107074926966537676326235447210,
        69793950679652694742597709739166693763042633987085,
        41052684708299085211399427365734116182760315001271,
        65378607361501080857009149939512557028198746004375,
        35829035317434717326932123578154982629742552737307,
        94953759765105305946966067683156574377167401875275,
        88902802571733229619176668713819931811048770190271,
        25267680276078003013678680992525463401061632866526,
        36270218540497705585629946580636237993140746255962,
        24074486908231174977792365466257246923322810917141,
        91430288197103288597806669760892938638285025333403,
        34413065578016127815921815005561868836468420090470,
        23053081172816430487623791969842487255036638784583,
        11487696932154902810424020138335124462181441773470,
        63783299490636259666498587618221225225512486764533,
        67720186971698544312419572409913959008952310058822,
        95548255300263520781532296796249481641953868218774,
        76085327132285723110424803456124867697064507995236,
        37774242535411291684276865538926205024910326572967,
        23701913275725675285653248258265463092207058596522,
        29798860272258331913126375147341994889534765745501,
        18495701454879288984856827726077713721403798879715,
        38298203783031473527721580348144513491373226651381,
        34829543829199918180278916522431027392251122869539,
        40957953066405232632538044100059654939159879593635,
        29746152185502371307642255121183693803580388584903,
        41698116222072977186158236678424689157993532961922,
        62467957194401269043877107275048102390895523597457,
        23189706772547915061505504953922979530901129967519,
        86188088225875314529584099251203829009407770775672,
        11306739708304724483816533873502340845647058077308,
        82959174767140363198008187129011875491310547126581,
        97623331044818386269515456334926366572897563400500,
        42846280183517070527831839425882145521227251250327,
        55121603546981200581762165212827652751691296897789,
        32238195734329339946437501907836945765883352399886,
        75506164965184775180738168837861091527357929701337,
        62177842752192623401942399639168044983993173312731,
        32924185707147349566916674687634660915035914677504,
        99518671430235219628894890102423325116913619626622,
        73267460800591547471830798392868535206946944540724,
        76841822524674417161514036427982273348055556214818,
        97142617910342598647204516893989422179826088076852,
        87783646182799346313767754307809363333018982642090,
        10848802521674670883215120185883543223812876952786,
        71329612474782464538636993009049310363619763878039,
        62184073572399794223406235393808339651327408011116,
        66627891981488087797941876876144230030984490851411,
        60661826293682836764744779239180335110989069790714,
        85786944089552990653640447425576083659976645795096,
        66024396409905389607120198219976047599490197230297,
        64913982680032973156037120041377903785566085089252,
        16730939319872750275468906903707539413042652315011,
        94809377245048795150954100921645863754710598436791,
        78639167021187492431995700641917969777599028300699,
        15368713711936614952811305876380278410754449733078,
        40789923115535562561142322423255033685442488917353,
        44889911501440648020369068063960672322193204149535,
        41503128880339536053299340368006977710650566631954,
        81234880673210146739058568557934581403627822703280,
        82616570773948327592232845941706525094512325230608,
        22918802058777319719839450180888072429661980811197,
        77158542502016545090413245809786882778948721859617,
        72107838435069186155435662884062257473692284509516,
        20849603980134001723930671666823555245252804609722,
        53503534226472524250874054075591789781264330331690)

nn = 0

print(len(data))

for i in range(len(data)):
    print(i)
    nn += data[i]

print(nn)
print(str(nn)[:10])

print(f'----------------------14--')

elem = 0
shag_max = 0

for i in range(1, 1_000_000):
    shag = i
    shag_n = 1

    # print(shag, '-> ', end='')

    while shag > 1:
        if shag % 2 == 0:  # чет
            shag //= 2
            # print(shag, ' ', end='')
        else:
            shag = 3 * shag + 1
            # print(shag, ' ', end='')
        shag_n += 1

    # print(shag)
    # print('SHAGOV -', shag_n)
    if shag_n > shag_max:
        elem = i
        shag_max = shag_n

print('>>>', elem, shag_max)

print(f'----------------------15--')

import copy

side = 3

matrix = []
routes = []


def make_matrix(n):
    for stroka in range(n):
        zz = []
        for ryad in range(n):
            zz.append('0')
        matrix.append(zz)


def print_matrix_border(name):
    for i in name:
        print(i)

def print_matrix(name):
    for i in range(side):
        for n in range(side):
            if n == side-1:
                print(name[i][n])
            else:
                print(name[i][n], ' ', end='')


step = 1

make_matrix(side)
print_matrix(matrix)
print()

for stroka in range(side):
    for ryad in range(side):
        matrix[stroka][ryad] = 'X'
        print(matrix)
        if matrix not in routes:
            routes.append(copy.deepcopy(matrix))
            step += 1
            # print_matrix(name)
            # print()
print()
# print(routes)
print(step)
print()

matrix = []

make_matrix(side)

for stroka in range(side):
    for ryad in range(side):
        matrix[ryad][stroka] = 'X'

        if matrix not in routes:
            routes.append(copy.deepcopy(matrix))
            step += 1
            print(matrix)

print()
# print(routes)
print(step)
print()

# print_matrix(routes[399])


print(f'----------------------16--')


st = str(2**1000)
zz = 0
print(str(st))

for i in range(len(st)):
    zz += int(st[i])

print(zz)


print(f'----------------------17--')


units = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve",
         "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
scales = ["hundred", "thousand", "million", "billion", "trillion"]


def int2text(num):
    st = ''

    if str(num)[-4:-3]:
        st += units[int(str(num)[-4:-3])] + scales[1]
        # print('>', units[int(str(num)[-4:-3])], scales[1])
        if str(num)[-3:] == '000':
            return st
    if str(num)[-3:-2]:
        st += units[int(str(num)[-3:-2])] + scales[0]
        # print('>', units[int(str(num)[-3:-2])], scales[0])
        if str(num)[-2:] == '00':
            return st

        # print('> and')
        st += 'and'

    if str(num)[-2:-1]:  # двузнач
        if int(str(num)[-2:]) > 19:
            st += tens[int(str(num)[-2:-1])]
            # print('>', tens[int(str(num)[-2:-1])])
            if not int(str(num)[-1]) == 0:  # ноль вконце
                st += units[int(str(num)[-1])]
                # print('>', units[int(str(num)[-1])])
        else:
            st += units[int(str(num)[-2:])]
            # print('>', units[int(str(num)[-2:])])

    else:  # одознач
        st += units[int(str(num)[-1])]
        # print('>', units[int(str(num)[-1])])
    return st


def count_characters(st):
    # print(len(st.replace('-', '').replace(' ', '')))
    return len(st.replace('-', '').replace(' ', ''))


nn = 0

for i in range(1, 1001):
    nn += count_characters(int2text(i))
    print(i, int2text(i), count_characters(int2text(i)), nn)


print(f'----------------------18--')

tr1 = [
['', '', '', '', '', '', '', '', '', '', '', '', '', '', 75, '', '', '', '', '', '', '', '', '', '', '', '', '',''],
['', '', '', '', '', '', '', '', '', '', '', '', '', 95, '', 64, '', '', '', '', '', '', '', '', '', '', '', '',''],
['', '', '', '', '', '', '', '', '', '', '', '', 17, '', 47, '', 82, '', '', '', '', '', '', '', '', '', '', '',''],
['', '', '', '', '', '', '', '', '', '', '', 18, '', 35, '', 87, '', 10, '', '', '', '', '', '', '', '', '', '',''],
['', '', '', '', '', '', '', '', '', '', 20, '', 4, '', 82, '', 47, '', 65, '', '', '', '', '', '', '', '', '', ''],
['', '', '', '', '', '', '', '', '', 19, '', 1, '', 23, '', 75, '', 3, '', 34, '', '', '', '', '', '', '', '', ''],
['', '', '', '', '', '', '', '', 88, '', 2, '', 77, '', 73, '', 7, '', 63, '', 67, '', '', '', '', '', '', '', ''],
['', '', '', '', '', '', '', 99, '', 65, '', 4, '', 28, '', 6, '', 16, '', 70, '', 92, '', '', '', '', '', '', ''],
['', '', '', '', '', '', 41, '', 41, '', 26, '', 56, '', 83, '', 40, '', 80, '', 70, '', 33, '', '', '', '', '',''],
['', '', '', '', '', 41, '', 48, '', 72, '', 33, '', 47, '', 32, '', 37, '', 16, '', 94, '', 29, '', '', '', '',''],
['', '', '', '', 53, '', 71, '', 44, '', 65, '', 25, '', 43, '', 91, '', 52, '', 97, '', 51, '', 14, '', '', '',''],
['', '', '', 70, '', 11, '', 33, '', 28, '', 77, '', 73, '', 17, '', 78, '', 39, '', 68, '', 17, '', 57, '', '',''],
['', '', 91, '', 71, '', 52, '', 38, '', 17, '', 14, '', 91, '', 43, '', 58, '', 50, '', 27, '', 29, '', 48, '',''],
['', 63, '', 66, '', 4, '', 68, '', 89, '', 53, '', 67, '', 30, '', 73, '', 16, '', 69, '', 87, '', 40, '', 31, ''],
[4, '', 62, '', 98, '', 27, '', 23, '', 9, '', 70, '', 98, '', 73, '', 93, '', 38, '', 53, '', 60, '', 4, '', 23]]

tr = [
    ['', '', '', 3, '', '', ''],
    ['', '', 7, '', 4, '', ''],
    ['', 2, '', 4, '', 6, ''],
    [8, '', 5, '', 9, '', 3],
]

# for i in tr1:
#     print(len(i))

# print(tr[0][14])
# print(tr[1][13], tr[1][15])
# print(tr[14][28])


def print_animatrix(name):
    for i in range(len(name)):
        for j in range(len(name[i])):
            if name[i][j] == '' and j != len(name[i])-1:
                print('  ', end='')
            elif name[i][j] != '' and j != len(name[i])-1:
                print(str(name[i][j]).zfill(2), end='')
            elif name[i][j] == '' and j == len(name[i])-1:
                print('  ')
            elif name[i][j] != '' and j == len(name[i])-1:
                print(str(name[i][j]).zfill(2))


import copy
import time
import pyautogui
import sys

ttl = []
ttl_copy = []
way_max = 0

ttl_copy = copy.deepcopy(tr1)


def perebor(name, st, rd, way_n):

    global way_max

    max_st = len(name)
    max_rd = len(name[0])

    print('> RABOTAEM:', max_st, 'x', max_rd, '-', st, rd, way_n)
    # print('>>', name[st][rd], way_n)

    if way_n == '-':       # new
        ttl.append([name[st][rd]])
        way_n = 0
    else:
        ttl[way_n].append(name[st][rd])

    # print(ttl)

    if st + 1 < max_st:

        way_max += 1
        tmp = copy.deepcopy(ttl[way_n])
        ttl.append(tmp)
        tmp = str(st+1)+'x'+str(rd+1)
        ttl[way_max].append(tmp)

        # ANIMAtRiXXXXXXXXXxxxxxxxxx!!!!

        ttl_copy[st][rd] = '**'
        print_animatrix(ttl_copy)

        pyautogui.click(x=1600, y=500)
        pyautogui.hotkey('ctrl', 'l')
        # time.sleep(0.1)

        #

        perebor(name, st+1, rd-1, way_n)



# perebor(tr, 0, 3, '-')

perebor(tr1, 0, 14, '-')

print()

# for i in ttl:
#     print(i)

print('-------')

# print(len(ttl))

winner = 0

while True:
    go_next = False
    for i in range(len(ttl)):
        # print(ttl[i], len(ttl[i]))
        for j in range(len(ttl[i])):
            # print(ttl[i][j])
            # print(type(j))
            if type(ttl[i][j]) == str:
                go_next = True
                z1 = int(ttl[i][j][:ttl[i][j].find('x')])
                z2 = int(ttl[i][j][ttl[i][j].find('x')+1:])
                # print(True, z1, z2)
                del ttl[i][j]
                perebor(tr1, z1, z2, i)
    if not go_next:
        print()
        for i in ttl:
            # print(i)
            tmp = sum(i)  # 15
            if winner < tmp:
                winner = tmp
        print('>>>', winner)
        print('EXIT')

        # print(sys.getsizeof(ttl))

        quit()

print(f'----------------------19--')

day_name = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']


# 1 января 1900 года - понедельник.
# В апреле, июне, сентябре и ноябре 30 дней.
# В феврале 28 дней, в високосный год - 29.
# В остальных месяцах по 31 дню.

def month2day(n, leap_year):
    mm = 4, 6, 9, 11
    if n in mm:
        return 30
    elif n == 2 and leap_year:
        return 29
    elif n == 2 and not leap_year:
        return 28
    else:
        return 31


def leap_year(n):
    if str(n)[-2:] == '00':
        if n % 400 == 0:
            return True
        else:
            return False
    elif n % 4 == 0:
        return True
    else:
        return False


# print(leap_year(2020))
# print(month2day(12, True))

year, month, day = 1900, 1, 1
day_ow_week = 1
sunday = 0
sunday_find = 0

# year, month, day = 2000, 12, 31
# and not month == 12 and not day == 31

while True:
    leap_y = leap_year(year)
    month = 1

    while month <= 12:
        day = 1

        while day <= month2day(month, leap_y):
            print(year, leap_y, month, day, day_name[day_ow_week - 1])
            if day_ow_week == 7:
                day_ow_week = 1
                sunday += 1
                if year >= 1901 and day == 1:
                    sunday_find += 1
            else:
                day_ow_week += 1
            if year == 2000 and month == 12 and day == 31:
                print()
                print('Всего воскресений:', sunday)
                print('Воскресений на первое число месяца:', sunday_find)
                quit()
            day += 1
        month += 1
    year += 1

# с 1 января 1901 года до 31 декабря 2000 года)?

# 1	Январь
# 2	Февраль
# 3	Март
# 4	Апрель
# 5	Май
# 6	Июнь
# 7	Июль
# 8	Август
# 9	Сентябрь
# 10	Октябрь
# 11	Ноябрь
# 12	Декабрь


# Високосный год - любой год, делящийся нацело на 4,
# однако последний год века (ХХ00) является високосным в том и только том случае,
# если делится на 400.



print(f'----------------------20--')


nn, nnn = 1, 0

for i in range(100, 0, -1):
    nn *= i

print(nn)
nn = str(nn)

for i in range(len(nn)):
    print('+', nn[i], end='')
    nnn += int(nn[i])

print('>>', nnn)


print(f'----------------------21--')


def divider(n):     # ДЕЛИТЕЛИ
    result = []
    i = 1
    while i < n:
        if n % i == 0:
            result.append(i)
        i += 1
    return result

arr = []
res = 0

for i in range(10001):
    tmp = sum(divider(i))
    print(i, tmp)
    arr.append([i, tmp])

print()

for i in range(len(arr)):

    for j in range(len(arr)):
        if not arr[i][0] == arr[i][1] and arr[i][0] == arr[j][1] and arr[i][1] == arr[j][0]:
            print(arr[i], arr[j])
            res += arr[i][0] + arr[j][1]

print('>>', res, '/ 2 =', int(res/2))


print(f'----------------------22--')

abc = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
       'W', 'X', 'Y', 'Z']
st = ''


def letter_number(n):
    return abc.index(n) + 1

f = open("names.txt", "r")
for line in f:
    st = line
f.close()

arr = st.split(',')
arr.sort()
res = 0

for i in range(len(arr)):
    print(i + 1, arr[i], '> ', end='')
    sum_i = 0
    for n in arr[i]:
        tmp = letter_number(n)
        print(tmp, ' ', sep='', end='')
        sum_i += int(tmp)
    points = (i + 1) * sum_i
    res += points

    print('=', sum_i, points, res)


print(f'----------------------23--')


excess_numbers = []



def sum_divider(n):  # ДЕЛИТЕЛИ
    i = 1
    res = 0
    tmp = n / 2 + 1
    while i < tmp:
        if n % i == 0:
            res += i
        i += 1
    return res


def perfect_number(n):
    return True if n == sum_divider(n) else False



def arr_index(n):
    try:
        excess_numbers.index(n)
    except ValueError:
        return False
    else:
        return True

print(perfect_number(28))
print(arr_index(0))


ress = 0


# for i in range(28100, 11111111111):
for i in range(1, 28130):
# for i in range(1, 33):
    found = False
    for j in range(0, len(excess_numbers)):
        tmp = i - excess_numbers[j]
        # print(tmp)
        if tmp in excess_numbers:
            print(i, '(', excess_numbers[j], '+', excess_numbers[excess_numbers.index(tmp)], ')')
            found = True
            break
        else:
            pass
    if found == False:
        ress += i
        print(i, '>', ress)


print('>>', ress)


print(f'----------------------24--')

from itertools import permutations


a = ('0','1','2')
a = ('0','1','2','3','4','5','6','7','8','9')
n = len(a)
rep = 1


res = 1

for i in permutations(a * rep, n):
    tmp = ''.join(i)
    print(tmp, res)
    if res == 1_000_000:
        quit()
    res += 1


print(f'----------------------25--')



fib1, fib2 = 0, 1
n = 0

while len(str(fib1)) != 1000:
    tmp = fib1 + fib2
    fib1 = fib2
    fib2 = tmp
    n += 1
    print(n, fib1)


print(f'----------------------26--')

num = longest = 1
for n in range(3, 1000, 2):
    if n % 5 == 0:
        continue

    p = 1
    while (10 ** p) % n != 1:
        p += 1

    if p > longest:
        num, longest = n, p

print(num)

print(f'----------------------27--')



def is_prime(n):        # простые числа		from prime
    if n==2 or n==3: return True
    if n%2==0 or n<2: return False
    for i in range(3,int(n**0.5)+1,2):   # only odd numbers
        if n%i==0:
            return False
    return True



# for i in range(44):
#     print(i, i**2 + i + 41, is_prime(i**2 + i + 41), (i**2 + i + 41)/41)
#
# print()
#
#
# for i in range(85):
#     print(i, i**2 - 79 * i + 1601, is_prime(i**2 - 79 * i + 1601))


lim = 1000


for a in range(-1 * lim, lim + 1):
    for b in range(-1 * lim, lim + 1):

        posled = 0
        for n in range(-1 * lim, lim + 1):
            if is_prime(n ** 2 + a * n + b):
                posled += 1
                # print(a, b, n, (n ** 2 + a * n + b), is_prime(n ** 2 + a * n + b))
            else:

                print(a,b,n,posled)
                break

# n2+an+b

print(f'----------------------28--')


# 5 на 5
#
# 21 22 23 24 25
# 20  7  8  9 10
# 19  6  1  2 11
# 18  5  4  3 12
# 17 16 15 14 13

# ряды - rows
# столбы - columns


mat = []


def make_spiral_matrix(n):      # спиральная матрица ВПРАВО
    for i in range(n):
        mat.append([0 for a in range(n)])

    row, col = n // 2, n // 2
    num = 1
    direction = 'right'

    mat[row][col] = num

    # for i in mat:
    #     print(i)

    print()

    while True:

        num += 1
        # print(num, '>', row, col, direction)

        try:
            if direction == 'right':
                col += 1
                if mat[row + 1][col] == 0:
                    direction = 'down'
            elif direction == 'down':
                row += 1
                if mat[row][col - 1] == 0:
                    direction = 'left'
            elif direction == 'left':
                col -= 1
                if mat[row - 1][col] == 0:
                    direction = 'up'
            elif direction == 'up':
                row -= 1
                if mat[row][col + 1] == 0:
                    direction = 'right'
        except IndexError:
            break

        # print(num, '>>', row, col, direction)

        mat[row][col] = num

        # for i in mat:
        #     print(i)
        #
        # print()

def sum_diagonals(name):
    res = 0
    for i in range(len(name)):
        print('>', res, name[i][i])
        res = res + name[i][i]
    print()
    n = 0
    for i in range(len(name)-1, -1, -1):
        print('>>', res, i, n, name[i][n])
        res = res + name[i][n]
        n += 1

    print(res)
    res = res - name[len(name) // 2][len(name) // 2]
    print(res)


make_spiral_matrix(1001)


print()

for i in mat:
    print(i)

print()


sum_diagonals(mat)


print(f'----------------------29--')


limits = [2,100]
res = []

for i in range(limits[0], limits[1]+1):
    for n in range(limits[0], limits[1]+1):
        tmp = i ** n
        print(i, n, tmp)
        if tmp not in res:
            res.append(tmp)

print(len(res))

print(f'----------------------30--')

def sum_of_degrees(n):
    n = str(n)
    res = 0
    for i in range(len(str(n))):
        res = res + int(n[i])**5
    return res


print(sum_of_degrees(1634))

res = 0
for i in range(3, 1_000_000):
    if i == sum_of_degrees(i):
        res = res + i
        print('>', i, res)
    if i % 1_000_000 == 0:
        print(i)

print(res)

print(f'----------------------31--')






print(f'----------------------32--')





from itertools import permutations      # все возможные перестановки ПЕРЕБОР

res = 0
prz = []

def check_multipliers(n):
    global res, prz
    # print(n)
    n = str(n)
    for i in range(1, len(n)-1):
        for j in range(i+1, len(n)):
            if int(n[:i]) * int(n[i:j]) == int(n[j:]):
                # print(i, '>', n[:i], n[i:j], n[j:])
                print(n[:i] + '*' + n[i:j] + '=' + n[j:])
                prz += [int(n[j:])]
                # return n[:i] + '*' + n[i:j] + '=' + n[j:]


a = [*'123456789']
n = len(a)
rep = 1
for i in permutations(a * rep, n):
    tmp = int(''.join(i))
    check_multipliers(tmp)
    # if not check_multipliers(tmp) == None:
    #     print(check_multipliers(tmp))

print(prz)
prz = list(set(prz))
print(prz)
import numpy

print('>>>', numpy.sum(prz))


print(f'----------------------33--')


arr = []


for i in range(10,100):

    if '0' not in str(i):
        arr += [i]

print(arr)


for i in arr:
    for j in arr:
        # if not i == j and str(i)[0] == str(j)[1]:
        #     # print(i, j, str(i)[0], str(j)[1])
        #     if i/j == int(str(i)[1]) / int(str(j)[0]):
        #         print(i, j)

        if not i == j and str(i)[1] == str(j)[0]:
            if i/j == int(str(i)[0]) / int(str(j)[1]):
                print(i, '/', j, '=', i/j, '-->', str(i)[0], '/', str(j)[1], '=', int(str(i)[0]) / int(str(j)[1]))



print(f'----------------------34--')

import math

def fac_sum(n):
    tmp = 0
    for i in str(n):
        tmp += math.factorial(int(i))
    return tmp

for i in range(3, 100000000):
    if i == fac_sum(i):
        print(i)
    if i % 100_000 == 0:
        print('>', i)


print(f'----------------------35--')

def is_prime(n):        # простые
    if n==2 or n==3: return True
    if n%2==0 or n<2: return False
    for i in range(3,int(n**0.5)+1,2):   # only odd numbers
        if n%i==0:
            return False
    return True

# print(is_prime(5))

def permutation(n):
    n = str(n)
    for i in range(len(n)-1):
        n = n[1:] + n[0]
        print(n, '',end='')
        if not is_prime(int(n)):
            return False
    return True


permutation(10)

res = 0

for i in range(1_000_001):
# for i in range(1000):
    if is_prime(i):
        print(i, ': ', end='')
        if permutation(i):
            res += 1
        print()


# 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79 и 97

print('>', res)

print(f'----------------------36--')

def palindrome(string):                    # палиндром
    reversed_string = string[::-1]
    return string == reversed_string

res = 0

for i in range(1, 1_000_001):
    # print(i, palindrome(str(i)), bin(i), str(bin(i))[2:])
    if palindrome(str(i)) and str(bin(i))[2] != 0 and palindrome(str(bin(i))[2:]):
        print(i, str(bin(i))[2:], True)
        res += i

print('>', res)

print(f'----------------------37--')



def is_prime(n):        # простые
    if n==2 or n==3: return True
    if n%2==0 or n<2: return False
    for i in range(3,int(n**0.5)+1,2):   # only odd numbers
        if n%i==0:
            return False
    return True

# 3797
# 3797, 797, 97, 7
# 3797, 379, 37, 3


def remove_left(n):
    n = str(n)
    for i in range(len(n)-1):
        n = n[1:]
        # print(n)
        if not is_prime(int(n)):
            return False
    return True

def remove_right(n):
    n = str(n)
    for i in range(len(n)-1):
        n = n[:-1]
        # print(n)
        if not is_prime(int(n)):
            return False
    return True


res = 0

for i in range(10, 100000000):
    if is_prime(i) and remove_left(i) and remove_right(i):
        res += i
        print(i, res)
    if i % 100_000 == 0:
        print('>', i)


print(f'----------------------38--')

def pan_number(n):          # Пан-цифровые !!!!!!!!! без нуля
    for i in str(n):
        if i == '0':
            return False
        tmp = 0
        for j in str(n):
            # print(i , j)
            if i == j:
                tmp += 1
                if tmp > 1:
                    return False
    return True

for i in range(1, 100_000_000):
    tmp = ''
    j = 1
    while True:
        # print(tmp + str(i * j))
        if len(tmp + str(i * j)) < 11:
            tmp += str(i * j)
            # print(i, '*', j, '=', i * j, '>',tmp)
            j += 1
            if len(tmp) == 9 and pan_number(tmp):
                print('>', i, tmp)
        else:
            break
    if i % 1_000_000 == 0:
        print('>', i)


print(f'----------------------39--')


import math


# 120
# {20,48,52}, {24,45,51}, {30,40,50}
# P = a + b + c
# c2 = a2 + b2


# print(20 ** 2 + 48 ** 2, 52 ** 2)
# print(24 ** 2 + 45 ** 2, 51 ** 2)
# print(30 ** 2 + 40 ** 2, 50 ** 2)

lim = 1001
# 465 0     winner: 5 for 420

res_max = 0
res_max_data = []

for p in range(1, lim):
    # print(p)
    res = 0
    for c in range(1, p):
        for b in range(1, c):
            # a = 1
            # while a + b + c <= p:
            # for a in range(1, p - c -b):
            for a in range(1, b):
                if a + b + c == p and c ** 2 == a ** 2 + b ** 2:
                    res += 1
                    print('>', p, '=', a,b,c)


    if res > res_max:
        res_max = res
        res_max_data = p

    print('>>', p, int(res), '    winner:', res_max, 'for', res_max_data)

print(res_max, 'for', res_max_data)


# ------

import time
from collections import Counter

# startTime = time.clock()

MAX = 1000

def getB(p, a):
    return (p ** 2 - 2 * p * a) // (2 * p - 2 * a)

triangleSolutions = [(p, a, getB(p, a), p - a - getB(p, a)) for p in range(2, MAX + 1, 2) for a in range(1, p // 3 + 1)  if a ** 2 + getB(p, a) ** 2 == (p - a - getB(p, a)) ** 2]

perimeters = [x[0] for x in triangleSolutions]

maximized = Counter(perimeters).most_common()[0][0]

print("The right-triangle perimeter below {0} with the most solutions is {1}.".format(MAX, maximized))

# print("Program execution took {0} seconds.".format(time.clock() - startTime))


print(f'----------------------40--')

# 0.123456789101112131415161718192021...
#
# Видно, что 12-ая цифра дробной части - 1.

n = 1
tmp = ''

while True:
    tmp += str(n)
    # print(tmp)
    n += 1
    # if len(tmp) > 10:
    if len(tmp) > 1000100:
        print(tmp[1 - 1])
        print(tmp[10 - 1])
        print(tmp[100 - 1])
        print(tmp[1000 - 1])
        print(tmp[10000 - 1])
        print(tmp[100000 - 1])
        print(tmp[1000000 - 1])

        print(int(tmp[1 - 1]) * int(tmp[10 - 1]) * int(tmp[100 - 1]) * int(tmp[1000 - 1]) * int(tmp[10000 - 1]) * int(
            tmp[100000 - 1]) * int(tmp[1000000 - 1]))

        break

# d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000



print(f'----------------------41--')

def is_prime(n):        # простые
    if n==2 or n==3: return True
    if n%2==0 or n<2: return False
    for i in range(3,int(n**0.5)+1,2):   # only odd numbers
        if n%i==0:
            return False
    return True

def pan_number(n):          # Пан-цифровые !!!!!!!!! без нуля
    for i in str(n):
        if i == '0':
            return False
        tmp = 0
        for j in str(n):
            # print(i , j)
            if i == j:
                tmp += 1
                if tmp > 1:
                    return False
    return True


from itertools import permutations      # все возможные перестановки ПЕРЕБОР
a = ('7','6','5','4','3','2','1')
n = 7
rep = 1
for i in permutations(a * rep, n):
    tmp = int(''.join(i))
    # print(tmp)
    if is_prime(tmp) and pan_number(tmp):
        print(tmp)

print(f'----------------------42--')

abc = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
       'W', 'X', 'Y', 'Z']


def triangular_numbers(n):
    print(int(1 / 2 * n * (n + 1)))


tri_numbers = []

for n in range(1, 1000):
    tri_numbers.append(int(1 / 2 * n * (n + 1)))

# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
# SKY равно 19 + 11 + 25 = 55 = t10

# print(abc.index('S')+1)
# print(abc.index('K')+1)
# print(abc.index('Y')+1)

# triangular_numbers(4)

f = open("p042_words.txt", "r")
for line in f:
    st = line
f.close()

arr = st.split(',')

print(arr)

res = 0

for i in arr:
    tmp = 0
    # print(i, '', end='')
    for j in i:
        tmp += (abc.index(j) + 1)
        # print((abc.index(j) + 1), '', end='')
    # print('>',tmp)
    if tmp in tri_numbers:
        print(i, tmp)
        res += 1

print('>>>', res)

print(f'----------------------43--')



def pan_number(n):          # Пан-цифровые
    for i in str(n):
        tmp = 0
        for j in str(n):
            # print(i , j)
            if i == j:
                tmp += 1
                if tmp > 1:
                    return False
    return True


def parts_divider(n):
    n = str(n)

    # print(n[1:4])
    # print(n[2:5])
    # print(n[3:6])
    # print(n[4:7])
    # print(n[5:8])
    # print(n[6:9])
    # print(n[7:10])

    if int(n[1:4]) % 2 ==0 \
    and int(n[2:5]) % 3 ==0 \
    and int(n[3:6]) % 5 ==0 \
    and int(n[4:7]) % 7 ==0 \
    and int(n[5:8]) % 11 ==0 \
    and int(n[6:9]) % 13 ==0 \
    and int(n[7:10]) % 17 ==0:
        return True
    else:
        return False

res = 0

from itertools import permutations      # все возможные перестановки ПЕРЕБОР
a = ('0','1','2','3','4','5','6','7','8','9')
n = 10
rep = 1
for i in permutations(a * rep, n):
    tmp = int(''.join(i))
    # print(tmp)
    if parts_divider(tmp):
        print(tmp)
        res += tmp


print('>', res)

# print(parts_divider(1406357289))
# print(parts_divider(140634589))
# print(parts_divider(1345357289))

# 1406357289

# d2d3d4=406 делится на 2 без остатка
# d3d4d5=063 делится на 3 без остатка
# d4d5d6=635 делится на 5 без остатка
# d5d6d7=357 делится на 7 без остатка
# d6d7d8=572 делится на 11 без остатка
# d7d8d9=728 делится на 13 без остатка
# d8d9d10=289 делится на 17 без остатка

print(f'----------------------44--')

max_step = 10000

pen = []

for i in range(1, max_step):
    # print( int(i * (3 * i - 1) / 2) )
    pen.append(int(i * (3 * i - 1) / 2))

print(pen)

# pen = dict(pen)
# print(pen)

# n(3n−1)/2
# 1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...


# P4 + P7 = 22 + 70 = 92 = P8

res = []

for i in range(int(max_step / 2)):
    print(i)
    for j in range(i):

        # print(i, j, '|', pen[i], pen[j])

        # if pen[i] + pen[j] in pen:
        #     print(i, j, '---',

        # res.append([pen[i], '-', pen[j], '=',
        #             pen[i] - pen[j])

        if pen[i] + pen[j] in pen and pen[i] - pen[j] in pen:
            print(i, j, '---', pen[i], pen[j])
            res.append([pen[i], pen[j]])

print(res)

# 2166 1019 --- 7042750 1560090

print(f'----------------------45--')


t = []
p = []
h = []


def make_t(max):
    for n in range(max):
        t.append(int(n * (n + 1) / 2))


def make_p(max):
    for n in range(max):
        p.append(int(n * (3 * n - 1) / 2))

def make_h(max):
    for n in range(max):
        h.append(n * (2 * n - 1))

#                   Tn=n(n+1)/2	 	1, 3, 6, 10, 15, ...
# Пятиугольные	 	Pn=n(3n−1)/2	1, 5, 12, 22, 35, ...
# Шестиугольные	 	Hn=n(2n−1)	 	1, 6, 15, 28, 45, .


n = 100_000

make_t(n)
make_p(n)
make_h(n)

# print(t)
# print(p)
# print(h)

# T285 = P165 = H143 = 40755.

# print(t[285])
# print(p[165])
# print(h[143])

print(len(t))
print(len(p))
print(len(h))

# for i in range(n):
#     if t[i] in p and t[i] in h:
#         print('>>', i)
#     if i % 10_000 == 0:
#         print(i)

# > 55385

print(t[55385])

print(f'----------------------46--')


def is_prime(n):        # простые
    if n==2 or n==3: return True
    if n%2==0 or n<2: return False
    for i in range(3,int(n**0.5)+1,2):   # only odd numbers
        if n%i==0:
            return False
    return True


print()


double_square = []

for i in range(1, 100000):
    # print(i, 2 * (i ** 2))
    double_square.append(2 * (i ** 2))
# 99 > 19602


# 9 = 7 + 2×12
# 15 = 7 + 2×22
# 21 = 3 + 2×32
# 25 = 7 + 2×32
# 27 = 19 + 2×22
# 33 = 31 + 2×12


def goldbach(n):
    for i in range(n):
        if is_prime(n - double_square[i]):
            return True
    return False


print()

for i in range(3, 10000000, 2):   # нечетное составное
    if not is_prime(i):
        print(i)
        if not goldbach(i):
            print('>>', i)
            quit()



print(f'----------------------47--')



def prime_factors(n):  # ДЕЛИТЕЛИ без повторов со степенями
    """Разложить число на множители"""
    # result = [1]
    factors = []
    res = []
    i = 2
    while i < n:
        if n % i == 0:
            n /= i
            factors.append(i)
        else:
            i += 1
    factors.append(int(n))

    # print(factors)

    tmparr = []
    for i in factors:
        if i not in tmparr:
            if factors.count(i) > 1:
                # tmps =
                res.append(str(i) + '**' + str(factors.count(i)))
                tmparr.append(i)
            else:
                res.append(i)
                tmparr.append(i)

    # print(res)

    return res

# prime_factors(500)


# 14 = 2 × 7
# 15 = 3 × 5

import numpy

n1=0
n2=0
n3=0
n4=0

n1_mn = 0
n2_mn = 0
n3_mn = 0
n4_mn = 0

for i in range(1_000_000):
    # print(i, len(prime_factors(i)))
    if i % 10000 == 0:
        print(i)

    if len(prime_factors(i)) == 4 and len(prime_factors(i+1)) == 4 and len(prime_factors(i+2)) == 4 and len(prime_factors(i+3)) == 4:

    # n1_mn, n2_mn, n3_mn, n4_mn = n2_mn, n3_mn, n4_mn, len(prime_factors(i))
    # if n4_mn == 4 and n3_mn == 4 and n2_mn == 4 and n1_mn == 4:

        # if not numpy.array_equal(prime_factors(i), prime_factors(i + 1)) \
        #         and not numpy.array_equal(prime_factors(i), prime_factors(i + 2)) \
        #         and not numpy.array_equal(prime_factors(i), prime_factors(i + 3)):

        print(i, prime_factors(i))
        print(i + 1, prime_factors(i + 1))
        print(i + 2, prime_factors(i + 2))
        print(i + 3, prime_factors(i + 3))
        print()



print(f'----------------------48--')

n = 0

for i in range(1, 1001):
    n += i ** i


print(str(n)[-10:])


print(f'----------------------49--')


def is_prime(n):        # простые
    if n== 2 or n == 3: return True
    if n % 2 == 0 or n < 2: return False
    for i in range(3, int(n ** 0.5) + 1, 2):  # only odd numbers
        if n % i == 0:
            return False
    return True


def same_characters(n1, n2):
    for i in str(n1):
        if i not in str(n2):
            return False
    return True

# 1487, 4817, 8147

for i in range(1000, 10000):
    if is_prime(i) and is_prime(i + 3330) and is_prime(i + 6660):
        # print(i, i + 3330, i + 6660)
        if same_characters(i, i + 3330) and same_characters(i, i + 6660):
            print(i, i + 3330, i + 6660)

# 296962999629

print(f'----------------------50--')



def is_prime(n):        # простые
    if n== 2 or n == 3: return True
    if n % 2 == 0 or n < 2: return False
    for i in range(3, int(n ** 0.5) + 1, 2):  # only odd numbers
        if n % i == 0:
            return False
    return True

prime = []

# max_wrk = 1_00
max_wrk = 1_000_100

for i in range(max_wrk):
    if is_prime(i):
        prime.append(i)

print(prime)

# 41 = 2 + 3 + 5 + 7 + 11 + 13
# 953 = x + x + x +  (21 слаг)
# < 1_000_000

# print(prime.index(953))
# print(prime[12])
# print(prime[0])
print()


i = 0


super_max = 0
super_max_res = 0

for start_i in range(max_wrk):
    print()
    print('>', start_i)
    res = 0
    i = start_i

    max_start_i = 0
    max_res = 0

    while res <= max_wrk:
        if is_prime(res):
            max_res = res
            max_start_i = start_i
        # print(i, prime[i], res, is_prime(res))
        res += prime[i]
        i += 1
        # print(i, prime[i], res, is_prime(res))

    res = 0

    while res < max_res:
        print(prime[max_start_i], '', end='')

        max_start_i += 1
        res += prime[max_start_i]

    print('=', max_res, '  posled iz -', max_start_i - start_i, 'super: ', super_max, 'dlya:', super_max_res)
    if super_max < max_start_i - start_i:
        super_max = max_start_i - start_i
        super_max_res = max_res

# 41 = 2 + 3 + 5 + 7 + 11 + 13

# > 0
# 0 2 0 False
# 1 3 2 True
# 2 5 5 True
# 3 7 10 False
# 4 11 17 True
# 5 13 28 False
# 6 17 41 True
# 7 19 58 False
# 8 23 77 False
# 9 29 100 False
# 10 31 129 False

