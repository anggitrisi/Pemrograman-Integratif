while True:
  try:
    num = float(input("Enter a num: "))
    if num >= 0 or num < 0:
        if num >= 0:
            if num == 0:
                print("Zero")
            else:
                print("Positive number")
        else:
            print("Negative number")
        break
    print("Invalid num entered, must number")
  except Exception as e:
    print("Invalid num entered, must number")

