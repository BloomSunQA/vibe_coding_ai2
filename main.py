import tkinter as tk
import tkinter.messagebox as mb
import tkinter.simpledialog as sd

def is_leap_year(year: int) -> bool:
    """Вернуть True, если год високосный, иначе False."""
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def validate_year_input(value: str | None) -> int:
    """Проверить ввод пользователя и вернуть год как целое число."""
    if value is None:
        raise ValueError("Ввод отменён пользователем.")

    value = value.strip()
    if not value:
        raise ValueError("Ошибка: поле не должно быть пустым.")

    try:
        year = int(value)
    except ValueError:
        raise ValueError("Ошибка: необходимо ввести целое число.")

    if year <= 0 or year > 9999:
        raise ValueError("Год должен быть от 1 до 9999.")

    return year

def main() -> None:
    root = tk.Tk()
    root.withdraw()

    try:
        user_input = sd.askstring("Введите год", "Пожалуйста, введите год для проверки:")
        year = validate_year_input(user_input)

        if is_leap_year(year):
            mb.showinfo("Результат", f"{year} год является високосным.")
        else:
            mb.showinfo("Результат", f"{year} год не является високосным.")
    except ValueError as exc:
        mb.showerror("Ошибка ввода", str(exc))
    except Exception as exc:
        mb.showerror("Ошибка", f"Произошла непредвиденная ошибка: {exc}")
    finally:
        root.destroy()

if __name__ == "__main__":
    main()