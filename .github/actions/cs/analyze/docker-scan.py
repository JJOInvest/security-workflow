import os
import re
import subprocess
import csv

def run_command(command, log_file):
    """Запускает shell-команду, возвращает вывод и пишет логи в файл."""
    try:
        process = subprocess.Popen(
            command, shell=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT
        )
        with open(log_file, "a") as log:
            for line in process.stdout:
                print(line, end="")  # Вывод в консоль
                log.write(line)       # Запись в лог-файл
        process.wait()
        if process.returncode != 0:
            raise subprocess.CalledProcessError(process.returncode, command)
    except subprocess.CalledProcessError as e:
        print(f"Ошибка выполнения команды: {command}\nКод ошибки: {e.returncode}")
        raise
    except Exception as e:
        print(f"Неожиданная ошибка при выполнении команды: {command}\n{e}")
        raise

def parse_images_from_md(file_path):
    """Извлекает Docker-образы из первого столбца файла images.md."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Файл {file_path} не найден.")
    
    images = []
    with open(file_path, 'r') as f:
        reader = csv.reader(f, delimiter='|')
        next(reader)  # Пропустить заголовок
        for row in reader:
            if len(row) > 1:
                image = row[1].strip()
                if image.startswith("docker pull"):
                    images.append(image.replace("docker pull ", "").strip())
    return images

def process_images(images, log_file):
    """Обрабатывает список Docker-образов, продолжая при ошибках."""
    for image in images:
        try:
            # Разделение для нового образа в лог-файле
            with open(log_file, "a") as log:
                log.write("\n")
                log.write("=" * 50 + "\n")
                log.write(f"Начало обработки Docker-образа: {image}\n")
                log.write("=" * 50 + "\n\n")
            
            print(f"\nРабота с образом: {image}")
            
            # Docker pull
            print(f"\nЗагружаем образ: {image}")
            run_command(f"docker pull {image}", log_file)
            
            # Trivy scan
            print(f"\nСканируем образ Trivy: {image}")
            run_command(f"/usr/local/bin/trivy image {image}", log_file)
            
            # Grype scan
            print(f"\nСканируем образ Grype: {image}")
            run_command(f"/usr/local/bin/grype {image}", log_file)

            # Docker rmi
            print(f"\nУдаляем образ: {image}")
            run_command(f"docker rmi {image}", log_file)
            
            # Успешное завершение обработки
            with open(log_file, "a") as log:
                log.write(f"\nУспешно обработан Docker-образ: {image}\n")
                log.write("=" * 50 + "\n\n")

        except Exception as e:
            print(f"Ошибка обработки образа {image}: {e}")
            with open(log_file, "a") as log:
                log.write(f"\nОшибка обработки Docker-образа {image}: {e}\n")
                log.write("=" * 50 + "\n\n")

if __name__ == "__main__":
    # Путь к файлу images.md
    md_file = "images.md"
    log_file = "scan_results.log"

    # Создание или очистка файла логов
    with open(log_file, "w") as log:
        log.write("Логи сканирования Docker-образов\n")
        log.write("=" * 50 + "\n\n")

    # Проверка существования файла images.md
    if not os.path.exists(md_file):
        print(f"Файл {md_file} не найден. Проверьте путь к файлу.")
    else:
        # Извлечение списка образов
        docker_images = parse_images_from_md(md_file)
        print(f"Найдено {len(docker_images)} Docker-образов.")

        # Обработка образов
        try:
            process_images(docker_images, log_file)
            print(f"\nСканирование завершено. Логи сохранены в {log_file}.")
        except Exception as e:
            print(f"Произошла ошибка при обработке образов: {e}")
