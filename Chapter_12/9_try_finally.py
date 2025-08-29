def main():
    try:
        a = int(input("Enter a no.: "))
        print(a)
        return

    except Exception as e:
        print(e)
        return

    finally:
        print("I'm inside finally")

main()