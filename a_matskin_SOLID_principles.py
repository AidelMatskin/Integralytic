import os

class ProcessFile:
    def read_file(self, file_path):
        try:
            file = open(file_path, "r")
            data = file.read()
            file.close()
            return data
        except FileNotFoundError: 
            return None

    def write_file(self, file_path, data):
        try:
            file = open(file_path, "w")
            file.write(data)
            file.close()
        except IOError:
            pass

    def delete_file(self, file_path):
        try:
            os.remove(file_path)
        except FileNotFoundError:
            pass


class GetProductInfo:
    def __init__(self, process_file):
        self.process_file = process_file

    def get_product_info(self, product_id):
        file_path = f"products/{product_id}.txt"
        return self.process_file.read_file(file_path)


class ProcessProductInfo:
    def __init__(self, process_file):
        self.process_file = process_file

    def save_product_info(self, product_id, data):
        file_path = f"products/{product_id}.txt"
        self.process_file.write_file(file_path, data)

    def delete_product_info(self, product_id):
        file_path = f"products/{product_id}.txt"
        self.process_file.delete_file(file_path)


# Example usage
product_id = "P12345"

process_file = ProcessFile()

retrieve_info = GetProductInfo(process_file)
product_info = retrieve_info.get_product_info(product_id)
print("Product information:", product_info)

using_info = ProcessProductInfo(process_file)
new_data = "This is some updated product information."
using_info.save_product_info(product_id, new_data)

using_info.delete_product_info(product_id)
print("Product information deleted.")

# I tried to make changes that would meet the requirements. It seems to
# me that the code is much longer and more complicated, but that was necessary 
# to make sure that I was following the solid guidelines.  
# I had to add a lot in order to comply with the OCP (open for modification, closed for extension))
#