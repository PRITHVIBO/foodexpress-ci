import zipfile
files = ["cart.py", "orders.py"]
with zipfile.ZipFile("foodexpress.zip", "w") as z:
    for f in files:
        z.write(f)
print("Created foodexpress.zip")