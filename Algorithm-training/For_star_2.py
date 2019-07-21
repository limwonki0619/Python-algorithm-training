Height = 41

def star():
    Height = int(input('Height 값은 현재 '33'만 가능합니다.'))
    denominator_1 = 4
    denominator_2 = 5
    
    print(' '*19, '*')  # Part 1
    
    for P_2 in range(Height // denominator_1):  # Part 2, i = 0 ~ 8
        for P_2_blank_1 in range(P_2, 17-P_2):  # i:17-i
            print(' ', end='')
        for P_2_star_1 in range(P_2, P_2+1):    #  i:i+1
            print('*', end='')
        for P_2_blank_2 in range(0, P_2+1):     #  0:i+1
            print(' ', end='')
        for P_2_star_2 in range(0, (P_2*2)+3):  #  0:(i*2)+3
            print('*', end='')
        for P_2_blank_3 in range(0, P_2+1):
            print(' ', end='')
        for P_2_star_3 in range(P_2, P_2+1):
            print('*', end='')
        print()

    for P_3 in range(Height // denominator_2):  # Part_3, i = 0 ~ 6
        for P_3_blank_1 in range(P_3, P_3+1):
            print(' ', end='')
        for P_3_star_1 in range(P_3, P_3+1):
            print('*', end='')
        for P_3_blank_2 in range(0, P_3+1):
            print(' ', end='')
        for P_3_star_2 in range(P_3, 34-P_3): # 수정된 (첫번째)별 갯수 : 34
            print('*', end='')
        for P_3_blank_3 in range(0, P_3+1):
            print(' ', end='')
        for P_3_star_3 in range(P_3, P_3+1):
            print('*', end='')
        print()

    for P_4 in reversed(range(Height // denominator_1)):  # Part_4
        for P_4_blank_1 in range(P_4, P_4 + 1):
            print(' ', end='')
        for P_4_star_1 in range(P_4, P_4 + 1):
            print('*', end='')
        for P_4_blank_2 in range(0, P_4 + 1):
            print(' ', end='')
        for P_4_star_2 in range(P_4, 34 - P_4):
            print('*', end='')
        for P_4_blank_3 in range(0, P_4 + 1):
            print(' ', end='')
        for P_4_star_3 in range(P_4, P_4 + 1):
            print('*', end='')
        print()

    for P_5 in reversed(range(Height // denominator_2)):    # Part_5
        for P_5_blank_1 in range(P_5, 17-P_5):
            print(' ', end='')
        for P_5_star_1 in range(P_5, P_5+1):
            print('*', end='')
        for P_5_blank_2 in range(0, P_5+1):
            print(' ', end='')
        for P_5_star_2 in range(0, (P_5*2)+3):
            print('*', end='')
        for P_5_blank_3 in range(0, P_5+1):
            print(' ', end='')
        for P_5_star_3 in range(P_5, P_5+1):
            print('*', end='')
        print()

    print(' '*19, '*')  # Part 6 == Part 1

star()

