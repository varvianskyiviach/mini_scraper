import ftplib


class FTPManager:
    def __init__(self, ftp_host, ftp_username, ftp_password) -> None:
        self.ftp_host = ftp_host
        self.ftp_username = ftp_username
        self.ftp_password = ftp_password
        self.ftp: ftplib.FTP = None

    def __enter__(self) -> 'FTPManager':
        try:
            self.ftp = ftplib.FTP(self.ftp_host)
            self.ftp.login(self.ftp_username, self.ftp_password)

        except ftplib.all_errors as e:
            print(f"Connection to FTP server {self.ftp_host} is failed: {str(e)}")

        return self

    def __exit__(self, exc_type, exc_value, traceback) -> None:
        self.ftp.quit()
