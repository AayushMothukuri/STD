import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)


        f = open(file_from, 'rb')
        dbx.files_upload(f.read(), file_to)

def main():
    access_token='sl.A1ypgJ3OYY5swQy29a0tbiIB6Cwm_oAOIhQc4uN15gGzkYAaK7vjoxINSbkMlkD2DPT4LWyXVA4tY5Dc-ruPxX3Fns2m0Yzz8GiI_7lUSioT6jsxRDLgDpW8ExltO1gzqjOOPxM'
    transferData = TransferData(access_token)

    file_from = input("Enter the file path to transfer : -")
    file_to = input("enter the full path to upload to dropbox:- ")  # This is the full path to upload the file to, including name that you wish the file to be called once uploaded.

    # API v2
    transferData.upload_file(file_from, file_to)
    print("file has been moved !!!")


main()
   
   
    

        