import os
import sys
import pathlib
from docx2pdf import convert
 
def validate_input(input_folder_path,output_folder_path):
     """Input Validation"""
     err_msg=None
     input_dir = os.path.dirname(input_folder_path)
     output_dir = os.path.dirname(output_folder_path)
     if not os.path.isdir(input_dir):
        err_msg="Please check the input file path"
     elif not os.path.isdir(output_dir):
        err_msg="Please check the output file path"
     elif not os.path.exists(input_folder_path):
         err_msg = "File is not available in source path!!"
     if err_msg is not None:
        display_response(1,err_msg)
 
def bulk_convert_word_pdf(input_folder_path,output_folder_path):
    # Bulk Conversion
    try:
        # Converting docx specifying both the input# and output folder
        convert(input_folder_path,output_folder_path)
        result="Successfully converted all Word(.docx) files in the mentioned folder to PDF files in the mentioned output folder"
        display_response(0,result)
    except Exception as exception:
        status="Error while converting:"+ (str(exception))
        display_response(2,status)
    
def display_response(resp_code,resp_msg):
    """Return the response message along with response code."""
    if resp_code == 0:
        sys.stdout.write(resp_msg + '\n')
        sys.exit(0)
    else:
        sys.stderr.write(resp_msg + '\n')
        sys.exit(1)
    
def main_function(args):
    """Main Function"""
    input_folder_path=None
    output_folder_path=None
    try:
        data_arg={}
        for arg in args:
            if "=" in arg:
                arg_s=arg.split('=')
                key_name=arg_s[0].upper()
                data_arg.update({key_name: arg_s[1]})
        input_folder_path=data_arg.get("INPUT_FOLDER_PATH")
        output_folder_path=data_arg.get("OUTPUT_FOLDER_PATH")
        validate_input(input_folder_path,output_folder_path)
        bulk_convert_word_pdf(input_folder_path,output_folder_path)
    except ValueError as error:
        msg="Exception: " + str(error) + "Usage " + sys.argv[0] + "INPUT_FOLDER_PATH=<Str>"* "\
        OUTPUT_FOLDER_PATH=<Str>*"
        display_response(2,str(msg))

if __name__ =='__main__':
    MSG=None
    if len(sys.argv) != 3:
        MSG="One or more required parameters is Null. " \
              "Usage " + sys.argv[0] + " INPUT_FOLDER_PATH=<Str>* OUTPUT_FOLDER_PATH=<Str>* "
        display_response(1,MSG)
    else:
        main_function(sys.argv)
