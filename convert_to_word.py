import os
import subprocess

def convert_to_word():
    input_file = 'reports/Colorado_Car_Sales_Analysis_Report.md'
    output_file = 'reports/Colorado_Car_Sales_Analysis_Report.docx'
    
    # Command to convert markdown to Word using pandoc
    cmd = f'pandoc "{input_file}" -o "{output_file}" --from markdown --to docx'
    
    try:
        subprocess.run(cmd, shell=True, check=True)
        print(f"Successfully converted {input_file} to {output_file}")
    except subprocess.CalledProcessError as e:
        print(f"Error converting file: {e}")
        print("Please make sure pandoc is installed (https://pandoc.org/installing.html)")

if __name__ == "__main__":
    convert_to_word() 