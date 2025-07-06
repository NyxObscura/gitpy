import os
import git
from datetime import datetime, timedelta

def create_fake_commits(repo_path, start_date_str, end_date_str, commit_message="Fake commit for contribution"):
    """
    Membuat fake commit pada rentang tanggal tertentu di repositori Git.

    Args:
        repo_path (str): Path ke repositori Git lokal Anda.
        start_date_str (str): Tanggal mulai dalam format 'YYYY-MM-DD'.
        end_date_str (str): Tanggal akhir dalam format 'YYYY-MM-DD'.
        commit_message (str): Pesan commit yang akan digunakan.
    """
    try:
        repo = git.Repo(repo_path)
    except git.InvalidGitRepositoryError:
        print(f"Error: '{repo_path}' bukan repositori Git yang valid.")
        return

    start_date = datetime.strptime(start_date_str, '%Y-%m-%d')
    end_date = datetime.strptime(end_date_str, '%Y-%m-%d')

    current_date = start_date
    while current_date <= end_date:
        # Menulis perubahan kecil ke file (misalnya, README.md)
        # Anda bisa memodifikasi file lain atau membuat file baru
        file_to_modify = os.path.join(repo_path, "README.md")
        with open(file_to_modify, "a") as f:
            f.write(f"\nFake commit on {current_date.strftime('%Y-%m-%d %H:%M:%S')}")

        # Menambahkan file ke staging area
        repo.index.add([file_to_modify])

        # Mengatur variabel lingkungan untuk tanggal commit
        os.environ['GIT_AUTHOR_DATE'] = current_date.strftime('%Y-%m-%d %H:%M:%S +0700') # +0700 untuk WIB
        os.environ['GIT_COMMITTER_DATE'] = current_date.strftime('%Y-%m-%d %H:%M:%S +0700')

        # Melakukan commit
        repo.index.commit(commit_message)
        print(f"Committed on: {current_date.strftime('%Y-%m-%d')}")

        # Menghapus variabel lingkungan setelah commit
        del os.environ['GIT_AUTHOR_DATE']
        del os.environ['GIT_COMMITTER_DATE']

        # Maju ke hari berikutnya
        current_date += timedelta(days=1)

    print("\nProses fake commit selesai.")
    print("Jangan lupa untuk melakukan 'git push' setelah ini.")

if __name__ == "__main__":
    # Ganti dengan path ke repositori lokal Anda
    # Pastikan Anda sudah mengkloning repositori GitHub yang ingin Anda "hijaukan"
    REPOSITORY_PATH = "/path/to/your/local/repo" # <--- GANTI INI

    # Ganti dengan tanggal mulai akun GitHub Anda dibuat atau tanggal awal yang Anda inginkan
    # hingga tanggal saat ini
    START_DATE = "2023-01-01" # <--- GANTI INI
    END_DATE = "2023-12-31"   # <--- GANTI INI (sesuaikan dengan rentang yang Anda inginkan)

    # Contoh untuk membuat commit setiap hari dalam rentang tertentu
    create_fake_commits(REPOSITORY_PATH, START_DATE, END_DATE)

    # Jika Anda ingin mengisi tahun 2023 secara penuh seperti contoh Anda,
    # Anda bisa memanggil fungsi ini dengan rentang tanggal yang diinginkan.
    # Misalnya, untuk setiap hari di tahun 2023:
    # create_fake_commits(REPOSITORY_PATH, "2023-01-01", "2023-12-31")

    # Anda juga bisa membuat loop untuk mengisi beberapa tahun:
    # for year in range(2023, datetime.now().year + 1):
    #     start = f"{year}-01-01"
    #     end = f"{year}-12-31" if year < datetime.now().year else datetime.now().strftime('%Y-%m-%d')
    #     create_fake_commits(REPOSITORY_PATH, start, end)
