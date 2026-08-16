learning_rate = 0.01
batch_size = 64
epochs = 100
dropout = 0.5


if 0 <= learning_rate <= 1:
    print("learning_rate: OK")
else:
    print("learning_rate: błąd — wartość musi być w zakresie od 0 do 1")

if batch_size > 0 and (batch_size & (batch_size - 1)) == 0:
    print("batch_size: OK")
else:
    print("batch_size: błąd — wartość musi być dodatnią potęgą liczby 2")

if 0 < epochs < 1000:
    print("epochs: OK")
else:
    print("epochs: błąd — wartość musi być większa od 0 i mniejsza od 1000")

if 0 <= dropout <= 1:
    print("dropout: OK")
else:
    print("dropout: błąd — wartość musi być w zakresie od 0 do 1")
