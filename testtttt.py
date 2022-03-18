from multiprocessing import Pool
import time

def f(x):
    print(x*x)

if __name__ == '__main__':
    with Pool(processes=4) as p:
        start_1 = time.time() # 開始測量執行時間
        # print(f(10))

    #     # 設定 chunksize 為 1
    #     p.map(f, range(1000000), chunksize=1)
    #
        end_1 = time.time() # 結束測量執行時間
    #
    #
        start = time.time() # 開始測量執行時間
    #
    #     # 設定 chunksize 為 1000
        p.map(f, range(10000000), chunksize=1000)
    #
        end = time.time() # 結束測量執行時間
        print("chunksize 為 1，執行時間為 %f 秒" % (end_1 - start_1))
        print("chunksize 為 1000，執行時間為 %f 秒" % (end - start))
    #
    #     if result1 == result2:
    #         print("結果相同")