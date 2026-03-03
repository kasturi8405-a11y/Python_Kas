
Companyname = "Tech Solutions"
Bussiness = "Software Development"

print(Companyname[0])
print(Companyname[-1])
print(Companyname[0:6])
print(Companyname[:6])
print(Companyname[5:])
print(Companyname[:7])

print(len(Bussiness))
print(Bussiness.strip())
print(Bussiness.upper())
print(Bussiness.lower())
print(Bussiness.title())
print(Bussiness.replace("Software", "IT"))

message_1 = f"Welcome to {Companyname}, we specialize in {Bussiness}."
print(message_1)

text = """Python is a powerful programming language. It's easy to learn and versatile!
You can use Python for web development, data science, and automation. The syntax is clean and readable.
This makes Python perfect for beginners and experts alike."""

print(len(text))
print(text.count("Python"))
print(text.count("P"))
print(sentence_count := text.split("."))
print(len(sentence_count))








