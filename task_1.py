import os
import shutil
import argparse

def copy_files_recursive(src_dir, dest_dir):
    try:
        for item in os.listdir(src_dir):
            item_path = os.path.join(src_dir, item)
            if os.path.isdir(item_path):
                copy_files_recursive(item_path, dest_dir)
            elif os.path.isfile(item_path):
                _, ext = os.path.splitext(item)
                ext = ext[1:] if ext else "no_extension" 
                target_folder = os.path.join(dest_dir, ext)
                os.makedirs(target_folder, exist_ok=True)
                try:
                    shutil.copy2(item_path, target_folder)
                    print(f"Копійовано: {item_path} → {target_folder}")
                except Exception as e:
                    print(f"Помилка копіювання {item_path}: {e}")
    except PermissionError as e:
        print(f"Немає доступу до {src_dir}: {e}")
    except FileNotFoundError as e:
        print(f"Файл або директорія не знайдені: {e}")
    except Exception as e:
        print(f"Непередбачена помилка у {src_dir}: {e}")
def main():
    parser = argparse.ArgumentParser(description="Рекурсивне копіювання та сортування файлів за розширенням.")
    parser.add_argument("src", help="Шлях до вихідної директорії")
    parser.add_argument("dest", nargs="?", default="dist", help="Шлях до директорії призначення (за замовчуванням dist)")
    args = parser.parse_args()
    src_dir = os.path.abspath(args.src)
    dest_dir = os.path.abspath(args.dest)
    if not os.path.exists(src_dir):
        print(f"Помилка: директорія {src_dir} не існує.")
        return
    os.makedirs(dest_dir, exist_ok=True)
    copy_files_recursive(src_dir, dest_dir)
    print(f"\n Усі файли скопійовані у {dest_dir}")
if __name__ == "__main__":
    main()
