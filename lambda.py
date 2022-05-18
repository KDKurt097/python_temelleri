#def square(num): return num ** 2
#square = lambda num: num ** 2 # bu şekilde de yapılabilir hatta bu şekilde square fonksiyon görevi görür
numbers = [1,3,4,5,9] 

squareNumber =list(map(lambda num: num ** 2, numbers)) # fonksiyon yerine tek kullanımlık lambda kullanabilirsiniz
#squareNumber =list(map(square, numbers)) # mao metodu bi l
# yerine alltaki de kullanılabilir
# for item in map(square, numbers):
#    print(item)

print(squareNumber)
