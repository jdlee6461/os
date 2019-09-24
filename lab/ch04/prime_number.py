from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
import sys


def verify_prime_number(n):
    for i in range(2, int(n/2)+1):
        if n % i == 0:
            return
    return n

if __name__=="__main__":
    target_num = int(sys.argv[1])
    results = []
    values = [i for i in range(target_num, target_num+100)]

    # for v in values:
    #     results.append(verify_prime_number(v))

    # with ThreadPoolExecutor(max_workers = 4) as executor:
    #     results = list(executor.map(verify_prime_number, values))

    with ProcessPoolExecutor(max_workers = 4) as executor:
        results = list(executor.map(verify_prime_number, values))

    for r in results:
        if r:
            print(r)