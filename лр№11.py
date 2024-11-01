import csv
from datetime import datetime

def process_population_data(input_file, output_file):
    """
    Функція для обробки даних про населення України
    Args:
        input_file (str): шлях до вхідного файлу
        output_file (str): шлях до вихідного файлу
    """
    try:
        # Читаємо дані з CSV файлу
        with open(input_file, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            
            # Фільтруємо дані для України за 1991-2019 роки
            ukraine_data = []
            for row in reader:
                if row['Country Name'] == 'Ukraine' and \
                   1991 <= int(row['Year']) <= 2019:
                    ukraine_data.append({
                        'Year': int(row['Year']),
                        'Population': int(float(row['Population']))
                    })
            
            # Сортуємо дані за роком
            ukraine_data.sort(key=lambda x: x['Year'])
            
            # Виводимо дані на екран
            print("\nНаселення України за роками:")
            print("Рік\t\tНаселення")
            print("-" * 30)
            for data in ukraine_data:
                print(f"{data['Year']}\t\t{data['Population']:,}")
            
            # Знаходимо мінімальне та максимальне значення
            min_population = min(ukraine_data, key=lambda x: x['Population'])
            max_population = max(ukraine_data, key=lambda x: x['Population'])
            
            # Записуємо результати у новий CSV файл
            with open(output_file, 'w', encoding='utf-8', newline='') as outfile:
                writer = csv.writer(outfile)
                writer.writerow(['Тип', 'Рік', 'Населення'])
                writer.writerow(['Мінімальне значення', 
                               min_population['Year'],
                               min_population['Population']])
                writer.writerow(['Максимальне значення', 
                               max_population['Year'],
                               max_population['Population']])
            
            print(f"\nРезультати записано у файл {output_file}")
            print(f"\nМінімальне населення: {min_population['Population']:,} "\
                  f"(рік: {min_population['Year']})")
            print(f"Максимальне населення: {max_population['Population']:,} "\
                  f"(рік: {max_population['Year']})")
            
    except FileNotFoundError:
        print(f"Помилка: Файл {input_file} не знайдено")
    except PermissionError:
        print(f"Помилка: Немає дозволу на доступ до файлу {input_file}")
    except csv.Error as e:
        print(f"Помилка при обробці CSV файлу: {e}")
    except Exception as e:
        print(f"Виникла непередбачена помилка: {e}")

def main():
    input_file = 'population_data.csv'  # Назва вхідного файлу
    output_file = 'ukraine_population_analysis.csv'  # Назва вихідного файлу
    
    # Створюємо тестові дані, якщо файл не існує
    try:
        with open(input_file, 'r') as file:
            pass
    except FileNotFoundError:
        # Створюємо тестовий CSV файл
        with open(input_file, 'w', encoding='utf-8', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Country Name', 'Year', 'Population'])
            # Додаємо тестові дані для України
            population = 52000000  # Початкове значення
            for year in range(1991, 2020):
                # Моделюємо зміну населення
                population = population - (year - 1991) * 100000
                writer.writerow(['Ukraine', year, population])
        print(f"Створено тестовий файл {input_file}")
    
    # Обробляємо дані
    process_population_data(input_file, output_file)

if __name__ == "__main__":
    main()