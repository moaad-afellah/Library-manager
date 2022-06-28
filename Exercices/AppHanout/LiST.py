listt = [["moaad", "afellah", "1992", 123], ["hasan", "hmad", 1, 55], ["saaad", "brahim", "mohamed", "uyt"],
        {"moaad": 122}]
for element in listt:
        #print(element)
        if type(element) is list:
            for el in element:
                print(el)