"""Fliter"""
import json
def main():
    """Filter"""
    dictscore = json.loads(input())
    socre = float(input())
    ans = []
    for i in dictscore:
        if dictscore[i] >= socre:
            ans.append(i)
    if not ans:
        print("Nope")
    else:
        for i in sorted(ans):
            print(f"{i}\t{dictscore[i]:.2f}")
main()
