print("""
Marvel Movie Character Creator
========================================

Hey there!
I am going to ask you a serries of questions to find out which marvel character you are.
Let's begin
""")
print()
hangingAround = input("Do you like 'hanging around'?: ")
if hangingAround == 'yes':
    print('You are spiderman')
else: 
    print('Then you are not Spider-man')
gravelly = input('Do you have a gravelly voice?: ')
if gravelly == 'yes':
    print('Then you are Korg')
else:
    print('Aww, then you are not Korg')
marvelous = input('Do you often feel Marvelous?: ')
if marvelous == 'yes':
    print('Aha! You are Captain Marvel! Hi!')
else:
    print('i give up')
