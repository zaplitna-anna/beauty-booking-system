class BookingService:
    @staticmethod
    def get_available_slots(service, date):
        raise NotImplementedError(
            "Пошук вільного часу ще не реалізовано."
        )

    @staticmethod
    def is_slot_available(service, start_at):
        raise NotImplementedError(
            "Перевірку доступності часу ще не реалізовано."
        )

    @staticmethod
    def create_booking(client, service, start_at):
        raise NotImplementedError(
            "Створення бронювання ще не реалізовано."
        )

    @staticmethod
    def cancel_booking(booking_id):
        raise NotImplementedError(
            "Скасування бронювання ще не реалізовано."
        )
