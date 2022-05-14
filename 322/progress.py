from datetime import datetime
DAYS_IN_YEAR = 365

def ontrack_reading(books_goal: int, books_read: int,
                    day_of_year: int = None) -> bool:
    if day_of_year is None:
        day_of_year = datetime.now().timetuple().tm_yday
    days_left_in_year = DAYS_IN_YEAR - day_of_year
    books_left_to_read = books_goal - books_read
    if books_read == 0:
        return False
    else:
        days_to_finish_book = day_of_year / books_read

    days_required_for_goal = days_to_finish_book * books_left_to_read

    return days_left_in_year >= days_required_for_goal
