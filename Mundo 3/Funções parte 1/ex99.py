from time import sleep
def maior(*nums):
    maiorV = 0
    if not nums:
        print('~-='*30)
        print(f'Foram informados ao todo 0 valores')
        print(f'O maior valor informado foi 0')
    else:
        print('~-='*30)
        print('Analisando valores passados...')
        for n in nums:
            print(f'{n} ',end='')
            if n > maiorV:
                maiorV = n
        print(f'Foram informados ao todo {len(nums)} valores')
        print(f'O maior valor informado foi {maiorV}')

maior(2,9,4,7,6,1)
sleep(1)
maior(4,7,0)
sleep(1)
maior()
sleep(1)
maior(5,8,1,9,0,3)
