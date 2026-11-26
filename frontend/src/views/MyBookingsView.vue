<script setup>
import BookingCard from '../components/BookingCard.vue'

const bookings = [
    {
        id: 1,
        serviceName: 'Манікюр',
        date: '26.11.2026',
        startTime: '11:00',
        endTime: '12:00',
        status: 'CONFIRMED',
    },
    {
        id: 2,
        serviceName: 'Оформлення брів',
        date: '13.11.2026',
        startTime: '16:00',
        endTime: '16:45',
        status: 'CANCELLED',
    },
]
</script>

<template>
    <div class="my-bookings-page">
        <section class="bookings-hero">
            <div class="page-container">
                <h1>ОСОБИСТИЙ КАБІНЕТ</h1>
                <p>
                    Переглядай інформацію про свої візити.
                </p>
            </div>
        </section>

        <section class="bookings-section">
            <div class="page-container">

                <div class="section-heading">
                    <div>
                        <h2>Історія записів</h2>
                    </div>

                    <span class="booking-count">
                        Усього записів: {{ bookings.length }}
                    </span>
                </div>

                <p class="demo-message">
                    <i class="fa-solid fa-circle-info"></i>
                    Це приклади записів для демонстрації інтерфейсу.
                    Справжні бронювання з'являться після
                    підключення до сервера.
                </p>

                <div v-if="bookings.length" class="bookings-grid">
                    <BookingCard v-for="booking in bookings" :key="booking.id" :booking="booking" />
                </div>

                <div v-else class="empty-state">
                    <div class="empty-icon">
                        <i class="fa-regular fa-calendar"></i>
                    </div>

                    <h3>Записів поки немає</h3>
                    <p>
                        Обери процедуру та заплануй
                        свій перший візит.
                    </p>
                    <RouterLink to="/services" class="primary-button">
                        Переглянути послуги
                    </RouterLink>
                </div>

                <div v-if="bookings.length" class="new-booking-area">
                    <RouterLink to="/services" class="primary-button">
                        <i class="fa-solid fa-plus"></i>
                        Новий запис
                    </RouterLink>
                </div>

            </div>
        </section>
    </div>
</template>

<style scoped>
.my-bookings-page {
    color: #460233;
}

.page-container {
    width: 100%;
    max-width: 1180px;
    margin: 0 auto;
    padding: 0 20px;
}

.bookings-hero {
    padding: 75px 0;
    background: linear-gradient(135deg,
            #fefafe 0%,
            #f9e9f4 100%);
    text-align: center;
}

.section-label {
    color: #b33791;
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 2px;
}

.bookings-hero h1 {
    margin: 18px 0;
    color: #460233;
    font-family: Georgia, serif;
    font-size: clamp(36px, 5vw, 52px);
}

.bookings-hero p {
    max-width: 600px;
    margin: 0 auto;
    color: #76556c;
    font-size: 16px;
    line-height: 1.8;
}

.bookings-section {
    padding: 70px 0 90px;
}

.section-heading {
    display: flex;
    justify-content: space-between;
    align-items: end;
    flex-wrap: wrap;
    gap: 16px;
    margin-bottom: 25px;
}

.section-heading h2 {
    margin: 12px 0 0;
    color: #460233;
    font-family: Georgia, serif;
    font-size: 34px;
}

.booking-count {
    color: #987d90;
    font-size: 14px;
}

.demo-message {
    margin: 0 0 28px;
    padding: 15px 18px;
    border-radius: 12px;
    background: #f9eef6;
    color: #76556c;
    font-size: 13px;
    line-height: 1.7;
}

.demo-message i {
    margin-right: 8px;
    color: #b33791;
}

.bookings-grid {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    align-items: start;
    gap: 24px;
}

/* Кнопка нового запису */
.new-booking-area {
    display: flex;
    justify-content: center;
    margin-top: 38px;
}

.primary-button {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    gap: 10px;
    padding: 14px 28px;
    border-radius: 30px;
    background: #b33791;
    color: white;
    text-decoration: none;
    font-weight: 600;
}

.primary-button:hover {
    background: #962878;
    color: white;
}

/* Порожній список */
.empty-state {
    padding: 65px 20px;
    border: 1px solid #f7e1f7;
    border-radius: 20px;
    background: white;
    text-align: center;
}

.empty-icon {
    display: flex;
    justify-content: center;
    align-items: center;
    width: 80px;
    height: 80px;
    margin: 0 auto 22px;
    border-radius: 50%;
    background: #f9e9f4;
    color: #b33791;
    font-size: 30px;
}

.empty-state h3 {
    color: #460233;
    font-size: 24px;
}

.empty-state p {
    margin: 15px 0 25px;
    color: #76556c;
}

@media (max-width: 768px) {
    .bookings-grid {
        grid-template-columns: 1fr;
    }

    .bookings-hero {
        padding: 55px 0;
    }

    .bookings-section {
        padding: 45px 0 65px;
    }

    .section-heading h2 {
        font-size: 29px;
    }
}
</style>