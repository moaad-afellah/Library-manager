def printFactute1(list):
    print("======   Bonjour chez Souss Hanout   =======")

    """
    1   article1    12  450
    2   article2    14  1520

    Total to pay: 4785
    """
    print("id" + "\t"
          + "product" + "\t"
          + "quantity" + "\t"
          + "price" + "\t"
          + "totality" + "\t"
          )
    for item in list:
        print(str(item["id"]) + "\t"
              + item["product"] + "\t"
              + str(item["quantity"]) + "\t\t"
              + str(item["price"]) + "\t\t"
              + str(item["totality"]) + "\t\t"
              )
    print("======   Merci pour votre visite   =======")

def llll():
    print('llll')