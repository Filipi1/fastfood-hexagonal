from datetime import datetime, timedelta, UTC
from typing import Optional


class DateHelper:
    @staticmethod
    def create_expiration_date(expiration_delta: Optional[timedelta] = None):
        """
        Cria uma data de expiração com base na data e hora atuais, adicionando um delta de tempo opcional.
        Por padrão, a data de expiração é 5 minutos a partir da data e hora atuais.

        Args:
            expiration_delta: timedelta opcional que representa o tempo a ser adicionado à data e hora atuais.

        """
        return datetime.now(UTC) + (expiration_delta or timedelta(minutes=5))

    @staticmethod
    def difference_in_seconds(
        subject_date: datetime, reference_date: Optional[datetime] = None
    ):
        return (subject_date - (reference_date or datetime.now(UTC))).total_seconds()
