<script setup>
import { ref } from 'vue'
import BookingCard from '../components/BookingCard.vue'
import MasterSchedule from '../components/MasterSchedule.vue'

const tabs = [
    {
        id: 'bookings',
        title: 'Записи',
        icon: 'fa-solid fa-clipboard-list',
    },
    {
        id: 'services',
        title: 'Послуги',
        icon: 'fa-solid fa-briefcase',
    },
    {
        id: 'schedule',
        title: 'Графік',
        icon: 'fa-solid fa-calendar-days',
    },
]

const activeTab = ref('bookings')
const master = {
    name: "Ім'я майстра",
    specialization: 'Майстер краси',
}

const bookings = [
    {
        id: 1,
        serviceName: 'Манікюр',
        date: '26.11.2026',
        startTime: '11:00',
        endTime: '12:00',
        status: 'CONFIRMED',
        customerName: 'Олена Коваль',
        customerPhone: '+380000000001',
    },
    {
        id: 2,
        serviceName: 'Оформлення брів',
        date: '27.11.2026',
        startTime: '14:00',
        endTime: '14:45',
        status: 'CONFIRMED',
        customerName: 'Марія Петренко',
        customerPhone: '+380000000002',
    },
]

const services = [
    {
        id: 1,
        name: 'Манікюр',
        duration: 60,
        price: 500,
    },
    {
        id: 2,
        name: 'Педикюр',
        duration: 90,
        price: 700,
    },
    {
        id: 3,
        name: 'Оформлення брів',
        duration: 45,
        price: 350,
    },
]

const confirmedCount = bookings.filter(
    (booking) => booking.status === 'CONFIRMED'
).length
</script>

<template>
    <div class="master-page">

        <section class="master-hero">
            <div class="page-container">
                <h1>Панель майстра</h1>
                <p>
                    Керування записами, послугами
                    та робочим графіком.
                </p>
            </div>
        </section>

        <section class="dashboard-section">
            <div class="page-container">
                <div class="welcome-block">
                    <div class="master-avatar">
                        <i class="fa-regular fa-user"></i>
                    </div>

                    <div>
                        <h2>{{ master.name }}</h2>
                        <p>{{ master.specialization }}</p>
                    </div>
                </div>

                <div class="stats-grid">
                    <div class="stat-card">
                        <span>Усього записів</span>
                        <strong>{{ bookings.length }}</strong>
                    </div>

                    <div class="stat-card">
                        <span>Підтверджено</span>
                        <strong>{{ confirmedCount }}</strong>
                    </div>

                    <div class="stat-card">
                        <span>Послуги</span>
                        <strong>{{ services.length }}</strong>
                    </div>
                </div>

                <p class="demo-notice">
                    <i class="fa-solid fa-circle-info"></i>
                    Це демонстраційні дані для ЛР №4.
                    Редагування та збереження підключимо пізніше.
                </p>

                <div class="dashboard-layout">

                    <aside class="dashboard-sidebar">
                        <h3>Керування</h3>

                        <nav class="sidebar-navigation">
                            <button v-for="tab in tabs" :key="tab.id" type="button" class="sidebar-button"
                                :class="{ active: activeTab === tab.id }" :aria-pressed="activeTab === tab.id"
                                @click="activeTab = tab.id">
                                <i :class="tab.icon"></i>
                                {{ tab.title }}
                            </button>
                        </nav>
                    </aside>

                    <main class="dashboard-content">

                        <section v-if="activeTab === 'bookings'">
                            <div class="content-heading">
                                <div>
                                    <span class="section-label">
                                        КЛІЄНТИ
                                    </span>
                                    <h2>Записи клієнтів</h2>
                                </div>

                                <span class="item-count">
                                    Записів: {{ bookings.length }}
                                </span>
                            </div>

                            <div v-if="bookings.length" class="booking-list">
                                <BookingCard v-for="booking in bookings" :key="booking.id" :booking="booking"
                                    :show-customer="true" />
                            </div>

                            <p v-else class="empty-message">
                                Поки немає записів клієнтів.
                            </p>

                            <div class="future-feature">
                                <h3>
                                    <i class="fa-solid fa-plus"></i>
                                    Ручне бронювання
                                </h3>

                                <p>
                                    Тут майстер зможе створювати
                                    записи для клієнтів, які звернулися
                                    телефоном або особисто.
                                </p>

                                <span class="feature-label">
                                    Буде реалізовано в ЛР №5
                                </span>
                            </div>
                        </section>

                        <section v-else-if="activeTab === 'services'">
                            <div class="content-heading">
                                <div>
                                    <span class="section-label">
                                        ПРОЦЕДУРИ
                                    </span>
                                    <h2>Мої послуги</h2>
                                </div>
                            </div>

                            <div class="service-list">
                                <article v-for="service in services" :key="service.id" class="master-service-card">
                                    <div>
                                        <h3>{{ service.name }}</h3>

                                        <p>
                                            <i class="fa-regular fa-clock"></i>
                                            {{ service.duration }} хв
                                        </p>
                                    </div>

                                    <strong>
                                        {{ service.price }} грн
                                    </strong>
                                </article>
                            </div>

                            <p class="section-hint">
                                Додавання, редагування та деактивація
                                послуг будуть доступні після
                                підключення до Django REST API.
                            </p>
                        </section>
                        <MasterSchedule v-show="activeTab === 'schedule'" />
                    </main>
                </div>
            </div>
        </section>
    </div>
</template>

<style scoped>
.master-page {
    color: #460233;
}

.page-container {
    width: 100%;
    max-width: 1180px;
    margin: 0 auto;
    padding: 0 20px;
}

.master-hero {
    padding: 65px 0;
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

.master-hero h1 {
    margin: 15px 0;
    font-family: Georgia, serif;
    font-size: clamp(34px, 5vw, 48px);
    color: #460233;
}

.master-hero p {
    margin: 0;
    color: #76556c;
    font-size: 16px;
}

.dashboard-section {
    padding: 50px 0 90px;
}

.welcome-block {
    display: flex;
    align-items: center;
    gap: 18px;
    margin-bottom: 30px;
}

.master-avatar {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 65px;
    height: 65px;
    border-radius: 18px;
    background: #f9e9f4;
    color: #b33791;
    font-size: 27px;
}

.welcome-block h2 {
    margin: 0 0 5px;
    color: #460233;
    font-size: 22px;
}

.welcome-block p {
    margin: 0;
    color: #927489;
}

.stats-grid {
    display: grid;
    grid-template-columns: repeat(3, minmax(0, 1fr));
    gap: 20px;
    margin-bottom: 25px;
}

.stat-card {
    display: flex;
    flex-direction: column;
    gap: 8px;
    padding: 24px;
    border: 1px solid #f7e1f7;
    border-radius: 16px;
    background: white;
    box-shadow: 0 4px 15px rgba(179, 55, 145, 0.06);
}

.stat-card span {
    color: #76556c;
    font-size: 14px;
}

.stat-card strong {
    color: #b33791;
    font-size: 30px;
    line-height: 1;
}

.demo-notice {
    margin-bottom: 30px;
    padding: 14px 18px;
    background: #f9eef6;
    border-radius: 10px;
    color: #76556c;
    font-size: 13px;
}

.demo-notice i {
    color: #b33791;
    margin-right: 7px;
}

.dashboard-layout {
    display: grid;
    grid-template-columns: 230px minmax(0, 1fr);
    align-items: start;
    gap: 25px;
}

.dashboard-sidebar,
.dashboard-content {
    background: white;
    border: 1px solid #f7e1f7;
    border-radius: 18px;
    box-shadow: 0 4px 15px rgba(179, 55, 145, 0.05);
}

.dashboard-sidebar {
    padding: 22px 14px;
}

.dashboard-sidebar h3 {
    padding: 0 12px;
    margin-bottom: 20px;
    color: #460233;
    font-size: 16px;
}

.sidebar-navigation {
    display: flex;
    flex-direction: column;
    gap: 6px;
}

.sidebar-button {
    display: flex;
    align-items: center;
    gap: 12px;
    width: 100%;
    padding: 13px 15px;
    background: transparent;
    border: none;
    border-radius: 10px;
    color: #76556c;
    text-align: left;
    font-weight: 500;
    cursor: pointer;
}

.sidebar-button i {
    width: 20px;
    color: #b33791;
}

.sidebar-button:hover,
.sidebar-button.active {
    background: #f9e9f4;
    color: #b33791;
}

.sidebar-button.active {
    font-weight: 700;
}

.dashboard-content {
    min-height: 400px;
    padding: 28px;
}

.content-heading {
    display: flex;
    justify-content: space-between;
    align-items: end;
    flex-wrap: wrap;
    gap: 12px;
    margin-bottom: 28px;
}

.content-heading h2 {
    margin: 10px 0 0;
    color: #460233;
    font-family: Georgia, serif;
    font-size: 28px;
}

.item-count {
    color: #987d90;
    font-size: 13px;
}

.booking-list {
    display: grid;
    gap: 18px;
}

.empty-message {
    color: #76556c;
    text-align: center;
    padding: 35px;
}

.future-feature {
    margin-top: 30px;
    padding: 22px;
    background: #fefafe;
    border: 1px dashed #e7bfd9;
    border-radius: 14px;
}

.future-feature h3 {
    color: #460233;
    font-size: 18px;
}

.future-feature h3 i {
    color: #b33791;
    margin-right: 8px;
}

.future-feature p {
    color: #76556c;
    line-height: 1.7;
    font-size: 14px;
}

.feature-label {
    display: inline-block;
    padding: 7px 12px;
    background: #f9e9f4;
    border-radius: 20px;
    color: #b33791;
    font-size: 12px;
}

.service-list {
    display: grid;
    gap: 14px;
}

.master-service-card {
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
    gap: 18px;
    padding: 22px;
    border: 1px solid #f7e1f7;
    border-radius: 14px;
}

.master-service-card h3 {
    margin-bottom: 9px;
    color: #460233;
    font-size: 18px;
}

.master-service-card p {
    margin: 0;
    color: #927489;
    font-size: 14px;
}

.master-service-card p i {
    color: #b33791;
    margin-right: 5px;
}

.master-service-card strong {
    color: #b33791;
    font-size: 18px;
}

.schedule-list {
    border: 1px solid #f7e1f7;
    border-radius: 14px;
    overflow: hidden;
}

.schedule-row {
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
    gap: 12px;
    padding: 17px 20px;
    border-bottom: 1px solid #f7e1f7;
}

.schedule-row:last-child {
    border-bottom: none;
}

.schedule-row strong {
    color: #460233;
    font-size: 14px;
}

.schedule-row span {
    color: #76556c;
    font-size: 14px;
}

.schedule-row .day-off {
    color: #b33791;
}

.section-hint {
    margin: 22px 0 0;
    color: #927489;
    font-size: 13px;
    line-height: 1.7;
}

@media (max-width: 900px) {
    .dashboard-layout {
        grid-template-columns: 1fr;
    }

    .sidebar-navigation {
        flex-direction: row;
        flex-wrap: wrap;
    }

    .sidebar-button {
        width: auto;
    }
}

@media (max-width: 576px) {
    .master-hero {
        padding: 50px 0;
    }

    .dashboard-section {
        padding: 35px 0 60px;
    }

    .stats-grid {
        gap: 10px;
    }

    .stat-card {
        padding: 15px;
    }

    .stat-card span {
        font-size: 12px;
    }

    .stat-card strong {
        font-size: 24px;
    }

    .dashboard-content {
        padding: 20px;
    }

    .content-heading h2 {
        font-size: 25px;
    }

    .sidebar-button {
        padding: 10px;
        font-size: 13px;
    }
}
</style>