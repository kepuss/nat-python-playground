input_list = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400, 410, 420, 430, 440, 450, 460, 470, 480, 490,
              500, 510, 520, 530, 540, 550, 560, 570, 580, 590, 600, 610, 620, 630, 640, 650, 660, 670, 680, 690, 700, 710, 720, 730, 740, 750, 760, 770, 780, 790, 800, 810, 820, 830, 840, 850, 860, 870, 880, 890, 900, 910, 920, 930, 940, 950, 960, 970, 980, 990]


def check_if_list_elements_differ_by_10(input):
    for item in range(len(input)-1):
        if input[item] is None or input[item+1] is None:
            raise ValueError("One of the elements is an empty value!")
        if type(input[item]) is list or type(input[item+1]) is list:
            raise TypeError("One of the elements is a nested array!")
        if type(input[item]) is not int or type(input[item+1]) is not int:
            raise TypeError("One of the elements is not an integer!")
        if input[item+1] - input[item] != 10:
            return False
    return True


try:
    print(check_if_list_elements_differ_by_10(input_list))
except Exception as e:
    print("An error has occurred.", e)
