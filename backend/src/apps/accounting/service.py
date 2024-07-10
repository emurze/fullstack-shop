from dataclasses import dataclass


@dataclass(frozen=True)
class CalculateSalaryCommand:
    pass


class AccountingService:
    def calculate_salary(self):
        pass
