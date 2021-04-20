def main():
    Dict={}
    text = input("Text: ").split()
    for words in text:
        if words not in Dict:
            Dict[words]=1
        else:
            Dict[words]+=1
        max_length= max(len(i) for i in Dict)
    for short, full in sorted(Dict.items()):
        print(f"{short:<{max_length}}: {full}")
main()

