def main():
    reg = str(input("Enter the license plate number: "))
    print("Car from Kraków:", reg_check(reg))
def reg_check(reg):
    if "KR" in reg or "KK" in reg:
        return True
    else:
        return False
main()