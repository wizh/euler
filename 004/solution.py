# Don't worry, I now switched to 2.7
print(max(i * j for i in range(900, 1000)
                for j in range(900, 1000) if str(i*j) == str(i*j)[::-1]))
