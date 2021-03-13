
def fizz_buzz(x: int) -> str:
    # Determine if 'x' is a multiple of 3, 5 and 7
    m3 = x % 3 == 0
    m5 = x % 5 == 0
    m7 = x % 7 == 0

    if m3 and m5 and m7: return 'Devhaus Learning Model'
    if m3 and m7: return 'Devhaus Model'
    if m3 and m5: return 'Devhaus Learning'
    if m3: return 'Devhaus'
    if m5: return 'Learning'
    if m7: return 'Model'

    return str(x)

def main():
    # Print fizz-buzz for 1-105
    for i in range(1, 106):
        print(fizz_buzz(i))

if __name__ == '__main__':
    main()