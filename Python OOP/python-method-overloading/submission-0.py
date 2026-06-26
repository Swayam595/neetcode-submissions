class TextProcessor:
    # Implement method overloading for format_text method
    def format_text(self, *args: str) -> str:
        if len(args) == 1:
            return args[0].upper()
        else:
            return "".join(args)



# Don't modify the code below
processor = TextProcessor()
print(processor.format_text("hello"))
print(processor.format_text("hello", "world"))
