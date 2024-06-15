for value in collection:
    smth()
programmAfterCycle()

for i in range(3):
    print(i)
print("End")

for value in [1, 2, 3, 4, 5]:
    print(value)

for value in (1, 2, 3, 4, 5):
    print(value)

for value in {1, 2, 3, 4, 5}:
    print(value)

range(start, stop, step)  # start - start; stop - end (not include); step - step(default: 1)

for _ in range(5):
    print("Hello")

for tuple_ in enumerate(["a", "b", "c"]):
    print(tuple_)

for pos, value in enumerate("abc", start=1):
    print(pos, value)

while condition:
    smth()
programAfterCycle()

while condition:
    startCommand()
    command()
    command()
    break  # => end()
    command()
    continue  # => startCommand()
end()

while True:
    smth()  # Endless cycle