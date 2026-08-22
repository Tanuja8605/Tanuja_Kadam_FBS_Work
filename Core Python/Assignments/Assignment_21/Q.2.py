from userdefineExcept import TelevisionException

class Television:

    def __init__(self, model_no=0, screen_size=0, price=0):
        self.model_no = model_no
        self.screen_size = screen_size
        self.price = price

    def get_model_no(self):
        if len(str(self.model_no)) > 4:
            raise ValueError("Model number should not have more than 4 digits")
        return self.model_no

    def get_screen_size(self):
        if self.screen_size < 12 or self.screen_size > 70:
            raise TelevisionException("Screen size should be between 12 and 70 inches")
        return self.screen_size

    def get_price(self):
        if self.price < 0 or self.price > 5000:
            raise TelevisionException("Price should be between 0 and 5000")
        return self.price

    def display(self):
        self.get_model_no()
        self.get_screen_size()
        self.get_price()

        print("Model Number:", self.model_no)
        print("Screen Size:", self.screen_size)
        print("Price:", self.price)


try:
    t1 = Television(2349, 50, 3000)

    t2 = Television(23,45,2500)

    t1.display()

    print("--------------------------")

    t2.display()

except Exception as e:
    print("Error:", e)

    t1.model_no = 0
    t1.screen_size = 0
    t1.price = 0



    t2.model_no = 0
    t2.screen_size = 0
    t2.price = 0

    print("Data replaced with zero")

finally:
    print("Order Done...")
