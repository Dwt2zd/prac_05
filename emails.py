def main():
    dicti={}
    wholem=input("Email: ")
    email=wholem.split('@')
    while email != [""]:
        no_name=' '.join((str(email[0]).title()).split("."))
        unk_name=str(input(f"Is your name {no_name}? (y/n)")).lower()
        if unk_name == "n":
            yes_name=input("Name:")
            dicti[yes_name] = ''.join(email)
            dicti[yes_name] = '@'.join(email)
        elif unk_name == '' or unk_name == 'y':
            dicti[no_name] = ''.join(email)
            dicti[no_name] = '@'.join(email)
        email= input("Email: ").split("@")
    for name, address in dicti.items():
        print(f"{name} ({address})")
main()